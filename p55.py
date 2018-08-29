name = ""


while name != "exit":

    print("whats your name?")
    name = input()

    if name == "exit":
        exit
    else:
        print("hi " + name + ", nice to have you here!")

        print("the length of your name is " + str(len(name)) + " characters long.")
        print("------------------------------------------------------------------")

