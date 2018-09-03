while True:

    spam = input()
    
    try:
        if spam == "exit":
            break
        elif int(spam) == 1:
            print("Hello")
        elif int(spam) == 2:
            print("Howdy")
        print("Greetings")
        
    except ValueError:
        print("Greetings")

