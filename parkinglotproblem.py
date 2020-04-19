# parking spots, cars move in and out randomly

import random

parkspace = ["unoccupied","unoccupied","unoccupied"]

print(parkspace)


for i in range(27):
    if "car1 is occupying" not in parkspace:
        car1 = random.randint(0, 2)
        if parkspace[car1] == "unoccupied":
            parkspace[car1] = "car1 is occupying"

        print(parkspace)

    if "car2 is occupying" not in parkspace:
        car2 = random.randint(0, 2)
        if parkspace[car2] == "unoccupied":
            parkspace[car2] = "car2 is occupying"

        print(parkspace)

    if "car3 is occupying" not in parkspace:
        car3 = random.randint(0, 2)
        if parkspace[car3] == "unoccupied":
            parkspace[car3] = "car3 is occupying"

        print(parkspace)


        time = random.randint(0, 5)
        if time == 5:
            parkspace[car1] = "unoccupied"

        time = random.randint(0, 5)
        if time == 5:
            parkspace[car2] = "unoccupied"

        time = random.randint(0, 5)
        if time == 5:
            parkspace[car3] = "unoccupied"

