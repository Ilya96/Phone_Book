# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon, QColor
from PyQt4.QtGui import QDialog
from PyQt4.uic import loadUi
from message_window import MessageWindowPresenter


class AddWindowPresenter(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.parent = parent
        loadUi('AddWindow.ui', self)
        self.setWindowTitle(u'Добавление нового контакта')
        self.setWindowIcon(QIcon('icon.png'))
        self.loginTextEdit.setTextColor(QColor('gray'))
        self.loginTextEdit.setPlainText(u'Имя контактного лица')#(u'Петя')
        self.loginTextEdit.setTextColor(QColor('black'))
        self.phoneNumberTextEdit.setTextColor(QColor('gray'))
        self.phoneNumberTextEdit.setPlainText(u"Номер телефона (цифры после '+7')")#('9653838383')
        self.phoneNumberTextEdit.setTextColor(QColor('black'))

        self.okButton.clicked.connect(self.on_okButton_click)
        self.cancelButton.clicked.connect(self.on_cancelButton_click)

    def on_cancelButton_click(self):
        self.close()

    def on_okButton_click(self):
        if unicode(self.phoneNumberTextEdit.toPlainText()).isdigit() and len(self.phoneNumberTextEdit.toPlainText()) == 10:
            answer = self.parent.parent.service.post_contact(self.parent.user_info[0][0], self.loginTextEdit.toPlainText(), self.phoneNumberTextEdit.toPlainText(),  self.bornDateEdit.text())
            if answer == 0:
                if unicode(self.loginTextEdit.toPlainText())[0] in u'ЙЦУКЕНГШЩЗЪХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' \
                                                          u'йцукенгшщзхъэждлорпавыфячсмитьбю':
                    message_window = MessageWindowPresenter(self, u"Контакт успешно добавлен в алфавитном\n "
                                                                  u"порядке на страницу с буквой '" + self.loginTextEdit.toPlainText()[0] + "'!")
                else:
                    message_window = MessageWindowPresenter(self, u"Контакт успешно добавлен в алфавитном\n "
                                                                  u"порядке на страницу 'Прочее'!")
            else:
                message_window = MessageWindowPresenter(self, u"Такой контакт у вас уже есть!")
        else:
            message_window = MessageWindowPresenter(self, u"Номер телефона должен содержать только\n "
                                                          u"10 цифр без разделителей! (цифры после '7+')")
        message_window.show()
