#! /usr/bin/python3.7


def printPicnic(itemsDict, leftWidth, rightWidth):
    print("Picnic Items".center(leftWidth + rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))


picnicItems = {"sandwiches": 4, "apples": 12, "cookies": 8000}

printPicnic(picnicItems, 20, 10)
