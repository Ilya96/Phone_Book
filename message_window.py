# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QDialog
from PyQt4.uic import loadUi


class MessageWindowPresenter(QDialog):
    def __init__(self, parent, label):
        QDialog.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.parent = parent
        loadUi('MessageWindow.ui', self)
        self.setWindowTitle('!')
        self.setWindowIcon(QIcon('icon.png'))
        self.label.setText(label)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.okButton.clicked.connect(self.on_okButton_click)

    def on_okButton_click(self):
        self.close()