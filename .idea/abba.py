x = input("Enter a 4-digit number:")

fourth = x%10
third = (x/10)%10
second = (x/100)%10
first = (x/1000)%10


if (fourth,third,second,first)==(first,second,third,fourth):
    print("The number {} is the same backwards.").format(x)
else:
    exit()

# for i in range(10):
#     z = x%10
#     x = x/10
#     if z == 0:
#         exit()
#     print(z)
# print(x)
