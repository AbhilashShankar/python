# isbn_number = input("What is your isbn number")
n = 306406152
list = [int(x) for x in str(n)]
list_value = (list[0]*9) + (list[1]*8) + (list[2]*7) + (list[3]*6) + (list[4] * 5) + (list[5]*4) + (list[6]*3) + (list[7]*2) + (list[8]*1)
print(list)
print(list_value)
def is_integer():
    if (float(float(list_value)/11))%1 == 0:
        return True
    else:
        return False

if is_integer() == True:
    print("This isbn is valid")
else:
    print("This isbn is not valid")