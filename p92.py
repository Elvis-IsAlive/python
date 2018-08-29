name =  ""

while True:
    print("Who are you?")
    name = input()

    if name == "Joe":
        print("Please enter your password, Joe")
        while True:
            pwd = input()
            if pwd == "JoesPassword":
                break
            print("wrong password, Joe. Try again")

        print("Login successfull")
        print("Hi, Joe, whats up?")
        break

    
        

    
