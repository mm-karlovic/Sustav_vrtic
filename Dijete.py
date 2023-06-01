class Dijete:
    def __init__(self, ime: str, prezime: str, oib: int, dob: str, grad: str, drzavljanstvo: str, imeMajke: str,
                 imeOca: str, skupina: str, program: str, biljeska: str):
        self.__oib = oib
        if len(str(oib)) != 11:
            raise Exception("OIB treba imati 11 znamenki.")
        try:
            self.__oib = oib
        except:
            raise Exception("OIB se sastoji samo od znamenki.")
        self.ime = ime
        self.prezime = prezime
        self.dob = dob
        self.grad = grad
        self.drzavljanstvo = drzavljanstvo
        self.imeMajke = imeMajke
        self.imeOca = imeOca
        self.skupina = skupina
        self.program = program
        self.bijeska = biljeska

    def getOib(self):
        return self.__oib

    def setOib(self, oib):
        if len(str(oib)) != 11:
            raise ("OIB treba imati 11 znamenki.")
        try:
            self.__oib = oib
        except:
            raise ("OIB se sastoji samo od znamenki.")

    def __str__(self) -> str:
        return self.__oib + "\t" + self.ime + "\t" + self.prezime + "\t" + self.dob + "\t" + self.grad + "\t" + self.drzavljanstvo + "\t" + self.imeMajke + "\t" + self.imeOca + "\t" + self.skupina + "\t" + self.program + "\t" + self.biljeska

    def pripremiZaJson(self):
        return {"ime": self.ime, "prezime": self.prezime, "oib": self.__oib, "dob": self.dob, "grad": self.grad,
                "drzavljanstvo": self.drzavljanstvo, "imeMajke": self.imeMajke, "imeOca": self.imeOca,
                "program": self.program, "biljeska": self.biljeska}
        # TODO:treba li ovdje oib?