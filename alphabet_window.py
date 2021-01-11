# -*- coding: utf-8 -*-
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QDialog, QTableWidgetItem, QTableWidget
from PyQt4.uic import loadUi
from add_window import AddWindowPresenter
from contacts_window import ContactsWindowPresenter
from birthdays_window import BirthdaysWindowPresenter
from datetime import date


class AlphabetWindowPresenter(QDialog):
    ALPHABET = [u'АБ', u'ВГ', u'ДЕ', u'ЖЗИЙ', u'КЛ', u'МН', u'ОП', u'РС', u'ТУ', u'ФХ', u'ЦЧШЩ', u'ЪЫЬЭ', u'ЮЯ',
                u'Прочее']

    def __init__(self, parent, user_info):
        QDialog.__init__(self, parent)
        loadUi('AlphabetWindow2.ui', self)
        self.parent = parent
        self.user_info = user_info
        self.setWindowTitle(U'Здравствуйте, ' + user_info[0][1] + '!')
        self.setWindowIcon(QIcon('icon.png'))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels([u'Строка'])
        self.tableWidget.setRowCount(len(self.ALPHABET))
        row = 0
        for i in self.ALPHABET:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(unicode(i)))
            row += 1
        data = self.parent.service.get_contacts(self.user_info[0][0])
        dates = []
        for i in data:
            day = date(date.today().year, i[2].month, i[2].day)
            delta = day - date.today()
            if 7 > delta.days > 0:
                dates.append(i)
        if len(dates):
            self.add = BirthdaysWindowPresenter(self, dates)
            self.add.show()
        self.addButton.clicked.connect(self.on_addButton_click)
        self.exitButton.clicked.connect(self.on_exitButton_click)
        self.tableWidget.mousePressEvent = self.mousePressEvent

    def on_addButton_click(self):
        self.add = AddWindowPresenter(self)
        self.add.show()

    def on_exitButton_click(self):
        self.parent.service.delete_remember()
        self.parent.show()
        self.hide()

    def mousePressEvent(self, e):
        QTableWidget.mousePressEvent(self.tableWidget, e)  # в начале правильная обработка
        if e.button() == Qt.LeftButton:
            self.contacts = ContactsWindowPresenter(self)
            self.contacts.show()
