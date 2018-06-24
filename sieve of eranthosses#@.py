# def gen_prime(N):
#     numbers = range(2,N)
#     for i in range(2,N):
#         for j in range(i, N):
#             print("i={} j={}".format(i,j))
#             # multiple = i*j
#             # if multiple in numbers:
#             #     numbers.remove(multiple)
#     print (numbers)

numbers = range(2,121,1)
def get_prime2(N):

    # for y in range(0,100,1):
    x = 0
    for y in range(0,5,1):
        for i in range((N-1)/numbers[y]):
            x = x + 1
            index = numbers[y]*(1+x)
            if index < N:
                numbers.remove(index)
            else:
                continue
    print(numbers)

if __name__ == "__main__":
    # gen_prime(120)
    get_prime2(120)
