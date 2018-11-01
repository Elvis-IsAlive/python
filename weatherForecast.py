#! /usr/bin/python3.6

"""Wettervorhersage in Textform"""

import json, requests, sys



# location from commandline input

if len(sys.argv) < 2:
    print("enter location as command line argument")
    sys.exit()
else:
    loc = " ".join(sys.argv[1:])


# daily : api.openweathermap.org/data/2.5/weather?q=London
# 3 days forecast: api.openweathermap.org/data/2.5/forecast?q={city name},{country code} 
url = "http://api.openweathermap.org/data/2.5/weather?q=%s" % loc
res = requests.get(url)
res.raise_for_status()

data = json.load(res.text)
w = data["list"]
desc = w[0]["weather"][0]["description"]
