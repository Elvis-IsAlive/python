#! /usr/bin/python3

tableData = [["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"]]


def printTable(table):
    line = ""
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(findMaxWidth(table[j]) + 4, " "), end = "")
        print("")


def findMaxWidth(col):
    max = 0
    for i in range(len(col)):
        if len(col[i]) > max:
            max = len(col[i])

    return max


printTable(tableData)
