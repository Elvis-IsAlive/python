    #! /usr/bin/python3.7
'''finds phone numbers and email adresses from the clipboard'''

import pyperclip, re


#Beispiel-Nummber:  09185-234333-234
phoneRegex = re.compile(r'''(
    (\(?\d{4,5}\)?)   #Vorwahl evtl. in Kalmmern
    (\s?[-/]?\s?)?	#Trennzeichen
    (\d{3,10})  #Nummer
    (\s?[-/]?\s?)?	#Trennzeichen
    (\d+)?    #Durchwahl
)''', re.VERBOSE)



emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    #username
    @    #@
    [a-zA-Z0-9.-]+    #domain
    [.]
    [.a-zA-Z0-9]{2,4}    #end
)''', re.VERBOSE)





text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    if not groups[5]:
        phoneNum = '-'.join([groups[1], groups[3]])
    else:
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups)



#print(matches)
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("contact information copied to clipboard:")
    print("\n".join(matches))
else:
    print("no contact information found")


# adsfasdf@web.de
# afiojdjiofafjdsioa-adf@dd.eu
# 1234-12341234
# 123412341234
# 1243-12341234-243
