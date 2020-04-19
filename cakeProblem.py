#cake problem to figure out which cakes should be stored to get the greatest value out of it.



#variables
#different cakes, their size and value
cake_tuples = [(7, 160), (3, 90), (2, 15)]
#maximmum storage
capacity = 20

#list for the values of cakes
valueList = list()

#get the relative values of each cake
def getValues():
    #create 2 lists, one that will be sorted and one that will have the values in order
    global sortedValueList
    #movethrough the list and input their real value by dividing the value/storage
    for i in range(len(cake_tuples)):
        value = str(cake_tuples[i]).replace("(", "").replace(")", "").replace(" ", "").split(",", 1)
        value = int(value[1]) / int(value[0])
        valueList.append(value)
        sortedValueList = valueList.copy()


#sort the value list in order from least to greatest in order to check in the next function
def sortValuableList():
    #created a sorted list to move through the most valuable, to the least valuable
    for i in range(len(sortedValueList)):
        for b in range(i+1,len(sortedValueList)):
            if sortedValueList[b] > sortedValueList[i]:
                temp = sortedValueList[b]
                sortedValueList.pop(b)
                sortedValueList.insert(0,temp)


#find the value of the duffle bag
def max_duffle_value():
    getValues()
    sortValuableList()

    #the maximum value able to be carried
    max = 0

    #find the relative value of the cake where the real value is greatest.
    value1 = str(cake_tuples[valueList.index(sortedValueList[0])]).replace("(", "").replace(")", "").replace(" ", "").split(",", 1)

    step = int(value1[0])
    counter = int(value1[1])

    #use the values as long as possible
    for z in range(step,capacity,step):
        max = max + counter

    #current count is equal to how much the range was able to count up to
    current_count = z

    if current_count < capacity:
        for i in range(1, len(sortedValueList)):
            value1 = str(cake_tuples[valueList.index(sortedValueList[i])]).replace("(", "").replace(")", "").replace(
                " ", "").split(",", 1)

            #do it for as long as possible, until it can not do it
            c = True
            while c == True:
                if current_count + int(value1[0]) <= capacity:
                    max = max + int(value1[1])
                    current_count = current_count + int(value1[0])
                else:
                    c = False

    return max





print(max_duffle_value())




