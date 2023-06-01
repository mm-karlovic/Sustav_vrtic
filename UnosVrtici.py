from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Dijete import Dijete
from Vrtic import Vrtic
import sqlite3
from PregledDjece import PregledDjece
from PretragaDjece import PretragaDjece


class UnosVrtici(QWidget):
    def __init__(self, unos_vrtici):
        super().__init__()
        self.unos_vrtici = unos_vrtici
        self.unos_vrtici.findChild(QPushButton, "unosvrticaButton").clicked.connect(self.unosVrtica)

    def porukaProzor(self, poruka: str, messageType=QMessageBox.Warning):
        print("Called porukaProzor function")
        msgBox = QMessageBox()
        msgBox.setIcon(messageType)
        msgBox.setText(poruka)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def unosVrtica(self):

        try:
            naziv = self.unos_vrtici.findChild(QLineEdit, "nazivVrticaText").text().strip()
            adresa = self.unos_vrtici.findChild(QLineEdit, "adresaVrticaText").text().strip()
            mjesto = self.unos_vrtici.findChild(QLineEdit, "mjestoVrticaText").text().strip()
            kapacitet = self.unos_vrtici.findChild(QLineEdit, "kapacitetVrticaText").text().strip()
            programi = self.unos_vrtici.findChild(QTextEdit, "programiEdit").toPlainText()
            skupine = self.unos_vrtici.findChild(QTextEdit, "skupineEdit").toPlainText()
            lista_programa = programi.split('\n')
            lista_skupina = skupine.split('\n')

            with sqlite3.connect("DjecjiVrtic.db") as conn:
                naredbe = conn.cursor()
                naziv_vrtica = naredbe.execute(f"SELECT name FROM kindergarten WHERE name = '{naziv}';").fetchall()

            if len(naziv_vrtica) == 0:

                try:
                    noviVrtic = Vrtic(naziv, mjesto, adresa, int(kapacitet))

                    # U Vrtice moramo unositi liste naziva grupa i naziva programa, odvajamo ih | znakom
                    grupe_string = "|".join(lista_skupina)
                    programi_string = "|".join(lista_programa)
                    with sqlite3.connect("DjecjiVrtic.db", timeout=10) as conn:
                        naredbe = conn.cursor()

                        try:
                            naredbe.execute(
                                        f"INSERT INTO kindergarten(name, city, address, capacity, \"group\", programs) "
                                        f"VALUES('{naziv}', '{mjesto}', '{adresa}', {int(kapacitet)}, "
                                        f"'{grupe_string}', '{programi_string}')"
                                    )
                        except sqlite3.IntegrityError as e:
                                    # HVATAMO UNIQUE CONSTRAINT exception
                                    self.porukaProzor("Vec postoji vrtic s istim nazivom ili istom adresom")
                        self.porukaProzor(f"Vrtic {noviVrtic.naziv} uspješno uneseno!!",
                                          QMessageBox.Information)
                        self.obrisi()
                except Exception as exc:
                    self.porukaProzor(str(exc))
            else:
                self.porukaProzor("Već postoji naziv, pokušajte unijeti drugi naziv za Vrtic")


        except Exception as exc:
            self.porukaProzor(str(exc))

    def obrisi(self):
        self.unos_vrtici.findChild(QLineEdit, "nazivVrticaText").clear()
        self.unos_vrtici.findChild(QLineEdit, "adresaVrticaText").clear()
        self.unos_vrtici.findChild(QLineEdit, "mjestoVrticaText").clear()
        self.unos_vrtici.findChild(QLineEdit, "kapacitetVrticaText").clear()
        self.unos_vrtici.findChild(QTextEdit, "programiEdit").clear()
        self.unos_vrtici.findChild(QTextEdit, "skupineEdit").clear()
