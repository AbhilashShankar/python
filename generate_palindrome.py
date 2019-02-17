from datetime import datetime


def method1():
    start_time = datetime.now()
    first = 0
    for i in range(9):
        first = 1001 + first
        second = 0
        for i in range(10):
            if i > 0:
                second = second + 110
            print(second + first)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


def method_arthimetic():
    for a in range(1, 10):
        for b in range(0, 10):
            pal = int(a) * 1000 + int(b) * 100 + int(b) * 10 + int(a)
            print "{}".format(pal)


def is_palindrome(i):
    fourth = i % 10
    third = (i / 10) % 10
    second = (i / 100) % 10
    first = (i / 1000) % 10
    if (first, second, third, fourth) == (fourth, third, second, first):
        return True
    return False


def palindrome():
    start_time = datetime.now()
    for i in range(1111, 9999):
        if is_palindrome(i):
            print(i)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


if __name__ == '__main__':
    # palindrome()
    method1()
    # method_arthimetic()
