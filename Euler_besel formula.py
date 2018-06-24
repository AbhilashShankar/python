import math

def find_pi(m):
    n = 1
    x = 0
    t = 0
    y = 0
    for i in range(m-1):
        x = float(1/float(1)**2)
        n = n + 1
        y = float(1/float(n)**2)
        t = t + y
        if y == 0.25:
            t = x + y
    return(math.sqrt(t*6))

def find_pi2(n):
    # pi = 0
    # for i in range(1,n+1):
    #     pi = pi + 1 / float(i**2)
    pi = sum( [1/float(i**2) for i in range(1,n+1)])
    return math.sqrt(pi*6)

if __name__ == "__main__":
    print(find_pi(1000))
    print(find_pi2(1000))

