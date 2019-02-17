"""Fibbonacci"""

def get_fibbo(n):
    a = 0
    b = 1
    for i in range(n):
        t = a
        a = b
        b = t + b
    return(t)

def get_fibbo_odd(n):
    c = 0
    w = 0
    while True:
        c = c + 1
        t = get_fibbo(c)
        if t%2 == 1:
            print(t,w)
            w = w + 1
        if w == n+1:
            return

if __name__ == "__main__":
    x = input("How much numbers do you want: ")
    get_fibbo_odd(x)
    get_fibbo(100)
