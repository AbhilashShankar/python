#a! + b! + c! = a+b+c


def afactorial(number):
    first = 1
    real = 1
    for i in range(1, number+1):
        first = i
        real = first*real
    print(real)

def bfactorial(number):
    first = 1
    real = 1
    for i in range(1, number+1):
        first = i
        real = first*real
    print(real)

def cfactorial(number):
    first = 1
    real = 1
    for i in range(1, number+1):
        first = i
        real = first*real
    print(real)




for i in range(1,11):
    afactorial(i)
for i in range(1,11):
    bfactorial(i)
for i in range(1,11):
    cfactorial(i)

