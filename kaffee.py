#! /bin/python3.6


class Gegenstand():
    counter = 0
    
    def __init__(self, bezeichnung):
        self.bezeichnung  = str(bezeichnung)    
        Gegenstand.counter += 1
        self.id = Gegenstand.counter
        

    def __str__(self):
        # return ", ".join(["Bezeichnung: " + self.bezeichnung, "ID: " + __str__(self.id)])
        s = ""
        for k, v in self.__dict__.items():
            s += ": ".join([k, str(v)]) + "\n"
        return s

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


class Tasse(Gegenstand):
    # Volumina in ml
    einheit = "ml"
    counter = 0
    
    def __init__(self, kapazitaet, fuellstand = 0):
        Tasse.counter += 1
        super().__init__("Tasse")
        self.id = Tasse.counter
        self.kapazitaet = float(kapazitaet)     
        self.fuellstand = float(fuellstand)


    def befuellen(self, delta):
        if (self.kapazitaet - self.fuellstand) >= delta:
            self.fuellstand += float(delta)
            return True
        else:
            print("Fassungsvermoegen von %s ID: %d nicht ausreichend. Aktueller Fuellstand: %.2f %s" % (self.bezeichnung, self.id, self.fuellstand, Tasse.einheit))  
            return False
            

    def leeren(self, delta):
        if self.fuellstand >= float(delta):
            self.fuellstand -= float(delta)
            return True
        else:
            return False
            print("Der Fuellstand von %s ID: %d ist nicht ausreichend. Aktueller Fuellstand: %0.2f %s" % (self.bezeichnung, self.id, self.fuellstand, Tasse.einheit))


class Kaffeemaschine(Gegenstand):
    # Volumina in ml
    einheit = "ml"
    counter = 0

    def __init__(self, kapazitaet_kaffee, kapazitaet_wasser, kapazitaet_pulver, fuellstand_kaffee = 0, fuellstand_wasser = 0, fuellstand_pulver = 0):
        Kaffeemaschine.counter += 1
        super().__init__("Kaffeemaschine")
        self.id = Kaffeemaschine.counter
        self.kapa_wasser = float(kapazitaet_wasser)
        self.fuellstand_wasser = float(fuellstand_wasser)
        self.kapa_pulver = float(kapazitaet_pulver)
        self.fuellstand_pulver = float(fuellstand_pulver)
        self.kapa_kaffee = float(kapazitaet_kaffee)
        self.fuellstand_kaffee = float(fuellstand_kaffee)


    def befuellen_pulver(self, delta):
        if self.fuellstand_pulver + delta > self.kapa_pulver:
            print("Fassungsvermoegen von %s ID: %d nicht ausreichend. Aktueller Fuellstand: %0.2f %s" % (self.bezeichnung, self.id, self.fuellstand_pulver, Kaffeemaschine.einheit))
        else:
            self.fuellstand_pulver += delta

    def befuellen_wasser(self, delta):
        if self.fuellstand_wasser + delta > self.kapa_wasser:
            print("Fassungsvermoegen von %s ID: %d nicht ausreichend. Aktueller Fuellstand: %.2f %s" % (self.bezeichnung, self.id, self.fuellstand_wasser, Kaffeemaschine.einheit))
        else:
            self.fuellstand_wasser += delta

    def befuellen(self, delta_wasser, delta_pulver):
        self.befuellen_pulver(delta_pulver)
        self.befuellen_wasser(delta_wasser)

        
    def bruehen(self):
        # timer 3 sekunden
        if (self.kapa_kaffee - self.fuellstand_kaffee) < self.fuellstand_wasser:
            print("Die Kaffee-Kapazitaet von %s ID: %d ist nicht ausreichend um %0.00f %s neuen Kaffeee zu bruehen" % (self.bezeichnung, self.id, self.fuellstand_wasser, Kaffeemaschine.einheit))
        else:
            self.fuellstand_kaffee += self.fuellstand_wasser
            self.fuellstand_wasser = 0
            self.fuellstand_pulver = 0

    def entnehmen(self, tasse, delta_kaffee):
        if self.fuellstand_kaffee >= delta_kaffee:
            if tasse.befuellen(delta_kaffee):
                self.fuellstand_kaffee -= delta_kaffee
                return True
            else:
                return False
        else:
            print("Der Fuellstand von %s ID: %d ist nicht ausreichend. Aktueller Fuellstand: %0.2f %s" % (self.bezeichnung, self.id, self.fuellstand_kaffee, self.einheit))
            return False
                    


t1 = Tasse(200)
t2 = Tasse(150)
km = Kaffeemaschine(1000, 1000, 100)


km.befuellen(1000, 100)
km.print_fuellstaende()
km.bruehen()
km.print_fuellstaende()
t1.print_fuellstaende()
print("---")
km.entnehmen(t1, 200)
t1.leeren(200)
km.entnehmen(t1, 200)
t1.leeren(200)
km.entnehmen(t1, 200)
t1.leeren(200)
km.print_fuellstaende()
t1.print_fuellstaende()


print(" ---" )
km.entnehmen(t2, 150)
t2.print_fuellstaende()

km.entnehmen(t1, 200)
t1.leeren(200)

km.print_fuellstaende()
t1.print_fuellstaende()

km.entnehmen(t1, 100)



