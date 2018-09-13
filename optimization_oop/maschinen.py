#! /usr/bin/python3.7



from enum import Enum

class Aufnahme(Enum):
   FRONT = 10
   HECK = 20
   BEIDE = 30



class Schlepper():
    anzahl = 0

    def __init__(self, name, geschwindigkeit, wendekreis):
        Schlepper.anzahl += 1
        self._wendekreis = wendekreis
        self._name = name
        self._geschwindigkeit = geschwindigkeit
        self._anbau_heck = None
        self._anbau_front = None
        self._status = None


    @property
    def name(self):
        return self._name

    @property
    def anbau_heck(self):
        return self._anbau_heck

    @anbau_heck.setter
    def anbau_heck(self, val):
        self._anbau_heck = val

    @property
    def anbau_front(self):
        return self._anbau_front

    @property
    def status(self):
        return "Genutzte Anbaumoeglichkeiten: " + self._status.name

    @status.setter
    def status(self, val):
        self._status = val

    @property
    def wendekreis(self):
        return self._wendekreis



    #Methode zum Anbauen eines Geraetes
    def anbauen(self, anbaugeraet, Aufnahme):

        if Aufnahme == Aufnahme.HECK and not self._anbau_heck:
            self._anbau_heck = anbaugeraet
        elif Aufnahme == Aufnahme.FRONT and not self._anbau_front:
            self._anbau_front = anbaugeraet
        else:
            print("Geraet kann nicht angebaut werden")

        self.update_status()



    def abbauen(self, Aufnahme):
        if Aufnahme == Aufnahme.FRONT:
            self.anbau_front = None
        elif Aufnahme == Aufnahme.HECK:
            self.anbau_heck = None
        elif Aufnahme == Aufnahme.BEIDE:
            self.anbau_front = None
            self.anbau_heck = None

        self.update_status()



    def update_status(self):
        if self._anbau_heck and self._anbau_front:
            self.status = Aufnahme.BEIDE
        elif self.anbau_heck:
            self.status = Aufnahme.HECK
        elif self.anbau_front:
            self.status = Aufnahme.FRONT


    def breite(self):
        if self._anbau_heck:
            return self._anbau_heck.breite
        else:
            return None


    def geschwindigkeit(self):

        if self._anbau_heck or self._anbau_front:
            if self._anbau_heck and self._anbau_front:
                return min(self._geschwindigkeit, self._anbau_front.geschwindigkeit, self._anbau_heck.geschwindigkeit)
            elif self._anbau_heck:
                return min(self._geschwindigkeit, self._anbau_heck.geschwindigkeit)
            elif self._anbau_front:
                return min (self._geschwindigkeit, self._anbau_front.geschwindigkeit)
        else:
            return self._geschwindigkeit




class Anbaugeraet():

    anzahl = 0


    def __init__(self, name, breite = None, geschw = None):
        Anbaugeraet.anzahl += 1
        self._name = name
        try:
            self._breite = float(breite)
            self._geschwindigkeit = float(geschw)
        except(TypeError):
            self._breite = None
            self._geschwindigkeit = None


    @property
    def breite(self):
##        print("Arbeitsbreite von " + self._name + ": " + str(self._arbeitsbreite) + "m")
        return self._breite

    @property
    def geschwindigkeit(self):
##        print("Arbeitsgeschwindigkeit von " + self._name + ": " + str(self._arbeitsgeschwindigkeit) + "km/h")
        return self._geschwindigkeit

    @property
    def name(self):
        return self._name
