#! /usr/bin/python3.7

import re, argparse, sys


#command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("password", type=str, help="password to be checked")
args = parser.parse_args()

pw = args.password
strongPw = True

if len(pw) < 8:
    strongPw = False
    print("password is too short")


#regex for number and upper and lowercase letters
numRegex = re.compile(r"\d+")   #number
upCaseRegex = re.compile(r"[A-Z]+") #uppercase
loCaseRegex = re.compile(r"[a-z]+") #lowercase

if not numRegex.search(pw):
    print("no number included")
    strongPw = False

if not upCaseRegex.search(pw):
    print("no uppercase letter included")
    strongPw = False

if not loCaseRegex.search(pw):
    print("no lowercase letter included")
    strongPw = False


if not strongPw:
    print("password is not strong.")
else:
    print("password is strong enough")
