# x = input("Enter a 4-digit number:")
# fourth = x%10
# third = (x/10)%10
# second = (x/100)%10
# first = (x/1000)%10
# if (fourth,third,second,first)==(first,second,third,fourth):
#     print("The number {} is the same backwards.").format(x)
# else:
#     exit()


def is_palindrome(i):
    fourth = i % 10
    third = (i / 10) % 10
    second = (i / 100) % 10
    first = (i / 1000) % 10
    if (first, second, third, fourth) == (fourth, third, second, first):
        return True
    return False

def palindrome():
    for i in range(1111,9999+1):
        if  is_palindrome(i):
            print("{} is a palindrome").format(i)

palindrome()

# if __name__ == "__main__":
#     palindrome()

