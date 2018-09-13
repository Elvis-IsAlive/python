#! /usr/bin/python3

"""main file"""

from maschinen import Schlepper, Anbaugeraet, Aufnahme
from felder import Feld

if __name__ == "__main__":

    s = Schlepper("Fendt Favorit 309", 40, 10)
    ab = Anbaugeraet("Egge", 3, 12)
    g = Anbaugeraet("Gewicht")
    s.anbauen(ab, Aufnahme.HECK)
    s.anbauen(g, Aufnahme.FRONT)


    print("Arbeitsbreite Schlepper " + s.name + ": " + str(s.breite()))
    print("Arbeitsbreite Gespann " + s.name + " und " + s.anbau_heck.name + ": " + str(s.breite()))
    print("Status von " + s.name + ": " + s.status)
    print("Der Wendekreis von " + s.name + " betraegt " + str(s.wendekreis) + "m")

    f = Feld("Oberer Acker", "100m", "100m")

    print(f.bezeichnung)
    print("l: " + str(f.laenge) + f.einheit)
    print("b: " + str(f.breite) + f.einheit)
    print("Das Feld " + f.bezeichnung + " ist " + str(f.flaeche) + str(f.einheit_flaeche) + " groß")
