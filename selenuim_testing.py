#! usr/bin/python3.6

from selenium import webdriver as wb

b = wb.Firefox()

b.get("http://inventwithpython.com")
try:
    elem = b.find_element_by_link_text("#invent")
    print("Found <%s> element with that class name!" % (elem.tag_name))
except:
    print("Couldnt find any element with that name")
