#! usr/bin/python3

"""Provides field objects"""

import re


class Feld():
    _counter = 0

    def __init__(self, bez, l, b):

        Feld._counter += 1

        regEx_Value = re.compile("\d+")
        regEx_Unity = re.compile("[a-zA-Z]+")
        self._laenge = float(regEx_Value.search(l).group())
        self._breite = float(regEx_Value.search(b).group())
        self._bezeichnung = bez

        unity_l = regEx_Unity.search(l).group()
        unity_b = regEx_Unity.search(b).group()
        if unity_b == unity_l:
            self._einheit = unity_b.lower()
        else:
            del self
            print("Laenge und Breite in gleicher Einheit angeben!")


    @property
    def bezeichnung(self):
        return self._bezeichnung

    @property
    def laenge(self):
        return self._laenge

    @property
    def breite(self):
        return self._breite

    @property
    def flaeche(self):
        return self._breite * self._laenge

    @property
    def einheit_flaeche(self):
        return "q" + self._einheit

    @property
    def einheit(self):
        return self._einheit
