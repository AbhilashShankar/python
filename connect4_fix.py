board = list()
##7 by 6 board
for b in range(42):
    board.append(" ")

##print the board
def print_board():
    print("|{}|{}|{}|{}|{}|{}|{}|\n"
          "|{}|{}|{}|{}|{}|{}|{}|\n"
          "|{}|{}|{}|{}|{}|{}|{}|\n"
          "|{}|{}|{}|{}|{}|{}|{}|\n"
          "|{}|{}|{}|{}|{}|{}|{}|\n"
          "|{}|{}|{}|{}|{}|{}|{}|".format(board[0],  board[1],  board[2],  board[3],  board[4],  board[5],  board[6],
                                          board[7],  board[8],  board[9],  board[10], board[11], board[12], board[13],
                                          board[14], board[15], board[16], board[17], board[18], board[19], board[20],
                                          board[21], board[22], board[23], board[24], board[25], board[26], board[27],
                                          board[28], board[29], board[30], board[31], board[32], board[33], board[34],
                                          board[35], board[36], board[37], board[38], board[39], board[40], board[41]))

##use to check the answer
def checkRows(columnstart, columnend, rowstart,rowend, rowstep, rowcounter):
    for c in range(columnstart, columnend, 7):
        # check in the current row
        for i in range(rowstart + c, rowend + c, rowstep):
            if board[i] == checkplayer:
                if board[i + rowcounter] == checkplayer:
                    if board[i + (rowcounter*2)] == checkplayer:
                        if board[i + (rowcounter*3)] == checkplayer:
                            print_board()
                            print("{} wins".format(checkplayer))
                            exit()

def winCheck():
    #horizontally
    global checkplayer
    for b in range(0,2,1):
        if b == 0:
            checkplayer = "x"
        if b == 1:
            checkplayer = "o"
        #check horizontally
        checkRows(0, 40, 0, 4, 1, 1)
        #check diagonally
        checkRows(0, 21, 0, 4, 1, 8)
        checkRows(0, 21, 3, 6, 1, 6)
        #check vertically
        checkRows(0, 21, 0, 7, 1, 7)

step = -7
counter = 0
player = str
column_list = list()

def checkMovements():
    global start
    global stop
    global step
    global check
    for i in range(1, 8, 1):
        if column == i:
            start = 34 + i
            stop = -8 + i

    column_list = list()
    for i in range(start, stop, step):
        column_list.append(i)

    if board[column_list[5]] != " ":
        if board[column_list[4]] != " ":
            if board[column_list[3]] != " ":
                if board[column_list[2]] != " ":
                    if board[column_list[1]] != " ":
                        if board[column_list[0]] != " ":
                            check = 0
    else:
        check = 1

while True:
    print_board()

    ##two player counter
    counter = counter + 1
    if counter > 1:
        counter = 0
    if counter == 1:
        player = "x"
    if counter == 0:
        player = "o"

    ##ask user to choose a column to drop a piece
    column = int(input("Choose a column"))
    ##determine positioning for columns, then replace from the bottom up.
    checkMovements()

    while check == 0:
        column = int(input("This Column is full, pick another one: "))
        checkMovements()

    for i in range(start, stop, step):
        if board[i] == " ":
            board.pop(i)
            board.insert(i, "{}".format(player))
            break
    winCheck()