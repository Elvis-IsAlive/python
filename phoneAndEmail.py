#! /usr/bin/python3.7
'''finds phone numbers and email adresses from the clipboard'''

import pyperclip, re


#Beispiel-Nummber:  09185-234333-234
phoneRegex = re.compile(r'''(
    (\d{4,5}|\(\d{4,5}\))   #Vorwahl evtl. in Kalmmern
    (\d?[-/]\\d?)      #Trennzeichen
    (\d{3,10})  #Nummer
    (\d?[-/]\\d?)      #Trennzeichen
    (\d{1,4})?          #Durchwahl
)''')



#TODO: create email phoneRegex

#TODO: find matches in clipboard text

#TODO: copy results to clipboard
