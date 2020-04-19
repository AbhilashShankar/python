firstNumber = 0
secondNumber = 1
product = 0

for i in range(9):
    #product is equal to first number + second number
    product = firstNumber + secondNumber
    #first number is current second number value
    firstNumber = secondNumber
    #update second number to the product
    secondNumber = product

    print(product)

