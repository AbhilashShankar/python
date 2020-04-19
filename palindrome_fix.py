import random

##one way to solve the problem
def checkPalindrome():
    while True:
        character = input("input a character")
        characterList = list(character)
        characterListInverse = list()

        for i in range(len(character)-1, -1, -1):
            characterListInverse.append(characterList[i])

        if characterListInverse == characterList:
            print("This is a palindrome")



#generate palindromes randomly
def genRandomPalindrome():
    valuesGiven = list()
    while True:
        numberList = list()
        numberListInverse = list()

        for i in range(0,4):
            numberList.insert(i, random.randint(0,9))
        for i in range(4 - 1, -1, -1):
            numberListInverse.append(numberList[i])

        if numberList not in valuesGiven:
            if numberList == numberListInverse:
                valuesGiven.append(numberList)
                print(numberList)


#generate number palindromes orderly
def genOrderPlaindrome():
    for a in range(1000,9999+1,1):
        if str(a) == str(a)[::-1]:
            print(a)


def genLetterPalindrome():
    #0-25
    alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    characterList = list()
    valueList = list()

    #move through last 26 letters all the way up
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    characterList.append(alphabetList[a])
                    characterList.append(alphabetList[b])
                    characterList.append(alphabetList[c])
                    characterList.append(alphabetList[d])

                    if characterList == characterList[::-1]:
                        valueList.append(characterList)
                        print(characterList)
                    characterList = list()
                    characterListInverse = list()


checkPalindrome()
