import random
word_list = ["dictionary", "pizza", "cat", "dog"]

#generate random word
word = word_list[random.randint(0,3)]


#creating the placeholders
charactercount = list()
for i in range(len(word)):
    charactercount.append("_")



##words split up into list
characterlist = list(word)


for i in range(200):
    guess_number = -1
    guess_letter = raw_input("Guess a letter: ")
    for c in range(len(word)):
        guess_number = guess_number + 1
        if guess_letter == characterlist[guess_number]:
            charactercount.pop(guess_number)
            charactercount.insert(guess_number, guess_letter)


        if charactercount == characterlist:
            print(charactercount)
            print("Congratulations, you guessed the word!")
            quit()
    print(charactercount)