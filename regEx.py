#! /usr/bin/python3
import re   # regex module
import argparse


def getMobilNumber(num):
    regex = re.compile(r"[+]?\d{4,5}[-+]?\d{6,8}")   #
    res = regex.search(num)
    if res != None:
        return res.group()
    else:
        return "No mobile number found"



parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="String to check for number")
args = parser.parse_args()


print(getMobilNumber(args.input))
