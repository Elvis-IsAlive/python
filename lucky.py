#! /usr/bin/python3.6

# lucky.py - opens several Google search results.

import sys, requests, webbrowser, bs4


# retrive google search results
print("Googling....")
res = requests.get("http://google.de/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# get links of top search results
soup = bs4.BeautifulSoup(res.text, features="html.parser")
links = soup.select(".r a")     # a element in class r 


# open browser tab for each link
for i in range(min(5, len(links))):
    webbrowser.open("http://google.de" + links[i].get("href"))
