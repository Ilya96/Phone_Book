# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon, QColor
from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.uic import loadUi
from alphabet_window import AlphabetWindowPresenter

class RegistrationWindowPresenter(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.parent = parent
        self.rememberCheckBoxFlag = False
        loadUi('RegistrationWindow.ui', self)
        self.setWindowTitle(u'Регистрация')
        self.setWindowIcon(QIcon('icon.png'))
        self.loginTextEdit.setTextColor(QColor('gray'))
        self.loginTextEdit.setPlainText(u'Имя пользователя')
        self.loginTextEdit.setTextColor(QColor('black'))
        self.passwordTextEdit.setTextColor(QColor('gray'))
        self.passwordTextEdit.setPlainText(u'Пароль')
        self.passwordTextEdit.setTextColor(QColor('black'))
        self.repeatPasswordTextEdit.setTextColor(QColor('gray'))
        self.repeatPasswordTextEdit.setPlainText(u'Повторите пароль')
        self.repeatPasswordTextEdit.setTextColor(QColor('black'))
        self.emailTextEdit.setTextColor(QColor('gray'))
        self.emailTextEdit.setPlainText(u'Адрес электронной почты')
        self.emailTextEdit.setTextColor(QColor('black'))

        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon('icon.png'))
        self.msg.setWindowTitle("!")
        self.msg.setStandardButtons(QMessageBox.Ok)

        self.rememberCheckBox.stateChanged.connect(self.checker)
        self.okButton.clicked.connect(self.on_okButton_click)
        self.cancelButton.clicked.connect(self.on_cancelButton_click)

    def checker(self, state):
        if state == QtCore.Qt.Checked:
            self.rememberCheckBoxFlag = not self.rememberCheckBoxFlag
        else:
            self.rememberCheckBoxFlag = not self.rememberCheckBoxFlag

    def on_cancelButton_click(self):
        self.close()

    def on_okButton_click(self):
        user_info = self.parent.service.get_login(self.loginTextEdit.toPlainText())
        if user_info:
            self.msg.setText(u"Пользователь с таким логином уже есть!")
            self.msg.exec_()
        elif self.passwordTextEdit.toPlainText() != self.repeatPasswordTextEdit.toPlainText():
            self.msg.setText(u"Пароли не совпадают!")
            self.msg.exec_()
        elif self.parent.service.get_email(self.emailTextEdit.toPlainText()):
            self.msg.setText(u"Пользователь с такой электронной почтой уже есть!")
            self.msg.exec_()
        elif len(self.emailTextEdit.toPlainText().split('@')) != 2:
            self.msg.setText(u"Такой формат электронной почты не поддерживается!")
            self.msg.exec_()
        elif not unicode(self.emailTextEdit.toPlainText()).split('@')[1] in ['gmail.com', 'mail.ru', 'yandex.ru']:
            self.msg.setText(u"Такой формат электронной почты не поддерживается!")
            self.msg.exec_()
        else:
            self.parent.service.delete_remember()
            if self.rememberCheckBoxFlag:
                self.parent.service.set_remember(self.loginTextEdit.toPlainText(), self.passwordTextEdit.toPlainText())
            self.parent.service.post_user(self.loginTextEdit.toPlainText(), self.passwordTextEdit.toPlainText(), self.emailTextEdit.toPlainText(), self.bornDateEdit.text())
            self.hide()
            self.parent.hide()
            self.parent.main = AlphabetWindowPresenter(self.parent, self.parent.service.get_login(self.loginTextEdit.toPlainText()))
            self.parent.main.show()