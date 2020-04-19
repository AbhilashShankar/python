import random

def play_game():
    alternate = 0
    move_list = list()
    while True:
        move = input("Make your move: ")

        if move not in move_list:
            alternate = alternate + 1
            if alternate > 1:
                alternate = 0
        if move in move_list:
            print("You cant go there!")

        for i in range(9):
            if move not in move_list:
                if alternate == 1:
                    if i == move:
                        board.pop(i)
                        board.insert(i,"x")

                if alternate == 0:
                    if i == move:
                        board.pop(i)
                        board.insert(i, "o")

        move_list.append(move)

        print_board()

        #horizontal
        if board[0] == board[1] == board[2] == "x":
                print("X won")
                exit()
        if board[3] == board[4] == board[5] == "x":
                print("X won")
                exit()
        if board[6] == board[7] == board[8] == "x":
                print("X won")
                exit()

        if board[0] == board[1] == board[2] == "o":
                print("o won")
                exit()
        if board[3] == board[4] == board[5] == "o":
                print("o won")
                exit()
        if board[6] == board[7] == board[8] == "o":
                print("o won")
                exit()

        #vertical
        if board[0] == board[3] == board[6] == "o":
                print("o won")
                exit()
        if board[1] == board[4] == board[7] == "o":
                print("o won")
                exit()
        if board[2] == board[5] == board[8] == "o":
                print("o won")
                exit()

        if board[0] == board[3] == board[6] == "x":
                print("X won")
                exit()
        if board[1] == board[4] == board[7] == "x":
                print("X won")
                exit()
        if board[2] == board[5] == board[8] == "x":
                print("X won")
                exit()

        #diagonal
        if board[0] == board[4] == board[8] == "o":
                print("o won")
                exit()
        if board[2] == board[4] == board[6] == "o":
                print("o won")
                exit()
        if board[0] == board[4] == board[8] == "x":
                print("X won")
                exit()
        if board[2] == board[4] == board[6] == "x":
                print("X won")
                exit()




def play_computer():
    computer_move = 0
    alternate = 0
    move_list = list()

    while True:
        move = input("Make your move: ")

        if move not in move_list:
            alternate = alternate + 1
            if alternate > 1:
                alternate = 0
        if move in move_list:
            print("You cant go there!")

        for i in range(9):
            if move not in move_list:
                if alternate == 1:
                    if i == move:
                        board.pop(i)
                        board.insert(i,"x")
                        g = 1
                    else:
                        g = 0

                if alternate == 0:
                    if i == move:
                        board.pop(i)
                        board.insert(i, "o")
                        g = 1
                    else:
                        g = 0

        move_list.append(move)

        if g == 1:
            while True:
                computer_move = random.randint(1, 8)

                if computer_move not in move_list:
                    alternate = alternate + 1
                    if alternate > 1:
                        alternate = 0

                if computer_move not in move_list:
                    if alternate == 1:
                        board.pop(computer_move)
                        board.insert(computer_move, "x")
                        break


                    if alternate == 0:
                        board.pop(computer_move)
                        board.insert(computer_move, "o")
                        break

        #horizontal
        def Xcheckboard(x,y,z):
            if board[x] == board[y] == board[z] == "x":
                print_board()
                print("X won")
                exit()

        def Ocheckboard(x,y,z):
            if board[x] == board[y] == board[z] == "x":
                print_board()
                print("O won")
                exit()

        for i in range(0, 6,3):
            Xcheckboard(0+i,1+i,2+i)

        # Xcheckboard(0,1,2)
        # Xcheckboard(3,4,5)
        # Xcheckboard(6, 7, 8)

        # if board[0] == board[1] == board[2] == "x":
        #         print_board()
        #         print("X won")
        #         exit()

        for i in range(0, 6, 3):
            Ocheckboard(0+i,1+i,2+i)

        # if board[0] == board[1] == board[2] == "o":
        #         print_board()
        #         print("o won")
        #         exit()


        #vertical
        for i in range(0,2,1):
            Ocheckboard(0 + i, 3 + i, 6+ i)
        for i in range(0,2,1):
            Xcheckboard(0 + i, 3 + i, 6+ i)

        # if board[0] == board[3] == board[6] == "o":
        #         print_board()
        #         print("o won")
        #         exit()
        # if board[1] == board[4] == board[7] == "o":
        #         print_board()
        #         print("o won")
        #         exit()
        # if board[2] == board[5] == board[8] == "o":
        #         print_board()
        #         print("o won")
        #         exit()



        # if board[0] == board[3] == board[6] == "x":
        #         print_board()
        #         print("X won")
        #         exit()
        # if board[1] == board[4] == board[7] == "x":
        #         print_board()
        #         print("X won")
        #         exit()
        # if board[2] == board[5] == board[8] == "x":
        #         print_board()
        #         print("X won")
        #         exit()


        #diagonal
        if board[0] == board[4] == board[8] == "o":
                print_board()
                print("o won")
                exit()
        if board[2] == board[4] == board[6] == "o":
                print_board()
                print("o won")
                exit()
        if board[0] == board[4] == board[8] == "x":
                print_board()
                print("X won")
                exit()
        if board[2] == board[4] == board[6] == "x":
                print_board()
                print("X won")
                exit()

        move_list.append(computer_move)

        print_board()



if __name__ == '__main__':

    question = input("Do you want to play 2 player or computer: ")

    if question == "2player":
        board = [" "," "," "," "," "," "," "," "," "]
        def print_board():
            print("|{}|{}|{}|".format(board[0],board[1],board[2]))
            print("|{}|{}|{}|".format(board[3],board[4],board[5]))
            print("|{}|{}|{}|".format(board[6],board[7],board[8]))
        print_board()

        play_game()

    if question == "computer":
        board = [" "," "," "," "," "," "," "," "," "]
        def print_board():
            print("|{}|{}|{}|".format(board[0],board[1],board[2]))
            print("|{}|{}|{}|".format(board[3],board[4],board[5]))
            print("|{}|{}|{}|".format(board[6],board[7],board[8]))
        print_board()
        play_computer()