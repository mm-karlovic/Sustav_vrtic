import sqlite3

from Dijete import Dijete


class Vrtic:
    def __init__(self, naziv: str, grad: str, adresa: str, kapacitet: int):
        self.naziv = naziv
        self.grad = grad
        self.adresa = adresa
        self.kapacitet = kapacitet
        self.dijete = []


