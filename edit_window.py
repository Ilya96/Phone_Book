# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtCore import QDate
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QDialog
from PyQt4.uic import loadUi
from message_window import MessageWindowPresenter

class EditWindowPresenter(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.parent = parent
        loadUi('AddWindow.ui', self)
        self.setWindowTitle(u'Редактирование контакта')
        self.setWindowIcon(QIcon('icon.png'))
        self.loginTextEdit.setPlainText(unicode(self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 0).text()))
        self.phoneNumberTextEdit.setPlainText(self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 1).text())
        date = self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 2).text().split('-')
        self.bornDateEdit.setDate(QDate(int(date[0]), int(date[1]), int(date[2])))

        self.okButton.clicked.connect(self.on_okButton_click)
        self.cancelButton.clicked.connect(self.on_cancelButton_click)

    def on_cancelButton_click(self):
        self.close()

    def on_okButton_click(self):
        if unicode(self.phoneNumberTextEdit.toPlainText()).isdigit() and len(self.phoneNumberTextEdit.toPlainText()) == 10:
            answer = self.parent.parent.parent.service.put_contact(self.parent.parent.user_info[0][0],
                self.loginTextEdit.toPlainText(),
                self.phoneNumberTextEdit.toPlainText(),
                self.bornDateEdit.text(),
                self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 0).text(),
                self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 1).text(),
                self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 2).text())
            self.parent.update_table()
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