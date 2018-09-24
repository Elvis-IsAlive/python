#! /usr/bin/python3

"""main file"""

from maschinen import Schlepper, Anbaugeraet, Aufnahme
from felder import Feld
import math

if __name__ == "__main__":

    s = Schlepper("Fendt Favorit 309", 40, 10)
    ab = Anbaugeraet("Egge", 15, 10, 12)
    g = Anbaugeraet("Gewicht")
    s.anbauen(ab, Aufnahme.HECK)
    s.anbauen(g, Aufnahme.FRONT)


    print("Arbeitsbreite Gespann " + s.name + " und " + s.anbau_heck.name + ": " + str(s.breite))
    print("Status von " + s.name + " " + s.status)
    print("Der Wendekreis von " + s.name + " betraegt " + str(s.wendekreis) + "m")

    f = Feld("Oberer Acker", "100m", "1000m")
    print("Das Feld \"" + f.bezeichnung + "\" ist " + str(f.flaeche("ha"))  + "ha groß")

    print("Mindestanzahl notwendiger Spuren bei einer Feldbreite von " + str(f.breite) + "m : " + str(math.ceil(min(f.laenge, f.breite)/s.breite)))
    print("Das Vorgewende bei einer Feldlänge von " + str(f.laenge) + " hat eine Mindestlänge von " + str(s.vorgewendelaenge) + "m")
    print("Wendestrecke beträgt: " + str(s.wendestrecke) + "m")
    print("Die Gesamtstrecke zur bearbeitung von \"" + f.bezeichnung + "\" beträgt " + \
            str(s.gesamtstreckeInKm(f)) + "km")
