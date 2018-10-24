#! /usr/bin/python3.7

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol needs to be a one char string")
    if not isinstance(width, int) or width <= 2:
        raise Exception("width must be an int greater than 2")
    if not isinstance(height, int) or height <= 2:
        raise Exception("height must be greater than 2")
    print(symbol * width)
    for i in range(height -2):
        print(symbol + " " * (width -2) + symbol)
    print(symbol * width)

for sym, w, h in (("#", 20, 6), ("x", 10, 10), ("*", 20, 10), ("D", 5, 5)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("An exceptin as occurred: " + str(err))
    
