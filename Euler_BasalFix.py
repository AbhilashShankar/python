#this formula can be used to calculate the value of pi,
import math
numb = 0

for i in range(1,50):
    numb = 1/(i*i) + numb
    print(math.sqrt(numb*6))

