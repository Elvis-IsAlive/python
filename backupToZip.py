#! /usr/bin/python3.7

"""backupToZip.py - copies entire folder and its contents into a zip file
whos filename will be incremented"""

import zipfile, os

def backupToZip(folder):
    # backing up folder contents into zip
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip" 
        if not os.path.exists(zipFilename):
            break
        else:
            number += 1
    
    # create zipfile
    print("creating %s ..." % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # walk folder
    for f, subfolders, files in os.walk(folder):
        print("Adding files in %s..." % (f))
        backupZip.write(f)
        for file in files:
            newBase = os.path.basename(folder) + "_"
            if f.startswith(newBase) and f.endswith(".zip"): continue
            backupZip.write(os.path.join(f, file))
        backupZip.close()
        print("Done")

backupToZip("updateFiles")
