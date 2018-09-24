#! /usr/bin/python3.7



from enum import Enum
import math



def returnNotNone(args):
    return [val for val in args if val is not None]


class Aufnahme(Enum):
   FRONT = 10
   HECK = 20
   BEIDE = 30
   KEINE = 40



class Schlepper():
    anzahl = 0

    def __init__(self, name, geschwindigkeit, wendekreis):
        Schlepper.anzahl += 1
        self._wendekreis = wendekreis
        self._vorgewendelaenge = None
        self._name = name
        self._geschwindigkeit = geschwindigkeit
        self._anbau_heck = None
        self._anbau_front = None
        self._status = None
        self._wendestrecke = None


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

    # @status.setter
    # def status(self, val):
    #     self._status = val

    @property
    def wendekreis(self):
        return self._wendekreis

    @property
    def vorgewendelaenge(self):
        return self._vorgewendelaenge

    @property
    def wendestrecke(self):
        return self._wendestrecke



    #Methode zum Anbauen eines Geraetes
    def anbauen(self, anbaugeraet, Aufnahme):

        if Aufnahme == Aufnahme.HECK and not self._anbau_heck:
            self._anbau_heck = anbaugeraet
        elif Aufnahme == Aufnahme.FRONT and not self._anbau_front:
            self._anbau_front = anbaugeraet
        else:
            print("Geraet kann nicht angebaut werden")

        self._unpdate_status()
        self._update_vorgewende_laenge()
        self._update_wendestrecke()



    def abbauen(self, aufnahme):
        if aufnahme == Aufnahme.FRONT:
            self._anbau_front = None
        elif aufnahme == Aufnahme.HECK:
            self._anbau_heck = None
        elif aufnahme == Aufnahme.BEIDE:
            self._anbau_front = None
            self._anbau_heck = None

        self._unpdate_status()
        self._update_vorgewende_laenge()
        self._update_wendestrecke()


    def _unpdate_status(self):
        if self._anbau_heck and self._anbau_front:
            self._status = Aufnahme.BEIDE
        elif self._anbau_heck:
            self._status = Aufnahme.HECK
        elif self._anbau_front:
            self._status = Aufnahme.FRONT
        else:
            self._status = Aufnahme.KEINE


    def _update_vorgewende_laenge(self):

        anbaugeraete = returnNotNone([self.anbau_heck, self.anbau_front])

        arbeitsbreiten = []
        for x in anbaugeraete:
            if x.breite:
                arbeitsbreiten.append(x.breite / 2) # Wenderadius
        arbeitsbreiten.append(self._wendekreis / 2)
        radius = max(arbeitsbreiten)

        self._vorgewendelaenge = math.ceil(radius * (2 + math.sin(math.pi/4))) #Annahme: pi/4 vor + ph/8 zurück + pi/8 vor
        # Berücksichtiugn sin, da sonst Anbaugerät ragt um sinus über Feld hinausragt


    def _update_wendestrecke(self):
        # max radius ermittel
        anbaugeraete = returnNotNone([self.anbau_heck, self.anbau_front])

        arbeitsbreiten = []
        for x in anbaugeraete:
            if x.breite:
                arbeitsbreiten.append(x.breite / 2) # Wenderadius
        arbeitsbreiten.append(self._wendekreis / 2)
        r = max(arbeitsbreiten)

        # Strecke ~ r*pi/4 + achsstand anbaugerät vorwärts + pi/8*r rückwärts + pi/8*r vorwärts
        # bei Rückwährtsfahrt zusätzlicher Platz für Anbaugerät notwendig?
        self._wendestrecke = math.ceil(math.pi / 2 * r + self.anbau_heck.radstand)




    def gesamtstreckeInKm(self, f):
        b = min(f.breite, f.laenge)   # Feld-Breite
        l = max(f.breite, f.laenge)   # Feld-Länge

        anz_spuren =  math.ceil(b / self._wendekreis)
        anz_wenden = anz_spuren - 1

        strecke_wenden = self._wendestrecke
        strecke_spur = l - self._vorgewendelaenge
        strecke_spur_vorgewende = b   # lange Seite des Vorgewendes entspricht Feldbreite

        # vorgewende
        anz_spuren_vorgew = self._vorgewendelaenge / self._wendekreis
        anz_wenden_vorgew = anz_spuren_vorgew - 1

        # Rückfahrt bei ungerader Spur-anzahl in Längsrichtung
        if anz_spuren % 2 != 0:
            anz_spuren += 1 # Zusatzfahrt zu rück zu Vorgewende
            #anz_wenden += 1 # zwei 90° Drehungen = eine Wendung >>> VERNACHLÄSSIGT
        else:
            pass
            #anz_spuren += 1 # lässt sich vor Vorgewendebearbeitung realisieren
            #  Drehungen >>> VERNACHLÄSSGIT


        if anz_spuren_vorgew % 2 != 0:
            anz_spuren_vorgew += 1  #einfache Fahrt notwendig
        else:
            pass
            # anz_spuren_vorgew += 1  #Breite des Feldes
        #     # Annahme: Vorgewendewechsel auf beiden Seiten möglich, ansonsten anz_spuren_vorgew +2


        return math.ceil((strecke_spur * anz_spuren + strecke_wenden * anz_wenden +\
            strecke_spur_vorgewende * anz_spuren_vorgew + anz_wenden_vorgew * strecke_wenden)) / 1000






    @property
    def breite(self):
        if self._status == Aufnahme.BEIDE:
            l = []
            for x in returnNotNone([self.anbau_heck, self.anbau_front]):
                if x.breite:
                    l.append(x.breite)
            return min(l)

        elif self._status == Aufnahme.FRONT:
            return self._anbau_front.breite
        else:
            return self._anbau_heck.breite


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


    def __init__(self, name, breite = None, radstand = None, geschw = None):
        Anbaugeraet.anzahl += 1
        self._name = name
        try:
            self._breite = float(breite)
            self._geschwindigkeit = float(geschw)
            self._radstand = radstand
        except(TypeError):
            self._breite = None
            self._geschwindigkeit = None
            self._radstand = radstand


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

    @property
    def radstand(self):
        return self._radstand
