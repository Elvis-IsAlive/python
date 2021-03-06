#! /usr/bin/python3.7



from enum import Enum

class Position(Enum):
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
    def anbauen(self, anbaugeraet, position):

        if position == Position.HECK and not self._anbau_heck:
            self._anbau_heck = anbaugeraet
        elif position == Position.FRONT and not self._anbau_front:
            self._anbau_front = anbaugeraet
        else:
            print("Geraet kann nicht angebaut werden")

        self.update_status()



    def abbauen(self, position):
        if position == Position.FRONT:
            self.anbau_front = None
        elif position == Position.HECK:
            self.anbau_heck = None
        elif position == Position.BEIDE:
            self.anbau_front = None
            self.anbau_heck = None

        self.update_status()



    def update_status(self):
        if self._anbau_heck and self._anbau_front:
            self.status = Position.BEIDE
        elif self.anbau_heck:
            self.status = Position.HECK
        elif self.anbau_front:
            self.status = Position.FRONT


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




if __name__ == "__main__":

    s = Schlepper("Fendt Favorit 309", 40, 10)
    ab = Anbaugeraet("Egge", 3, 12)
    g = Anbaugeraet("Gewicht")
    s.anbauen(ab, Position.HECK)
    s.anbauen(g, Position.FRONT)


    print("Arbeitsbreite Schlepper " + s.name + ": " + str(s.breite()))
    print("Arbeitsbreite Gespann " + s.name + " und " + s.anbau_heck.name + ": " + str(s.breite()))
    print("Status von " + s.name + ": " + s.status)
    print("Der Wendekreis von " + s.name + " betraegt " + str(s.wendekreis) + "m")
