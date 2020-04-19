#find pi using euler basal formula
# 1/1^2 + 1/2^2 + 1/3^2....   = (pi^2)/6
from math import sqrt
product = 0
for i in range(1,1000):
    product = product + 1/(i*i)

print(sqrt(product*6))