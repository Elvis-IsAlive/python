#! /usr/bin/python3.6

'''brute force pdf password '''


import PyPDF2, sys


filename = sys.argv[1]

print("bruteforcing pdf %s..." % filename)

reader = PyPDF2.PdfFileReader(filename, "r")

msg = "password cracked: "

with open("dictionary.txt", "r") as f:
    for line in f.readlines():
        word = line.strip()
        cap = word.capitalize()
        lower = word.lower()
        upper = word.upper()

        print("trying %s / %s / %s" %(cap, lower, upper))

        if reader.decrypt(cap) > 0:
            print(msg + cap)
            break
        elif reader.decrypt(lower) > 0:
            print(msg + lower)
            break
        elif reader.decrypt(upper) > 0:
            print(msg + upper)
            break

print("done.")
