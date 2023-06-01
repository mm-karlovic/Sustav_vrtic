from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Dijete import Dijete
from Vrtic import Vrtic
import sqlite3


#


class PretragaDjece(QWidget):
    def __init__(self, pretraga_widget):
        super().__init__()
        self.pretraga_widget = pretraga_widget
        # Nadodala sam ovaj dio za buttone, pa je to u redu
        self.pretraga_widget.findChild(QPushButton, "pretraziButton").clicked.connect(self.pretrazi)
        self.pretraga_widget.findChild(QPushButton, "deleteButton").clicked.connect(self.obrisiDijete)

    def porukaProzor(self, poruka: str, messageType=QMessageBox.Warning):
        print("Called porukaProzor function")
        msgBox = QMessageBox()
        msgBox.setIcon(messageType)
        msgBox.setText(poruka)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def pretrazi(self):
        try:
            todjete = self.pretraga_widget.findChild(QLineEdit, "unosOib").text().strip()

            with sqlite3.connect("DjecjiVrtic.db") as conn:
                naredbe = conn.cursor()
                djeca = naredbe.execute(f"SELECT * FROM child WHERE oib = '{todjete}';").fetchall()

            if djeca:
                tablica_pretrage = self.pretraga_widget.findChild(QTableWidget, "tablicaPretrage")
                tablica_pretrage.setRowCount(len(djeca))
                for i, dijete in enumerate(djeca):
                    tablica_pretrage.setItem(i, 0, QTableWidgetItem(str(dijete[1])))
                    tablica_pretrage.setItem(i, 1, QTableWidgetItem(str(dijete[2])))
                    tablica_pretrage.setItem(i, 2, QTableWidgetItem(str(dijete[3])))
                    tablica_pretrage.setItem(i, 3, QTableWidgetItem(str(dijete[4])))
                    tablica_pretrage.setItem(i, 4, QTableWidgetItem(str(dijete[5])))
                    tablica_pretrage.setItem(i, 5, QTableWidgetItem(str(dijete[6])))
                    tablica_pretrage.setItem(i, 6, QTableWidgetItem(str(dijete[7])))
                    tablica_pretrage.setItem(i, 7, QTableWidgetItem(str(dijete[8])))
                    tablica_pretrage.setItem(i, 8, QTableWidgetItem(str(dijete[9])))
                    tablica_pretrage.setItem(i, 9, QTableWidgetItem(str(dijete[10])))
                    tablica_pretrage.setItem(i, 10, QTableWidgetItem(str(dijete[11])))

            else:
                self.porukaProzor("Nema rezultata za upit: " + todjete, QMessageBox.Information)

        except:
            self.porukaProzor("Pogresan unos za OIB", QMessageBox.Warning)

    def obrisiDijete(self):
        dijeteoib = self.pretraga_widget.findChild(QLineEdit, "unosOib").text().strip()
        with sqlite3.connect("DjecjiVrtic.db") as conn:
            naredbe = conn.cursor()
            todjete = naredbe.execute(f"DELETE FROM child WHERE oib = '{dijeteoib}';")

        self.porukaProzor(f"{dijeteoib} je uspješno izbrisano iz sustava!", QMessageBox.Information)
        self.pretraga_widget.findChild(QLineEdit, "unosOib").clear()
        table = self.pretraga_widget.findChild(QTableWidget, "tablicaPretrage")
        table.clearContents()
        table.setRowCount(0)
