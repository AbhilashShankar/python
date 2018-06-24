"""
Madhava gives the following infinite series expansion of PI
PI/4 = 1 - 1/3 + 1/5 - 1/7 ....
"""
# print(1%2,2%2,3%2,4%2)
# counter=0
# for i in range(1,9,2):


def madhava(n):
    counter = 0
    sum = 0
    for i in range(1,n+1,2):
        counter = counter + 1
        if counter%2 == 0:
            sum = sum - 1/float(i)
            # print("even {}".format(i))
        else:
            sum = sum + 1/float(i)
            # print("odd {}".format(i))
    return(sum*float(4.0))

if __name__ == '__main__':
    print(madhava(1000000))
