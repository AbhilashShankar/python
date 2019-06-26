import random

for b in range(20):
    print_number = ""
    x = random.randint(1, 5)
    for i in range(x):
         print_number = print_number + "x"
    print(print_number)
