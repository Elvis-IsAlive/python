


while True:
    print("please enter a name for which to check the birthday (enter to exit)")
    name = input()
    if name == "":
        break

    if name in b:
        print(name + "'s birthday is on " + b[name])
    else:
        print("No birthday for " + name + " saved")
        print("What is " + name + "'s birthday?")
        bday = input()
        b[name] = bday
        print("Database updated.")
