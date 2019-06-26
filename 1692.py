number = input("Input a 4-digit number: ")

number_list = list()

first = (number/1000)
second = ((number/100)-((number/1000)*10))
third = ((number/10)-(number/100)*10)
fourth = (number-(number/10)*10)


for i in range(10):
    if first == i:
        if i not in number_list:
            number_list.insert((i-1),i)
    if second == i:
        if i not in number_list:
            number_list.insert((i-1),i)
    if third == i:
        if i not in number_list:
            number_list.insert((i-1),i)
    if fourth == i:
        if i not in number_list:
            number_list.insert((i-1),i)













print(number_list)

print(first)
print(second)
print(third)
print(fourth)