grid = [[".",".",".",".",".","."],
        [".","o","o",".",".","."],
        ["o","o","o","o",".","."],
        ["o","o","o","o","o","."],
        [".","o","o","o","o","o"],
        ["o","o","o","o","o","."],
        ["o","o","o","o",".","."],
        [".","o","o",".",".","."],
        [".",".",".",".",".","."]]


def transpose(grid):
    for i in range(len(grid[0])):   #spalten des grid
        for j in range(len(grid)):  #zeilen des grid
            print(grid[j][i], end = "")
        print("")   #spaltenwechsel


transpose(grid)
