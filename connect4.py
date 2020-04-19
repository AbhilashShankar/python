#Connect4

board = [" "," ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ",  " ", " "," ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", ]
a = 0
column_list = ["1","2","3","4","5","6","7"]






while True:
    columns = ("{} {} {} {} {} {} {}\n"
          "{} {} {} {} {} {} {}\n"
          "{} {} {} {} {} {} {}\n"
          "{} {} {} {} {} {} {}\n"
          "{} {} {} {} {} {} {}\n"
          "{} {} {} {} {} {} {}\n".format(board[0], board[1], board[2], board[3], board[4], board[5], board[6],
                                              board[7], board[8], board[9], board[10],board[11],board[12],board[13],
                                              board[14],board[15],board[16],board[17],board[18],board[19],board[20],
                                              board[21],board[22],board[23],board[24],board[25],board[26],board[27],
                                              board[28],board[29],board[30],board[31],board[32],board[33],board[34],
                                              board[35],board[36],board[37],board[38],board[39],board[40],board[41], ))
    print(columns)

    #make figure out the turns
    a = (a+1)%2
    turn = a

    #redo invalid column entries
    position = input("choose a column")
    while int(position) > int(7):
        print("your column is invalid")
        position = input("choose a column")
    while int(position) < int(1):
        print("your column is invalid")
        position = input("choose a column")



    #make the piece fall to the lowest it can
    for b in range(0,7,1):
        for i in range(35+b, -7+b, -7):
            if turn == 1:
                if position == "{}".format(column_list[0+b]):
                    if board[i] == " ":
                        board.pop(i)
                        board.insert(i, "x")
                        break
            if turn == 0:
                if position == "{}".format(column_list[0+b]):
                    if board[i] == " ":
                        board.pop(i)
                        board.insert(i, "o")
                        break


    #check if anyone won
    for j in range(0,4): ### changes values horizontally
        for h1 in range(j, 42, 7): # changes values vertically once all horizontal used.
            if board[h1] == "x":
                if board[h1 + 1] == "x":
                    if board[h1 + 2] == "x":
                        if board[h1 + 3] == "x":
                            print(columns)
                            print("x won")
                            exit()
            if board[h1] == "o":
                if board[h1 + 1] == "o":
                    if board[h1 + 2] == "o":
                        if board[h1 + 3] == "o":
                            print(columns)
                            print("o won")
                            exit()


    for c in range(0,4): ### changes values horizontally
        for h2 in range(c, 21, 7): # changes values vertically once all horizontal used.
            if board[h2] == "x":
                if board[h2 + 8] == "x":
                    if board[h2 + 16] == "x":
                        if board[h2 + 24] == "x":
                            print(columns)
                            print("x won")
                            exit()
            if board[h2] == "o":
                if board[h2 + 8] == "o":
                    if board[h2 + 16] == "o":
                        if board[h2 + 24] == "o":
                            print(columns)
                            print("o won")
                            exit()


    for k in range(6, 2, -1):
        for h3 in range(k, 27, 7): # changes values vertically once all horizontal used.
            if board[h3] == "x":
                if board[h3 + 6] == "x":
                    if board[h3 + 12] == "x":
                        if board[h3 + 18] == "x":
                            print(columns)
                            print("x won")
                            exit()

            if board[h3] == "o":
                if board[h3 + 6] == "o":
                    if board[h3 + 12] == "o":
                        if board[h3 + 18] == "o":
                            print(columns)
                            print("o won")
                            exit()

    for p in range(0,7,1): # change value horio
        for h4 in range(p, 20, 7): # changes values vertically once all horizontal used.
            if board[h4] == "x":
                if board[h4 + 7] == "x":
                    if board[h4 + 14] == "x":
                        if board[h4 + 21] == "x":
                            print(columns)
                            print("x won")
                            exit()

            if board[h4] == "o":
                if board[h4 + 7] == "o":
                    if board[h4 + 14] == "o":
                        if board[h4 + 21] == "o":
                            print(columns)
                            print("o won")
                            exit()
