#! /usr/bin/python3.6

"""download comics from xkcy.com"""

import requests, bs4, os

# directory for images
os.makedirs("xkcd_download", exist_ok = True)   # exists_ok=true -> does not raise err if dir exists already

# open home page
url = "https://xkcd.com"


while not url.endswith("#"):

    # TODO: Download the page
    print("Downloading page %s..." % url)
    res = requests.get(url, timeout = 1)                # open url
    res.raise_for_status()                  # check for errors
    soup = bs4.BeautifulSoup(res.text, features="html.parser")      # parse html with bf4
    
    # find url of image
    comicElem = soup.select("#comic img")   # select img from div comic
                                            # returns list of matches
    if comicElem == []:                     
        print("Could not find comic image")
    else:
        comicUrl = comicElem[0].get('src')  # select src from first element
        #print(comicUrl)
        # download image
        print("Downloading image %s" % (comicUrl))
        res = requests.get("https:" + comicUrl)
        res.raise_for_status()

        # save file
        print("Saving file %s" % os.path.basename(comicUrl))
        
        imgFile = open(os.path.join("xkcd_download", os.path.basename(comicUrl)), "wb")
        for c in res.iter_content(100000):
            imgFile.write(c)
        imgFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]      # select <a> element which rel element is set to prev
    url = "http://xkcd.com" + prevLink.get("href")  # gets href of prevLink and creates new url

    

print("Done.")
