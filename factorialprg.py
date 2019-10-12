

def factorial1(n):
    add = 0
    fact = 1
    for i in range(1,(n+1)):
        fact = fact * i
        add = add + (float(1)/float(fact))
        print(add)

if __name__ == '__main__':
    import time

