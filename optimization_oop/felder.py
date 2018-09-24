#! usr/bin/python3

"""Provides field objects"""

import re


Einheiten = {"m": 1, "km": 1000}


class Feld():
    _counter = 0

    def __init__(self, bez, l, b):

        def _standardieisereAufMeter(arg):
            regEx_Value = re.compile("\d+")
            regEx_Unity = re.compile("[a-zA-Z]+")

            value = float(regEx_Value.search(arg).group())
            unity = str(regEx_Unity.search(arg).group())

            if unity == "m":
                pass
            elif unity == "km":
                unity *= Einheiten["m"]
            else:
                print("Zulässige Einheiten: m, km")
            return value


        Feld._counter += 1
        self._bezeichnung = bez

        self._laenge = _standardieisereAufMeter(l)
        self._breite = _standardieisereAufMeter(b)
        self._standardEinheit = "m"

    @property
    def laenge(self):
        return self._laenge

    @property
    def breite(self):
        return self._breite

    @property
    def bezeichnung(self):
        return self._bezeichnung

    @property
    def laenge(self):
        return self._laenge

    @property
    def breite(self):
        return self._breite

    # @property
    def flaeche(self, arg = "qm"):
        if arg == "qm":
            return self._laenge * self._breite
        elif arg == "qkm":
            return self._laenge/1000 * self._breite/1000
        elif arg == "ha":
            return self._laenge/100 * self._breite/100
        else:
            print("Zulässige Einheiten: qm, ha, qkm")


    @property
    def standardEinheit(self):
            return self._standardEinheit
