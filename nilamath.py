"""
nilakantha pi formula 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) and so on...
"""
x = 0
y = 0
t = 0
sum = 0
for i in range(2,1000,2):
    sum = sum + 1

    x = i * (i + 1) * (i + 2)
    y = float(4)/x

    if sum%2 == 1:
        t = t + y
    if sum%2 == 0:
        t = t - y
    print(t+3)
