from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Dijete import Dijete
from Vrtic import Vrtic
import sqlite3


class PretragaVrtica(QWidget):
    def __init__(self, pretragaVrtica_widget):
        super().__init__()
        self.pretragaVrtica_widget = pretragaVrtica_widget

        self.pretragaVrtica_widget.findChild(QPushButton, "pretraziVrtic").clicked.connect(self.pretrazi)

    def __porukaProzor(self, poruka):
        porukaProzor = QMessageBox()
        porukaProzor.setIcon(QMessageBox.Warning)
        porukaProzor.setText(poruka)
        porukaProzor.setStandardButtons(QMessageBox.Ok)
        porukaProzor.exec()

    def pretrazi(self):
        try:
            vrtici = None
            tajvrtic = self.pretragaVrtica_widget.findChild(QLineEdit, "nazivVrtica").text().strip()

            with sqlite3.connect("DjecjiVrtic.db") as conn:
                naredbe = conn.cursor()
                vrtici = naredbe.execute(f"SELECT * FROM kindergarten WHERE NAME = '{tajvrtic}';").fetchall()

            if len(vrtici) == 0:
                self.__porukaProzor("Vrtić s tim imenom NE POSTOJI!!")
            else:
                trenutniRedak = 0
                self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setRowCount(len(vrtici))
                self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setColumnCount(len(vrtici[0]) - 1)

                for vrtic in vrtici:

                    self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setItem(trenutniRedak, 0, QTableWidgetItem(str(vrtic[1])))
                    self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setItem(trenutniRedak, 1, QTableWidgetItem(str(vrtic[2])))
                    self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setItem(trenutniRedak, 2, QTableWidgetItem(str(vrtic[3])))
                    self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setItem(trenutniRedak, 3, QTableWidgetItem(str(vrtic[4])))
                    self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setItem(trenutniRedak, 4, QTableWidgetItem(str(vrtic[5])))
                    self.pretragaVrtica_widget.findChild(QTableWidget, "tablicaPretrageVrtica").setItem(trenutniRedak, 5, QTableWidgetItem(str(vrtic[6])))
                    trenutniRedak += 1
        except Exception as exc:
            self.__porukaProzor(str(exc))