def getpalindrome(a):
    check = list()
    d = list(a)
    for i in a[::-1]:
        check.append(i)
    if d == check:
        print("This number is a palindrome")
    else:
        print("This number is not a palindrome")



if __name__ == '__main__':
    a = str(input("What is your number: "))
    getpalindrome(a)

