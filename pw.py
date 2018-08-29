#! /usr/bin/python3.7

'''insecure password locker program'''


import sys
import pyperclip


PASSWORDS = {"email": "asdfjee33",
             "blog": "aofijdöoz554",
             "luggage": "1234§§"}




if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]   # first command line argument is account name, [0] = program name

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("There is no password for account " + account)
