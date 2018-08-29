#! /usr/bin/python3
"""List the content of a directory to the depth of -directory"""
import os
import sys
import argparse



def printDir(directory, depth, lvl = 0):
    """prints the directories and files of a directory"""
    os.chdir(directory)

    for e in  sorted(os.listdir()):
        #only non-hidden elements
        if not str(e).startswith("."):

            #files
            if os.path.isfile(e):
                if lvl > 1:
                    print("\t" * (lvl - 1) + "--> " + e)
                else:
                    print("--> " * lvl + e)

            #directories
            elif os.path.isdir(e):
                if lvl > 1:
                    print("\t" * (lvl -1) + "--> " + e)
                else:
                    print("--> " * lvl + e)
                if depth > 0:
                    printDir(e, depth - 1, lvl + 1)
                    os.chdir("..")



def printMessage():
    """Prints initial message including given arguments"""
    width = 90

    print()
    print("".center(width, "+"))
    info = " CONTENT OF " + directory + ", DEPTH: " + str(depth) + " "
    print(info.center(width, "+"))
    info = " ARGUMENTS GIVEN: " + str(sys.argv[1:]) + " "
    print(info.center(width, "+"))
    print("".center(width, "+"))
    print()



def pareseArguments():
    """Parses the command line arguments to assign global variables"""
    global directory, depth

    parser = argparse.ArgumentParser(description = "Show content of given directory down to specified depth")
    parser.add_argument("directory", type=str, help="defines the directory")
    parser.add_argument("-d", "--depth", type=int, default = 0, help="defines the depth")
    args = parser.parse_args()
    print(args)

    directory = args.directory
    depth = args.depth



if __name__ == "__main__":

    directory = ""
    depth = 0

    pareseArguments()
    printDir(directory, depth)
