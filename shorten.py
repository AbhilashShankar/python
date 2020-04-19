#!/usr/bin/env python


##shorten repeating values
def shortenString():
    global s
    s = list(s)
    for i in range(1, len(s)):
        try:
            while s[i] == s[i - 1]:
                s.pop(i)
        except IndexError:
            return s


##check only unique values
def uniqueString(s):
    s = list(s)
    newList = list()
    # print(s)

    for i in range(len(s)):
        if s[i] not in newList:
            newList.append(s[i])
    s = newList
    return s

def uniqueStringII(s):
    #set() method is used to convert any of the iterable to the distinct element and sorted sequence of iterable elements, commonly called Set.
    return list(set(s))


if __name__ == '__main__':
    s = "aabbaffffffeeeaccaafffa"
    a = uniqueString(s)
    print("Method I {}".format(a))
    a = uniqueStringII(s)
    print("Method II {}".format(a))
