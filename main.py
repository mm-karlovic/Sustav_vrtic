from GlavniProzor import GlavniProzor
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    window = GlavniProzor()
    window.show()
    app.exec_()