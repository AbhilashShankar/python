x = input("What number do you want the factorial of: ")
product = 1
for i in range(1,int(x)+1):
    product = product * i
    print(i, product)