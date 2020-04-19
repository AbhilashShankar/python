#finds the prime numbers in a given list of numbers
numberList = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for i in range(len(numberList)):
    for b in range(2,20):
        if numberList[i] * b in numberList:
            numberList.remove(numberList[i] * b)
            print(numberList)