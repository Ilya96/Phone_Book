# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.uic import loadUi


class BirthdaysWindowPresenter(QDialog):
    def __init__(self, parent, dates):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        loadUi('Birthdays.ui', self)
        self.parent = parent
        self.dates = dates
        self.setWindowTitle(u'Ближайшие именинники!')
        self.setWindowIcon(QIcon('icon.png'))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels([u'Имя', u'Телефон', u'Дата рождения'])
        self.init_table()

    def init_table(self):
        row = 0
        self.tableWidget.setRowCount(0)
        for tup in self.dates:
            if True:
                self.tableWidget.setRowCount(row + 1)
                cell_0 = QTableWidgetItem(unicode(tup[0]))
                cell_1 = QTableWidgetItem(tup[1])
                cell_2 = QTableWidgetItem(str(tup[2]))
                self.tableWidget.setItem(row, 0, cell_0)
                self.tableWidget.setItem(row, 1, cell_1)
                self.tableWidget.setItem(row, 2, cell_2)
                row += 1
