"""
Find PI using Wallis Formula: 2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 = pi/2(and so on...)
"""
def find_pi(n):
    a = 2
    b = 1
    t = 0#first value
    z = 0#second value
    w = 0#saves the value of t * z
    for i in range(1,n,1):
        if a/b == 0:
            a = a + 2
        t = (float(a)/float(b))
        w = w * t
        if a/b >= 1:
            b = b + 2
        z = (float(a)/float(b))
        w = w * z
        if t == 2.0:
            w = t * z
    return(w*2)

if __name__ == "__main__":
    print(find_pi(10000))
