#given array of integers, find the most recurring integer
#works with strings


def recurringList():
    numList = [1,1,2,3,3,3]
    numbersTaken = list()
    repeatedNumbers = dict()

    listLength = len(numList)
    count = 0

    #start with first digit, go through next digits, change to second, go through next.....
    for i in range(listLength):
        for b in range(i+1,listLength):
            if numList[i] not in numbersTaken:
                if numList[i] == numList[b]:
                    count = count + 1

        #if it counts mulitple times, input it into the dictionary
        if count >= 1:
            #update dictionary with the   number:count
            repeatedNumbers.update({numList[i]:count})

        #reset count, and add number to numberstaken, so no recounts
        count = 0
        numbersTaken.append(numList[i])

    print(repeatedNumbers)

    v = list(repeatedNumbers.values())
    k = list(repeatedNumbers.keys())
    print(k[v.index(max(v))], "repeated the most")

recurringList()


