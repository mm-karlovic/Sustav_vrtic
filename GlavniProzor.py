import sys

from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow
from UnosDjeteta import UnosDjeteta
from PregledDjece import PregledDjece
from PretragaDjece import PretragaDjece
from UnosVrtici import UnosVrtici
from PregledVrtica import PregledVrtica
from PretragaVrtica import PretragaVrtica
from Vrtic import Vrtic



class GlavniProzor(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("Main.ui", self)

        self.setWindowTitle("Sustav Dječji Vrtić OL-OPYT_H-03/22")

        self.stackedWidget.setCurrentWidget(self.home)
        self.unosButton.clicked.connect(self.prikaziUnos)
        self.pregledButton.clicked.connect(self.prikaziPregled)
        self.pretragaButton.clicked.connect(self.prikaziPretraga)
        self.izlazButton.clicked.connect(self.close)
        self.vrticButton.clicked.connect(self.prikaziVrtic)
        self.pregledVrticaButton.clicked.connect(self.prikaziPregledVrtica)
        self.pretragaVrticaButton.clicked.connect(self.prikaziPretraguVrtica)

    def prikaziUnos(self):
        self.stackedWidget.setCurrentWidget(self.unos)
        self.setWindowTitle("Unos djeteta OL-OPYT_H-03/22")
        self.klasaUnosa = UnosDjeteta(self.unos)

    def prikaziPregled(self):
        self.stackedWidget.setCurrentWidget(self.pregled)
        self.setWindowTitle("Pregled upisane djece OL-OPYT_H-03/22")
        self.klasaPregled = PregledDjece(self.pregled)

    def prikaziPretraga(self):
        self.stackedWidget.setCurrentWidget(self.pretraga)
        self.setWindowTitle("Pretraga po djetetu OL-OPYT_H-03/22")
        self.klasaPretraga = PretragaDjece(self.pretraga)

    def prikaziVrtic(self):
        self.stackedWidget.setCurrentWidget(self.vrtici)
        self.setWindowTitle("Administracija Vrtića OL-OPYT_H-03/22")
        self.klasaVrtic = UnosVrtici(self.vrtici)

    def prikaziPregledVrtica(self):
        self.stackedWidget.setCurrentWidget(self.pregledVrtica)
        self.setWindowTitle("Pregled vrtića OL-OPYT_H-03/22")
        self.klasaPregledVrtica = PregledVrtica(self.pregledVrtica)

    def prikaziPretraguVrtica(self):
        self.stackedWidget.setCurrentWidget(self.pretragaVrtica)
        self.setWindowTitle("Pretraga vrtića OL-OPYT_H-03/22")
        self.klasaPretragaVrtica = PretragaVrtica(self.pretragaVrtica)





