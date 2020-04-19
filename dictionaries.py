menu = dict(Pizza=8, Drink=1, Burrito=12)
userOrder = {}
finalPrice = 0
print(menu)


x = input("What items do you want, and how much(ex: pizza,2,burrito,3 If no numbers put it becomes 1): ")
x = x.split(",")


for i in range(len(x)):
    try:
        if isinstance(int(x[i]),int):
            userOrder.update({str(x[i - 1].capitalize()): int(x[i])})
    except ValueError:
        userOrder.update({str(x[i].capitalize()): 1})


print(userOrder)


for i in userOrder:
    finalPrice = finalPrice + (menu[i]*userOrder[i])


print(finalPrice)

