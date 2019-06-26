number = input("Input a 2 digit number: ")
number_list = list()
while number/10 != 0:
    first = number/10
    second = number%10
    number = first*second
    number_list.append(number)
print(number_list)
print " -> ".join(map(str,number_list))
