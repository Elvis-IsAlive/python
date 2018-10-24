#! /usr/bin/python3.6

""" Öffnet alle Links von Firmen in Mittelfranken auf automation-valley.de  """

from selenium import webdriver
import os, sys


def checkForQuit(index, index_datei, msg="press q to quit or enter to go to continue"):
    if len(msg) > 0:
        print(msg)

    command = str(input()).lower()
    if command == "q":
        # speichere Index in datei
        with open(index_datei, "w") as f:
            f.write(str(index + 1))
        browser.quit()      # webdriver beenden
        quit()              # Skript beenden
    else:
        return command

def checkForNav(index, index_datei, msg="press q to quit, n to go to next company or enter to continue"):
    if len(msg) > 0:
        print(msg)
    command = checkForQuit(index, index_datei, "")
    if command == "n":        # nächstes Unternehmensseite auf automation-valley
        return 1
    elif command == "":         # Homeage des Unternehmens aufrufen
        return 0




url_av = "http://www.automation-valley.de/firmenprofile-teilnehmer/"
index_datei = "automationValley_index.txt"




# Index aus datei
try:
    with open(index_datei, "r") as f:
        index = int(f.read())       # schmeißt ValueError wenn kein Int gefunden wird
        print("Index : %i" % index)
except Exception as e:
    print("No index found. Setting index to 0")
    index = 0


browser = webdriver.Firefox()
browser.get(url_av)

liste = browser.find_element_by_id("lcp_instance_0")      # liste von Unternehmen
unternehmen = liste.find_elements_by_tag_name("li")


print("reading list %s..." % url_av)

links_subpage = []
for i in range(len(unternehmen)):
    link = unternehmen[i].find_element_by_tag_name("a").get_attribute("href")
    links_subpage.append(link)      # attribut href in a-tag



for i in range(index, len(links_subpage)):

    print("opening automation-valley.de page...")
    browser.get(links_subpage[i])       # Unternehmensseite auf automation-valley.de

    status = checkForNav(i, index_datei)
    if status == 1:         #  Untenehmens-Homepage überspringen und nächstes Unternehmen aufrufen
        index += 1
        # print("continuing with next company...")
        continue

    # Unternehmensseite
    url = browser.find_element_by_class_name("entry-content").find_element_by_tag_name("a").get_attribute("href")
    print("opening %s ..." %url)
    browser.get(url)
    checkForQuit(index, index_datei)
