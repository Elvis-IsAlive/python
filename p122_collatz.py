def collatz(number):
    if number%2 == 0:
        #even
        print(number // 2)
        return number // 2
    else:
        print(number*3+1)
        return number*3+1



while True:
    print("type int")
    try:
        num = input()

        #check string for exit
        if num == "exit":
            break

        #convert to int
        else:
            num = int(num)

        while num != 1:
            num = collatz(num)

    #any other string than "exit" evaluates to ValueError
    except ValueError:
        print("value is not an integer")

    

