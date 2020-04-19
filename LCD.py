LCDNumbers = [
" ___\n"
"|   |\n"
"|   |\n"
" ___\n",

" |\n"
" |\n"
" |\n"
" |\n",

" ___\n"
"    |\n"
" ___\n"
"|    \n"
" ___\n",

"____\n"
"    |\n"
"____\n"
"    |\n"
"____\n",

"|   |\n"
" ___\n"
"    |\n",

" _____\n"
"|  \n"
"____\n"
"    |\n"
"____\n",]

number = input("Input a number: ")
number_length = len(str(number))
numberList = list(number)
print_list = list()


for i in range(number_length):
    print(LCDNumbers[int(numberList[i])])