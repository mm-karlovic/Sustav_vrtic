import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Dijete import Dijete
from Vrtic import Vrtic
import sqlite3
from PregledDjece import PregledDjece
from PretragaDjece import PretragaDjece


class UnosDjeteta(QWidget):
    def __init__(self, unos_widget):
        super().__init__()
        self.unos_widget = unos_widget

        with sqlite3.connect("DjecjiVrtic.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT \"name\" FROM kindergarten ORDER BY id ASC")
            nazivi_vrtica = cursor.fetchall()
            cursor.execute("SELECT \"group\" FROM kindergarten")
            grupe_vrtic = cursor.fetchone()
            if grupe_vrtic:
                grupe_string = grupe_vrtic[0]
                grupe_lista = grupe_string.split('|')

            cursor.execute("SELECT \"programs\" FROM kindergarten")
            programi_vrtic = cursor.fetchone()
            if programi_vrtic:
                programi_string = programi_vrtic[0]
                programi_lista = programi_string.split('|')

        for row in nazivi_vrtica:
            self.unos_widget.findChild(QComboBox, "vrticcomboBox").addItem(row[0])

        self.unos_widget.findChild(QComboBox, "skupinaComboBox").addItems(grupe_lista)

        self.unos_widget.findChild(QComboBox, "programComboBox").addItems(programi_lista)
        # UKOLIKO ODABEREMO DRUGU VRIJEDNOST U COMBO BOXU:
        self.unos_widget.findChild(QComboBox, "vrticcomboBox").currentIndexChanged.connect(self.azurirajCombo)
        self.unos_widget.findChild(QPushButton, "unesiDijeteButton").clicked.connect(self.unosBtn)

    def azurirajCombo(self):

        odabrani = self.unos_widget.findChild(QComboBox, "vrticcomboBox").currentText()
        with sqlite3.connect("DjecjiVrtic.db") as conn:
            cursor = conn.cursor()
            # Odabiremo programe i grupe ovisno o odabranom vrticu u prvom Combo Boxu
            cursor.execute("SELECT programs, \"group\" FROM kindergarten WHERE name=?", (odabrani,))
            programi, grupe = cursor.fetchone()

        # Cistimo comboBoxeve
        self.unos_widget.findChild(QComboBox, "programComboBox").clear()
        self.unos_widget.findChild(QComboBox, "skupinaComboBox").clear()

        # DODAJEMO grupe i programe u ComboBox
        for program in programi.split("|"):
            self.unos_widget.findChild(QComboBox, "programComboBox").addItem(program)
        for grupa in grupe.split("|"):
            self.unos_widget.findChild(QComboBox, "skupinaComboBox").addItem(grupa)

    def porukaProzor(self, poruka: str, messageType=QMessageBox.Warning):
        msgBox = QMessageBox()
        msgBox.setIcon(messageType)
        msgBox.setText(poruka)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def unosBtn(self):

        try:
            ime = self.unos_widget.findChild(QLineEdit, "nameText").text().strip()
            prezime = self.unos_widget.findChild(QLineEdit, "surnameText").text().strip()
            oib = self.unos_widget.findChild(QLineEdit, "oibText").text().strip()
            dob = self.unos_widget.findChild(QLineEdit, "ageText").text().strip()
            grad = self.unos_widget.findChild(QLineEdit, "cityText").text().strip()
            drzava = self.unos_widget.findChild(QLineEdit, "countryText").text().strip()
            imeMajke = self.unos_widget.findChild(QLineEdit, "motherText").text().strip()
            imeOca = self.unos_widget.findChild(QLineEdit, "fatherText").text().strip()
            skupina = self.unos_widget.findChild(QComboBox, "skupinaComboBox").currentText()
            program = self.unos_widget.findChild(QComboBox, "programComboBox").currentText()
            biljeska = self.unos_widget.findChild(QLineEdit, "noteText").text().strip()

            oibPostoji = False
            vrtici = self.unos_widget.findChild(QComboBox, "vrticcomboBox").currentText()
            with sqlite3.connect("DjecjiVrtic.db") as conn:
                naredbe = conn.cursor()
                kap = naredbe.execute(f"SELECT capacity FROM kindergarten WHERE name = '{vrtici}';").fetchall()

            if kap[0][0] > 0:

                with sqlite3.connect("DjecjiVrtic.db") as conn:
                    naredbe = conn.cursor()
                    dohvaceni1 = naredbe.execute(f"SELECT * FROM child WHERE OIB = '{oib}';").fetchall()

                    if len(dohvaceni1) > 0:
                        oibPostoji = True

                    if oibPostoji:
                        self.porukaProzor("POGREŠKA! Dijete s tim OIB-om već postoji!!")

                    else:
                        try:
                            novoDijete = Dijete(ime, prezime, oib, dob, grad, drzava, imeMajke, imeOca, skupina,
                                                program,
                                                biljeska)

                            with sqlite3.connect("DjecjiVrtic.db") as conn:
                                naredbe = conn.cursor()
                                naredbe.execute(
                                    f"INSERT INTO child(name, surname, oib, age, city, country, nameMother, nameFather, note, "
                                    f"\"group\", program, kindergarten) VALUES('{ime}','{prezime}','{int(oib)}','{int(dob)}',"
                                    f"'{grad}','{drzava}','{imeMajke}','{imeOca}','{biljeska}', '{skupina}','{program}', "
                                    f"'{vrtici}')")

                                naredbe.execute(
                                    f"UPDATE kindergarten set capacity=capacity -1 WHERE name = '{vrtici}';")
                                conn.commit()

                                self.porukaProzor(f"Dijete {novoDijete.ime} {novoDijete.prezime} uspješno uneseno!!",
                                                  QMessageBox.Information)
                                self.obrisi()
                        except Exception as exc:
                            self.porukaProzor(str(exc))
            else:
                self.porukaProzor("Nema kapaciteta u vrticu za dijete, probajte upisati dijete u drugi vrtic.")


        except Exception as exc:
            self.porukaProzor(str(exc))

    def obrisi(self):
        self.unos_widget.findChild(QLineEdit, "nameText").clear()
        self.unos_widget.findChild(QLineEdit, "surnameText").clear()
        self.unos_widget.findChild(QLineEdit, "oibText").clear()
        self.unos_widget.findChild(QLineEdit, "ageText").clear()
        self.unos_widget.findChild(QLineEdit, "cityText").clear()
        self.unos_widget.findChild(QLineEdit, "countryText").clear()
        self.unos_widget.findChild(QLineEdit, "motherText").clear()
        self.unos_widget.findChild(QLineEdit, "fatherText").clear()

        self.unos_widget.findChild(QLineEdit, "noteText").clear()
