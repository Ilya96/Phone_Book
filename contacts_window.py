# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.uic import loadUi
from edit_window import EditWindowPresenter
from message_window import MessageWindowPresenter


class ContactsWindowPresenter(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        loadUi('ContactsWindow.ui', self)
        self.parent = parent
        self.setWindowTitle(U'Контакты')
        self.setWindowIcon(QIcon('icon.png'))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels([u'Имя', u'Телефон', u'Дата рождения'])
        self.update_table()
        self.editButton.clicked.connect(self.on_editButton_click)
        self.deleteButton.clicked.connect(self.on_deleteButton_click)

    def on_editButton_click(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            MessageWindowPresenter(self, u"Вы не выделили ни одной строки!").show()
        elif len(selected_rows) > 1:
            MessageWindowPresenter(self, u"Вы должны выделить только онду строку!").show()
        else:
            self.edit = EditWindowPresenter(self)
            self.edit.show()

    def on_deleteButton_click(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            MessageWindowPresenter(self, u"Вы не выделили ни одной строки!").show()
        else:
            for row in selected_rows:
                row_number = row.row()
                self.parent.parent.service.delete_contact(self.parent.user_info[0][0],
                                                          self.tableWidget.item(row_number, 0).text(),
                                                          self.tableWidget.item(row_number, 1).text(),
                                                          self.tableWidget.item(row_number, 2).text())
            self.update_table()
            MessageWindowPresenter(self, u"{0} строк удалены!".format(len(selected_rows))).show()

    def update_table(self):
        data = self.parent.parent.service.get_contacts(self.parent.user_info[0][0])
        row = 0
        self.tableWidget.setRowCount(0)
        for tup in data:
            if tup[0][
                0] in self.parent.tableWidget.currentItem().text() and self.parent.tableWidget.currentItem().text() != u'Прочее' \
                    or not (tup[0][0] in u'ЙЦУКЕНГШЩЗЪХФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъэждлорпавыфячсмитьбю') and \
                    self.parent.tableWidget.currentItem().text() == u'Прочее':
                self.tableWidget.setRowCount(row + 1)
                cell_0 = QTableWidgetItem(unicode(tup[0]))
                cell_1 = QTableWidgetItem(tup[1])
                cell_2 = QTableWidgetItem(str(tup[2]))
                self.tableWidget.setItem(row, 0, cell_0)
                self.tableWidget.setItem(row, 1, cell_1)
                self.tableWidget.setItem(row, 2, cell_2)
                row += 1
