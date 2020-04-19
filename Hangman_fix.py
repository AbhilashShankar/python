##this program is hangman
import random

wordList = [
"dictionary","pizza","facts", 'psychedelic','rod','creature','adventurous','effect',
'prick','language','quirky','sisters','spark','agonizing','sea','unequal','cannon',
'sweater','flowers','earthy','guard','multiply','free','hallowed','inform','trot',
'premium','blush','quack','blood','birth','zesty']

##choose a word, split it, and determine its length
wordChosen = wordList[random.randint(0,(len(wordList)-1))]
wordSplit = list(wordChosen)
wordLength = len(wordChosen)

##create the player inputs list
playerList = list()
for b in range(wordLength):
    playerList.append("-")
counter = 0

##the game
while True:
    playerInput = input("Enter a Letter: ")

    if playerInput == wordChosen:
        print("Congratulations, you guessed the word!!!")
        exit()

    for i in range(0,wordLength):
        if playerInput == wordSplit[i]:
            playerList.pop(i)
            playerList.insert(i, playerInput)

    if playerInput not in wordSplit:
        counter = counter + 1

    print(' '.join(playerList))
    print(counter)

    if playerList == wordSplit:
        print("Congratulations, you guessed the word!!!")
        exit()
    if counter == 6:
        print("You Lose!! The word was '{}'".format(wordChosen))
        exit()

