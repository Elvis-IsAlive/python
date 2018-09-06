#! /usr/bin/python3.7

'''testing some flow control for pizza oven'''


from enum import Enum

class Oven():
    """A class for oven object"""

    def __init__(self):
        #stati
        self._on = False
        self._temp_reached = False
        self._door_open = False


    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, b):
        self._on = b


    @property
    def door_open(self):
        return self._door_open

    @door_open.setter
    def door_open(self, b):
        self._door_open = b


    @property
    def temp_reached(self):
        return self._temp_reached

    @temp_reached.setter
    def temp_reached(self, b):
        self._temp_reached = b




class States(Enum):
    INIT = 10
    PREHEAT = 20
    PROCESSING = 30
    COOLING = 40
    SHUTDOWN = 50





def semi_automatic(oven):

    upper_temp_lim = 250
    lower_temp_lim = 150
    eating_temp = 75
    ps = None


    
    while True:

        if ps == States.INIT:
            print("Power supply checked")
            oven.on = True
            print("Oven turned on")
            ps = States.PREHEAT


        if ps == States.PREHEAT:
            #get temperature from user
            while True:
                print("Please enter a temperature between " + str(lower_temp_lim) + " degrees Celcius and " + str(upper_temp_lim) + " degrees Celcius")
                temp = input()
                if temp.isnumeric():
                    temp = float(temp)
                    if temp <= upper_temp_lim and temp >= lower_temp_lim:
                        print("Preheating oven to " + str(temp) + " degrees Celcius")
                        # countdown for 3 seconds
                        oven.temp_reached = True
                        ps = States.PROCESSING
                        break


        if ps == States.PROCESSING:
            if oven.temp_reached:
                print("Processing pizza")
                # countdown
                print("Pizza is ready")
                ps = States.COOLING


        if ps == States.COOLING:
            oven.on = False
            print("Pizza is getting cooled to " + str(eating_temp) + " degrees Celcius eating temperature")

            #contdown
            oven.temp_reached = False

            if not oven.temp_reached:
                while True:
                    print("Please take your pizza out of the oven and confirm with \'y\' or \'yes\' ")
                    info = input()
                    if info == "y" or info == "yes":
                        info = ""
                        oven.door_open = False
                        print("Pizza taken out of the oven")
                        ps = States.SHUTDOWN
                        break


        if ps == States.SHUTDOWN:
            while True:
                print("Please close the door of the oven and confirm with \'y\' or \'yes\'")
                info = input()
                if info == "y" or info == "yes":
                    oven.door_open = False
                    print("Door closed")
                    break

            while True:
                print("Do you want another pizza (’p’) or turn off ('t') the oven?")
                info =  input()
                #check input
                if info == "p" or info == "t":
                    break

            if info == "t":
                print("Powering off oven")
                oven.on = False
                print("Shut down complete")
                break  #break main loopat
            else:
                ps = States.PREHEAT



        # if ps is not set yet
        else:
            print("Process status undefined. Set ps to init")
            ps = States.INIT


    print("PROCESS COMPLETED")






oven = Oven()

semi_automatic(oven)
