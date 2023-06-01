from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Dijete import Dijete

from Vrtic import Vrtic
import sqlite3


class PregledDjece(QWidget):
    def __init__(self, pregled_widget):
        super().__init__()
        self.pregled_widget = pregled_widget

        djeca = None
        with sqlite3.connect("DjecjiVrtic.db") as conn:
            sucelje = conn.cursor()
            djeca = sucelje.execute("SELECT * FROM child;").fetchall()


        trenutniRedak = 0
        self.pregled_widget.findChild(QTableWidget, "tableWidget").setRowCount(len(djeca))
        self.pregled_widget.findChild(QTableWidget, "tableWidget").setColumnCount(len(djeca[0])-1)


        for dijete in djeca:
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,0,QTableWidgetItem(str(dijete[1])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,1,QTableWidgetItem(str(dijete[2])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,2,QTableWidgetItem(str(dijete[3])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,3,QTableWidgetItem(str(dijete[4])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,4,QTableWidgetItem(str(dijete[5])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,5,QTableWidgetItem(str(dijete[6])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,6,QTableWidgetItem(str(dijete[7])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,7,QTableWidgetItem(str(dijete[8])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,8,QTableWidgetItem(str(dijete[9])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,9,QTableWidgetItem(str(dijete[10])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,10,QTableWidgetItem(str(dijete[11])))
            self.pregled_widget.findChild(QTableWidget, "tableWidget").setItem(trenutniRedak,11,QTableWidgetItem(str(dijete[12])))
            trenutniRedak+=1





      