# Form implementation generated from reading ui file 'C:\Users\Bananator\PycharmProjects\BorodaChat\client\gui_client\gui_authentification_2.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 481)
        Dialog.setModal(True)
        self.IPTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.IPTextEdit.setGeometry(QtCore.QRect(20, 70, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IPTextEdit.setFont(font)
        self.IPTextEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.IPTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.IPTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.IPTextEdit.setPlaceholderText("")
        self.IPTextEdit.setObjectName("IPTextEdit")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 150, 331, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 19, 331, 41))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.PingButton = QtWidgets.QPushButton(Dialog)
        self.PingButton.setGeometry(QtCore.QRect(20, 110, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PingButton.setFont(font)
        self.PingButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.PingButton.setObjectName("PingButton")
        self.mainlabel = QtWidgets.QLabel(Dialog)
        self.mainlabel.setGeometry(QtCore.QRect(10, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mainlabel.setFont(font)
        self.mainlabel.setObjectName("mainlabel")
        self.iplabel = QtWidgets.QLabel(Dialog)
        self.iplabel.setGeometry(QtCore.QRect(20, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.iplabel.setFont(font)
        self.iplabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.iplabel.setObjectName("iplabel")
        self.portlabel = QtWidgets.QLabel(Dialog)
        self.portlabel.setGeometry(QtCore.QRect(186, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portlabel.setFont(font)
        self.portlabel.setObjectName("portlabel")
        self.PortTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.PortTextEdit.setGeometry(QtCore.QRect(280, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PortTextEdit.setFont(font)
        self.PortTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PortTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PortTextEdit.setObjectName("PortTextEdit")
        self.AuthTabWidget = QtWidgets.QTabWidget(Dialog)
        self.AuthTabWidget.setGeometry(QtCore.QRect(10, 190, 321, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AuthTabWidget.setFont(font)
        self.AuthTabWidget.setObjectName("AuthTabWidget")
        self.auth_tab = QtWidgets.QWidget()
        self.auth_tab.setObjectName("auth_tab")
        self.loginlabel = QtWidgets.QLabel(self.auth_tab)
        self.loginlabel.setGeometry(QtCore.QRect(12, 9, 61, 31))
        self.loginlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loginlabel.setObjectName("loginlabel")
        self.LoginTextEdit = QtWidgets.QPlainTextEdit(self.auth_tab)
        self.LoginTextEdit.setGeometry(QtCore.QRect(76, 13, 231, 31))
        self.LoginTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.LoginTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.LoginTextEdit.setObjectName("LoginTextEdit")
        self.passwordlabel = QtWidgets.QLabel(self.auth_tab)
        self.passwordlabel.setGeometry(QtCore.QRect(11, 47, 61, 31))
        self.passwordlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.passwordlabel.setObjectName("passwordlabel")
        self.PasswordTextEdit = QtWidgets.QPlainTextEdit(self.auth_tab)
        self.PasswordTextEdit.setGeometry(QtCore.QRect(76, 51, 231, 31))
        self.PasswordTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PasswordTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PasswordTextEdit.setObjectName("PasswordTextEdit")
        self.LoginButton = QtWidgets.QPushButton(self.auth_tab)
        self.LoginButton.setGeometry(QtCore.QRect(100, 90, 141, 31))
        self.LoginButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LoginButton.setObjectName("LoginButton")
        self.AuthTabWidget.addTab(self.auth_tab, "")
        self.regist_tab = QtWidgets.QWidget()
        self.regist_tab.setObjectName("regist_tab")
        self.RegistTextEdit = QtWidgets.QPlainTextEdit(self.regist_tab)
        self.RegistTextEdit.setGeometry(QtCore.QRect(10, 30, 291, 31))
        self.RegistTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RegistTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RegistTextEdit.setObjectName("RegistTextEdit")
        self.nicknamelabel = QtWidgets.QLabel(self.regist_tab)
        self.nicknamelabel.setGeometry(QtCore.QRect(10, 10, 321, 21))
        self.nicknamelabel.setObjectName("nicknamelabel")
        self.emaillabel = QtWidgets.QLabel(self.regist_tab)
        self.emaillabel.setGeometry(QtCore.QRect(10, 70, 321, 21))
        self.emaillabel.setObjectName("emaillabel")
        self.RegistEmailTextEdit = QtWidgets.QPlainTextEdit(self.regist_tab)
        self.RegistEmailTextEdit.setGeometry(QtCore.QRect(10, 90, 291, 31))
        self.RegistEmailTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RegistEmailTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RegistEmailTextEdit.setObjectName("RegistEmailTextEdit")
        self.registpasswordlabel = QtWidgets.QLabel(self.regist_tab)
        self.registpasswordlabel.setGeometry(QtCore.QRect(10, 130, 321, 21))
        self.registpasswordlabel.setObjectName("registpasswordlabel")
        self.RegistPasswordTextEdit = QtWidgets.QPlainTextEdit(self.regist_tab)
        self.RegistPasswordTextEdit.setGeometry(QtCore.QRect(10, 150, 291, 31))
        self.RegistPasswordTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RegistPasswordTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RegistPasswordTextEdit.setObjectName("RegistPasswordTextEdit")
        self.RegistButton = QtWidgets.QPushButton(self.regist_tab)
        self.RegistButton.setGeometry(QtCore.QRect(20, 190, 211, 31))
        self.RegistButton.setObjectName("RegistButton")
        self.AuthTabWidget.addTab(self.regist_tab, "")

        self.retranslateUi(Dialog)
        self.AuthTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.IPTextEdit.setPlainText(_translate("Dialog", "127.0.0.1"))
        self.PingButton.setText(_translate("Dialog", "Проверить соединение с сервером"))
        self.mainlabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#55557f;\">Corporative Chat</span><span style=\" color:#55557f; vertical-align:super;\">1.0 </span></p></body></html>"))
        self.iplabel.setText(_translate("Dialog", "IP:"))
        self.portlabel.setText(_translate("Dialog", "Port:"))
        self.PortTextEdit.setPlainText(_translate("Dialog", "5000"))
        self.loginlabel.setText(_translate("Dialog", "Логин:"))
        self.passwordlabel.setText(_translate("Dialog", "Пароль:"))
        self.LoginButton.setText(_translate("Dialog", "Войти"))
        self.AuthTabWidget.setTabText(self.AuthTabWidget.indexOf(self.auth_tab), _translate("Dialog", "Вход"))
        self.nicknamelabel.setText(_translate("Dialog", "Введите ник в чате:"))
        self.emaillabel.setText(_translate("Dialog", "Введите Email/Логин:"))
        self.registpasswordlabel.setText(_translate("Dialog", "Введите пароль:"))
        self.RegistButton.setText(_translate("Dialog", "Регистрация"))
        self.AuthTabWidget.setTabText(self.AuthTabWidget.indexOf(self.regist_tab), _translate("Dialog", "Регистрация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
