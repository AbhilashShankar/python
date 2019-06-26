
def mult(number):
    for i in range(20):
        if number%2 == 1:
            number = (number*3)+1
        else:
            number = number/2
        print(number)

if __name__ == '__main__':
    number = input("Input a number: ")
    mult(number)