# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from PyQt4.uic import loadUi
from alphabet_window import AlphabetWindowPresenter
from new_password_window import NewPasswordWindowPresenter
from registration_window import RegistrationWindowPresenter
from  data_provider import Service

class AuthorizationWindowPresenter(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi('AuthorizationWindow.ui', self)
        self.setWindowTitle(U'Авторизация')
        self.passwordTextEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.setWindowIcon(QIcon('icon.png'))
        self.service = Service()
        self.rememberCheckBoxFlag = False
        self.remember_data = self.service.get_remember()
        self.rememberCheckBox.stateChanged.connect(self.checker)
        self.showPasswordCheckBox.stateChanged.connect(self.hider)
        self.registrationButton.clicked.connect(self.on_registrationButton_click)
        self.cancelButton.clicked.connect(self.on_cancelButton_click)
        self.logInButton.clicked.connect(self.on_logInButton_click)
        self.forgotPasswordLink.clicked.connect(self.on_forgotPasswordLink_click)

        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon('icon.png'))
        self.msg.setWindowTitle("!")
        self.msg.setStandardButtons(QMessageBox.Ok)

    def hider(self, state):
        if state == QtCore.Qt.Checked:
            self.passwordTextEdit.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            self.passwordTextEdit.setEchoMode(QtGui.QLineEdit.Password)

    def checker(self, state):
        if state == QtCore.Qt.Checked:
            self.rememberCheckBoxFlag = not self.rememberCheckBoxFlag
        else:
            self.rememberCheckBoxFlag = not self.rememberCheckBoxFlag

    def on_registrationButton_click(self):
        self.add = RegistrationWindowPresenter(self)
        self.add.show()

    def on_cancelButton_click(self):
        self.close()

    def on_logInButton_click(self):
        if self.service.get_user(self.loginTextEdit.toPlainText(), self.passwordTextEdit.text()):
            self.service.delete_remember()
            if self.rememberCheckBoxFlag:
                self.service.set_remember(self.loginTextEdit.toPlainText(), self.passwordTextEdit.text())
            self.hide()
            self.main = AlphabetWindowPresenter(self, self.service.get_login(self.loginTextEdit.toPlainText()))
            self.main.show()
        else:
            self.msg.setText(u"Пользователь с такими данными не найден!")
            self.msg.exec_()

    def on_forgotPasswordLink_click(self):
        self.add = NewPasswordWindowPresenter(self)
        self.add.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AuthorizationWindowPresenter()
    if widget.remember_data:
        widget.main = AlphabetWindowPresenter(widget, widget.service.get_login(widget.remember_data[0][0]))
        widget.main.show()
    else:
        widget.show()
    sys.exit(app.exec_())