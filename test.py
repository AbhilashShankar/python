
def get_fibbo(n):
    a = 0
    b = 1
    for i in range(n):
        t = a
        a = b
        b = t + b
    return t



if __name__ == "__main__":
    print(get_fibbo(4))
