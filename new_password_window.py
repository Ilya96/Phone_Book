# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon, QColor
from PyQt4.QtGui import QDialog
from PyQt4.uic import loadUi

class NewPasswordWindowPresenter(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.parent = parent
        loadUi('NewPasswordWindow.ui', self)
        self.setWindowTitle(u'Восстановление пароля')
        self.setWindowIcon(QIcon('icon.png'))
        self.emailTextEdit.setTextColor(QColor('gray'))
        self.emailTextEdit.setPlainText(u'Адрес электронной почты')
        self.emailTextEdit.setTextColor(QColor('black'))

        self.cancelButton.clicked.connect(self.on_cancelButton_click)
        self.changePasswordButton.clicked.connect(self.on_changePasswordButton_click)

    def on_cancelButton_click(self):
        self.close()

    def on_changePasswordButton_click(self):
        pass