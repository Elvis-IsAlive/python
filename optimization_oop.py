#! /usr/bin/python3.7

from enum import Enum


class Position(Enum):
    FRONT = 10
    HECK = 20
    BEIDE = 30
    


class Schlepper():

    def __init__(self, name, geschwindigkeit):
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

    @property
    def anbau_front(self):
        return self._anbau_front
    
    @property
    def status(self):
        return self._status.name

    @status.setter
    def status(self, val):
        self._status = val

    #Methode zum Anbauen eines Gerätes
    def anbauen(self, anbaugerät, position):
        if position == Position.HECK and not self._anbau_heck:
            self._anbau_heck = anbaugerät
        elif position == Position.FRONT and not self._anbau_front:
            self._anbau_front = anbaugerät
        else:
            print("Gerät kann nicht angebaut werden")

        if self._anbau_heck and self._anbau_front:
            self._staus = Position.BEIDE
        elif self._anbau_heck:
            self._status = Position.HECK
        elif self._anbau_front:
            self._status = Position.Front



    def abbauen(self, position):
        if position == Position.FRONT:
            self._anbau_front = None
        elif position == Position.HECK:
            self.anbau_front = None
        elif position == Position.BEIDE:
            self.anbau_front = None
            self.anbau_front = None


    def arbeitsbreite(self):
        if self._anbau_heck:
##            print("Arbeitsbreite Gespann mit " + self._name + " und " + self._anbau_heck.name + ": " + str(self._anbau_heck.arbeitsbreite) + "m")
            return self._anbau_heck.arbeitsbreite
        else:
##            print("Kein Anbaugerät angebaut an " + self._name)
            return None


    def arbeitsgeschwindigkeit(self):
        if self._anbau_heck or self._anbau_front:
            if self._anbau_heck and self._anbau_front:
                return min(self._geschwindigkeit, self._anbau_front.arbeitsgeschwindigkeit, self._anbau_heck.arbeitsgeschwindigkeit)
            elif self._anbau_heck:
                return min(self._geschwindigkeit, self._anbau_heck.arbeitsgeschwindigkeit)
            elif self._anbau_front:
                return min (self._geschwindigkeit, self._anbau_front.arbeitsgeschwindigkeit)
        else:
            return self._geschwindigkeit
    


    
class Anbaugerät():

    def __init__(self, name, ab, geschw):
        self._name = name
        self._arbeitsbreite = float(ab)
        self._arbeitsgeschwindigkeit = float(geschw)

    @property
    def arbeitsbreite(self):
##        print("Arbeitsbreite von " + self._name + ": " + str(self._arbeitsbreite) + "m")
        return self._arbeitsbreite

    @property
    def arbeitsgeschwindigkeit(self):
##        print("Arbeitsgeschwindigkeit von " + self._name + ": " + str(self._arbeitsgeschwindigkeit) + "km/h")
        return self._arbeitsgeschwindigkeit

    @property
    def name(self):
        return self._name



s = Schlepper("Fendt Favorit 309", 40)
ab = Anbaugerät("Egge", 3, 12)



print("Arbeitsbreite Schlepper " + s.name + ": " + str(s.arbeitsbreite()))
s.anbauen(ab, Position.HECK)
print("Arbeitsbreite Gespann " + s.name + " und " + s.anbau_heck.name + ": " + str(s.arbeitsbreite()))
print("Arbeitsgeschwindigkeit Gespann: " + str(s.arbeitsgeschwindigkeit()))

