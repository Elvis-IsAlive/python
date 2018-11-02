
print#! /bin/python3.6


class Gefaess():
    counter = 0

    def __init__(self, bezeichnung):
        self.bezeichnung  = str(bezeichnung)
        Gefaess.counter += 1
        self.id = Gefaess.counter


    def __str__(self):
        # return ", ".join(["Bezeichnung: " + self.bezeichnung, "ID: " + __str__(self.id)])
        s = ""
        for k, v in self.__dict__.items():
            s += ": ".join([k, str(v)]) + "\n"
        return s


    def fuellen(self, delta):
        if self.kapazitaet == self.fuellstand:
            print("Keine freie Kapazitaet")
        elif delta <= 0 or delta > (self.kapazitaet - self.fuellstand):
            print("Argument muss größer 0 und kleiner gleich der freien Kapazitaet %1.2f sein. Ist: %1.2f" % (self.kapazitaet - self.fuellstand, delta))
        else:
            self.fuellstand += float(delta)
            return delta


    def leeren(self, delta):
        if delta <= 0 or delta > self.fuellstand:
            print("Argument muss größer 0 und kleiner gleich dem Fuellstand von %1.2f sein. Ist: %1.2f" % (self.fuellstand, delta))
        else:
            self.fuellstand -= float(delta)
            return delta


    def print_kapazitaeten(self):
        s = self.bezeichnung + " ID: " + str(self.id)
        for k, v in self.__dict__.items():
            if "kapa" in k:
                s += ", " + ": ".join([k, str(v)])
        print(s)

    def print_fuellstaende(self):
        s = self.bezeichnung + " ID: " + str(self.id)
        for k, v in self.__dict__.items():
            if "fuellstand" in k:
                s += ", " + ": ".join([k, str(v)])
        print(s)





class Tasse(Gefaess):
    # Volumina in ml
    einheit = "ml"
    counter = 0

    def __init__(self, kapazitaet, fuellstand = 0):
        Tasse.counter += 1
        super().__init__("Tasse")
        self.id = Tasse.counter

        for e in [kapazitaet, fuellstand]:
            if e < 0:
                raise ValueError("Argument muss größer gleich 0 sein. Ist: %1.2f" % e)

        self.kapazitaet = float(kapazitaet)
        self.fuellstand = float(fuellstand)








class Kaffeemaschine(Gefaess):
    # Volumina in ml
    ppk_g_pro_ml =  200 / 1000  # g Pulver pro ml Kaffee: Schätzung 200g / l
    wpk_ml_pro_ml = 1.05        # ml Wasser pro ml Kaffee
    counter = 0

    def __init__(self, kapazitaet_kaffee, kapazitaet_wasser, kapazitaet_pulver, fuellstand_kaffee = 0, fuellstand_wasser = 0, fuellstand_pulver = 0):
        Kaffeemaschine.counter += 1
        super().__init__("Kaffeemaschine")
        self.id = Kaffeemaschine.counter
        for e in [kapazitaet_kaffee, kapazitaet_pulver, kapazitaet_wasser, fuellstand_kaffee, fuellstand_pulver, fuellstand_wasser]:
            if e < 0:
                raise ValueError("Argumente müssen größer gleich 0 sein")

        self.kapa_wasser = float(kapazitaet_wasser)
        self.fuellstand_wasser = float(fuellstand_wasser)
        self.kapa_pulver = float(kapazitaet_pulver)
        self.fuellstand_pulver = float(fuellstand_pulver)
        self.kapa_kaffee = float(kapazitaet_kaffee)
        self.fuellstand_kaffee = float(fuellstand_kaffee)


    def fuellen_pulver(self, delta):
        if self.kapa_pulver == self.fuellstand_pulver:
            print("Keine freie Kapazitaet")
        elif delta <= 0 or delta > (self.kapa_pulver - self.fuellstand_pulver):
            print("Argument muss größer 0 und kleiner gleich der freien Kapazitaet %1.2f sein. Ist: %1.2f" % (self.kapazitaet - self.fuellstand, delta))
        else:
            self.fuellstand_pulver += float(delta)
            return float(delta)

    def fuellen_wasser(self, delta):
        if self.kapa_wasser == self.fuellstand_wasser:
            print("Keine freie kapazitaet")
        elif delta <= 0 or delta > (self.kapa_wasser - self.fuellstand_wasser):
            print("Argument muss größer 0 und kleiner gleich der freien Kapazitaet %1.2f sein. Ist: %1.2f" % (self.kapa_wasser - self.fuellstand_wasser, delta))
        else:
            self.fuellstand_wasser += float(delta)
            return float(delta)


    def fuellen(self, delta_wasser, delta_pulver):
        self.fuellen_pulver(delta_pulver)
        self.fuellen_wasser(delta_wasser)


    def bruehen(self):
        # timer 3 sekunden
        delta_kaffee = self.fuellstand_wasser / Kaffeemaschine.wpk_ml_pro_ml     # geringfügige Volumenverluste
        delta_pulver = delta_kaffee * Kaffeemaschine.ppk_g_pro_ml                # Pulverbedarf

        if self.fuellstand_wasser <= 0:
            print("Wassertank ist leer")
        elif self.fuellstand_pulver < delta_pulver:
            print("Pulver-Fuellstand von %1.2f nicht ausreichend. Notwendig: %1.2f" % (self.fuellstand_pulver, delta_pulver))
        elif (self.kapa_kaffee - self.fuellstand_kaffee) < delta_kaffee:
            print("Die freie Kaffee-Kapazitaet von %1.2f ist nicht ausreichend um %1.2f neuen Kaffeee zu bruehen" % (self.kapa_kaffee - self.fuellstand_kaffee, delta_kaffee))
        else:
            self.fuellstand_kaffee += delta_kaffee
            self.fuellstand_wasser = 0          # wird vollständig aufgebraucht (Filterkaffeemaschine)
            self.fuellstand_pulver -= delta_pulver
            return float(delta_kaffee)

    def entnehmen_kaffee(self, delta):
        if self.fuellstand_kaffee < delta:
            print("Fuellstand von %1.2f zu gering. Zuerst neuen Kaffee bruehen" % self.fuellstand_kaffee)
        else:
            self.fuellstand_kaffee -= float(delta)
            return float(delta)


kaffee = 1000       # ml
k_opt = Kaffeemaschine(kaffee, Kaffeemaschine.wpk_ml_pro_ml * kaffee, Kaffeemaschine.ppk_g_pro_ml * kaffee)
k_opt.fuellen(k_opt.kapa_wasser, k_opt.kapa_pulver)
k_opt.bruehen()

t = Tasse(200)
t.fuellen(k_opt.entnehmen_kaffee(200))

print(t)
print(k_opt)
