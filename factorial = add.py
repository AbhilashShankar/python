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


for a in range(1,100):
    for b in range (1,100):
        if a == b:
            continue
        for c in range(1,100):
            if c in [a,b]:
                continue
                acubed = (a*a*a)
                bcubed =(b*b*b)
                ccubed = (c*c*c)
                if acubed + bcubed + ccubed == a + b + c:
                    print(a,b,c)
                    exit()
