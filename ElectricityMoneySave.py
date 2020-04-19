miles = int(input("How many miles have you driven"))
MPG = int(input("What is your ICE cars fuel economy(MPG)"))
gasoline = float(input("What is the price of Gas $"))
kWhUsed = int(input("How much kWh have you used"))
ppw = float(input("What is the price per kWh, in cents"))
ppw = (ppw/100)

kWhPrice = (kWhUsed * ppw)

moneySaved = (((miles/MPG)*gasoline) - kWhPrice)

print("You have paid ${} for electricity".format(int(kWhPrice)))

print("You have saved ${}".format(int(moneySaved)))