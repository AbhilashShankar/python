LCD = [ #0
        " -  ",
        "|  |",
        "|  |",
        "|  |",
        " -  ",#end of zero

        "|   ",
        "|   ",
        "|   ",
        "|   ",
        "|   ",#end of one
     ]

number = raw_input("Enter your number:")

def zero():
    x = 0
    for i in range(5):
        print(LCD[x])
        x = x + 1

def one():
    y = 5
    for i in range(5):
        print(LCD[y])
        y = y + 1

if (number == "0" or number == "zero"):
    zero()
if (number == "1" or number == "one"):
    one()

