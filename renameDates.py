#! /usr/bin/python3.7

import os, shutil, re


# ^(.*?)     # beliebiger Text vor Datum
# (.*?)$


# define regex for date
# ?P<name> definiert einen Gruppennahmen
regEx = re.compile(r"""
                    (?P<month>(0|1)?\d) # month
                    ([-/]) # sep
                    (?P<day>(0|1|2|3)?\d)   # day
                    ([-/])  # sep
                    (?P<year>(19|20)?\d\d) # year
                    """, re.VERBOSE)       # MM-DD-YYYY mit
# variablen Trennzeichen "-" oder "/"



# loop over files in dir
os.chdir("/home/christoph/Documents/python/datefiles")

for f in os.listdir():
    res = regEx.search(f)
    if res:
        # vierstellige Jahreszahl
        if len(res.group("year")) == 2:
            year = str(20) + res.group("year")
        else:
            year = res.group("year")

        new_file_name = str(res.group("day") + "." + res.group("month") + "." + year)
        shutil.move(f, new_file_name)
        print("Renamed file %s to %s" %( f, new_file_name))
