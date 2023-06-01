from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Dijete import Dijete

from Vrtic import Vrtic
import sqlite3


class PregledVrtica(QWidget):
    def __init__(self, pregledvrtica_widget):
        super().__init__()
        self.pregledvrtica_widget = pregledvrtica_widget

        vrtici = None
        with sqlite3.connect("DjecjiVrtic.db") as conn:
            sucelje = conn.cursor()
            vrtici = sucelje.execute("SELECT * FROM kindergarten;").fetchall()
            
        self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setRowCount(len(vrtici))
        self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setColumnCount(len(vrtici[0])-1)

        trenutniRedak = 0
        for vrtic in vrtici:
            self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setItem(trenutniRedak,0,QTableWidgetItem(str(vrtic[1])))
            self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setItem(trenutniRedak,1,QTableWidgetItem(str(vrtic[2])))
            self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setItem(trenutniRedak,2,QTableWidgetItem(str(vrtic[3])))
            self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setItem(trenutniRedak,3,QTableWidgetItem(str(vrtic[4])))
            self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setItem(trenutniRedak,4,QTableWidgetItem(str(vrtic[5])))
            self.pregledvrtica_widget.findChild(QTableWidget, "tableVrtic").setItem(trenutniRedak,5,QTableWidgetItem(str(vrtic[6])))
            trenutniRedak += 1
      