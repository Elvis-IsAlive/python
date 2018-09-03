board = {"tl": " ", "tm": " ", "tr" : " ",
         "ml": " ", "mm": " ", "mr" : " ",
         "ll": " ", "lm": " ", "lr" : " "}


def print_board(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])    
    print("-+-+-")
    print(board["ll"] + "|" + board["lm"] + "|" + board["lr"])



turn = "x"
for i in range(9):
    print("please make your turn, " + turn + ".")
    move = input()
    board[move] = turn
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
                                                        
    print_board(board)
