def checkAnagram1():
    word1 = "fired"
    word2 = "fried"

    counter = 0
    word1 = list(word1)
    for i in range(len(word1)):
        if word1[i] in word2:
            counter = counter + 1

    if len(word2) == counter:
        print("This is an annagram")


def checkAnagram2():
    ##sorted lists in alphabetical order
    word1 = "iceman"
    word2 = "cinema"

    if sorted(word1) == sorted(word2):
        print("These are anagrams")

checkAnagram2()