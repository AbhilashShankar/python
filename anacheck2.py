##c[::-1] print backwards
def method1():
    dictionary = open('american-english.txt', 'r')
    for i in dictionary:
        c = list(i)
        c.remove('\n')
        f = c[:]

        if "'" not in c:
            f.append(f[0])
            f.pop(0)

            if len(c) > 1:
                if f[::-1] == c:
                    print(c)


def method2():
    dictionary = open('american-english.txt', 'r')
    for i in dictionary:
        c = i.strip()

        if "'" not in i:
            f = (str(i[1:len(i)-1]) + str(i[0]))

            if len(c) > 2:
                if f[::-1] == c:
                    print(c)


if __name__ == '__main__':
    method2()
