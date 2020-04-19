counter = 0
turn = "o"
check = str
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# 0 1 2
# 3 4 5
# 6 7 8

def playing_board():
    print("|{}|{}|{}|\n"
          "|{}|{}|{}|\n"
          "|{}|{}|{}|".format(board[0], board[1], board[2],
                              board[3], board[4], board[5],
                              board[6], board[7], board[8]))


def replace(position, value):
    board.pop(position)
    board.insert(position, "{}".format(value))
    board.pop(position)
    board.insert(position, "{}".format(value))


def position_check():
    for c in range(0, 2, 1):
        if c == 0:
            check = "x"
        if c == 1:
            check = "o"

        if board[position_list[0]] == check:
            if board[position_list[1]] == check:
                if board[position_list[2]] == check:
                    print("you win")
                    exit()

def check_win():
    global position_list
    position_list = list()

    for b in range(0, 3, 1):
        ##check vertically
        for i in range(b, 9, 3):
            position_list.append(i)
        position_check()

        position_list = list()

        ##check horizontally
        for i in range(b, 9, 1):
            position_list.append(i)
        position_check()

        position_list = list()

        ##check diagonally
        for i in range(0, 12, 4):
            position_list.append(i)
        position_check()

        position_list = list()

        ##check diagonally 2
        for i in range(2, 8, 2):
            position_list.append(i)
        position_check()

        position_list = list()


while True:
    movement = input("Which position do you want to go: ")
    movement = int(movement)

    if board[movement] != " ":
        print("Pick another position")
    else:
        counter = counter + 1
        if counter > 1:
            counter = 0
        if counter == 0:
            turn = "x"
        if counter == 1:
            turn = "o"
        replace(movement, turn)

    check_win()
    print(playing_board())
