#! /usr/bin/python3.7

import os, shutil, re

# define regex for date
# ?P<name> definiert einen Gruppennahmen
regEx = re.compile(r"""(?P<month>\d{1,2}) # month
                    ([-/]) # sep
                    (?P<day>\d{1,2})   # day
                    ([-/])  # sep
                    (?P<year>\d{2,4})""", re.VERBOSE)       # MM-DD-YYYY mit
# variablen Trennzeichen "-" oder "/"



# loop over files in dir
os.chdir("/home/christoph/Documents/python/datefiles")

for f in os.listdir():
    res = regEx.search(f)
    if res:
        new_file_name = str(res.group("day") + "." + res.group("month") + "." + res.group("year"))
        shutil.move(f, new_file_name)
        print("Renamed file " + f + " to " + new_file_name)
