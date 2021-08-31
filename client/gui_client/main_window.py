import json.decoder
import sys
import arrow
import requests.exceptions

from hashlib import sha256
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox
from client.gui_client.gui_authentification import Ui_Dialog
from client.gui_client.gui_design import Ui_MainWindow
from client.request_manager import HttpClient


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    _login = ''
    _password = ''
    _user = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dialog = QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)

        self.auth_window = self.dialog.ui

        self.auth_window.RegistButton.clicked.connect(self.registration)
        self.auth_window.LoginButton.clicked.connect(self.show_chat)
        self.auth_window.PingButton.clicked.connect(self.check_server_status)
        self.UserList.itemClicked.connect(self.update_messages_widget)
        self.window().UpdateButton.clicked.connect(self.all_db_messages)

        self.client = HttpClient()
        self.user_nick = None
        self.msgbox = QMessageBox()
        self.dialog.exec()

    def show_chat(self):
        login = self.auth_window.LoginTextEdit.toPlainText()
        password = str(sha256(self.auth_window.PasswordTextEdit.toPlainText().encode('utf-8')).hexdigest())
        response = self.auth(login, password)
        if response != 'denied':
            self.window().show()
            self.UserLabel.setText(response)
            MainWindow._login = login
            MainWindow._password = password
            MainWindow._user = response
            self.dialog.hide()
            try:
                messages = self.all_db_messages()
                if list(messages.keys())[0] == 'response':
                    if messages['response'] == 'no_messages':
                        self.msgbox.information(self, 'Внимание', 'К сожалению, для вас пока нет сообщений.')
                    if messages['response'] == 'dict_error':
                        self.msgbox.critical(self, 'Ошибка', 'Ошибка сервера.')
            except json.decoder.JSONDecodeError:
                self.msgbox.critical(self, 'Ошибка', 'Некорректные данные!')
            else:
                self.update_users_widget()
            self.UserList.setCurrentRow(0)

    def all_db_messages(self):
        messages = self.client.get_messages(MainWindow._login, MainWindow._password)
        print(self._login, self._password)
        print(messages)
        return messages

    def get_users(self):
        users = self.client.get_users(MainWindow._login, MainWindow._password)
        return users

    def registration(self):
        registration_body = {
            "nickname": self.auth_window.RegistTextEdit.toPlainText(),
            "login": self.auth_window.RegistEmailTextEdit.toPlainText(),
            "password": str(sha256(self.auth_window.RegistPasswordTextEdit.toPlainText().encode('utf-8')).hexdigest())
        }

        assert '' not in registration_body.values(), f'Some fields is empty. {registration_body.values()}'

        response = self.client.registration(registration_body)['response']

        if response == 'added':
            self.auth_window.RegistStatusLabel.setText(f'Пользователь успешно зарегистрирован.')
            self.auth_window.RegistStatusLabel.setStyleSheet('color: green')
        elif response == 'user_exists':
            self.auth_window.RegistStatusLabel.setText(f'Пользователь с таким логином уже зарегистрирован!')
            self.auth_window.RegistStatusLabel.setStyleSheet('color: red')
        elif response == 'nickname_exists':
            self.auth_window.RegistStatusLabel.setText(f'Пользователь с таким ником уже зарегистрирован!')
            self.auth_window.RegistStatusLabel.setStyleSheet('color: red')
        else:
            self.auth_window.RegistStatusLabel.setText(f'Что-то пошло не так.')
            self.auth_window.RegistStatusLabel.setStyleSheet('color: red')

    def auth(self, login, password):
        credentials = {
            "login": login,
            "password": password,
        }
        response = self.client.login(credentials)
        self.user_nick = response.get('response')
        self._login = credentials['login']
        self._password = credentials['password']

        if self.user_nick == 'denied':
            self.msgbox.setWindowTitle('Сервер')
            self.msgbox.setText("Неверный логин/пароль!")
            self.msgbox.exec()
            return 'denied'
        else:
            return response['response']

    # получение ВСЕХ сообщений из базы

    def update_users_widget(self):
        self.UserList.addItem(f'Общий чат')
        users = self.client.get_users(MainWindow._login, MainWindow._password)
        if len(users) != 0:
            for user in users:
                if user != self._user:
                    self.UserList.addItem(user)

    #   time = self.messageList.item(self.messageList.count() - 1).text()
    # НЕ АКТУАЛЬНО
    # добавление ВСЕХ требуемых сообщений из 'messages_to_add'
    def update_messages_widget(self):
        messages = []
        guest = self.UserList.currentItem().text()
        print(window._login, window._password, guest)
        user_messages = self.client.get_messages(MainWindow._login, MainWindow._password)
        print(user_messages)
        for message in user_messages[guest]:
            parsed_message = f'|{message["time"]} | {message["sender"]}: {message["message"]}'
            messages.append(parsed_message)
        if messages:
            self.add_user_messages(messages, guest)

    def add_user_messages(self, messages_to_add, guest) -> None:
        if messages_to_add != 0:
            for message in messages_to_add:
                if message not in self.MessageList.selectedItems():
                    self.add_message_to_widget(message, guest)

        self.MessageList.scrollToBottom()

    # НЕ АКТУАЛЬНО
    # добавление одного(!) сообщения
    def add_message_to_widget(self, message: dict, guest) -> None:
        sender = message[25:30]
        if sender == guest:
            item = self.MessageList.item('%s' % message)
            item.setBackground('red')
            self.MessageList.addItem(item)

    # НЕ АКТУАЛЬНО
    # отправляем сообщение и обновляем сообщения с сервера
    # !!!убрать 'update_messages()' и 'check_server_status()' после реализации автоматического обновления
    def send_message(self) -> None:
        sender = self.UserLabel.text()
        if self.MessageLineEdit.text() != '':  # если поля не пустые
            text = self.messageLineEdit.text()  # текст сообщения
            self.client.send_message(text, sender)  # отправляем имя пользователя, сообщение и время
            self.update_widget()  # обновляем сообщения с сервера
            self.messageLineEdit.clear()  # очищаем поле ввода сообщения ('messageLineEdit')
            self.check_server_status()

    # пинг\проверка соединения
    def check_server_status(self):
        host = {
            "ip": self.auth_window.IPTextEdit.toPlainText(),
            "port": self.auth_window.PortTextEdit.toPlainText()
        }
        try:
            self.client.base_url = f'http://{host["ip"]}:{host["port"]}'
            if self.client.check_server()["status"] == 'online':
                self.msgbox.setWindowTitle('Сервер')
                self.msgbox.setText('Соединение с сервером установлено!')
                self.msgbox.exec()
        except requests.exceptions.ConnectionError:
            self.raise_message('Сервер', 'Сервер недоступен, проверьте введенный адрес')


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    window = MainWindow()  # создаём объект класса ExampleApp
    app.exec()  # запускаем движок
