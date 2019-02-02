#2/n = sqrt2 + sqrt2/2
import math
top = 0
add = 1

for i in range(50):
    top = math.sqrt(2 + top)
    x = top/2
    add = (x) * add
    print(2/add)
