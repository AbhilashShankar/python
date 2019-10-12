import random


def get_permutationsrandom():
    letterlist = ["a","b","c"]
    listoflists = list()
    for i in range(100):
        a = random.randint(0,2)
        b = random.randint(0,2)
        c = random.randint(0,2)
        if a != b:
            if b != c:
                if c != a:
                    if [letterlist[a],letterlist[b],letterlist[c]] not in listoflists:
                        listoflists.append([letterlist[a],letterlist[b],letterlist[c]])
    print(listoflists)



def get_permutationssystematic():
    letterlist = ["a","b","c"]
    for i in range(1):
        for a in range(0,3):
            for b in range(0,3):
                if a == b:
                    continue
                for c in range(0,3):
                    if c in [a,b]:
                        continue
                    print(letterlist[a],letterlist[b],letterlist[c])

if __name__ == '__main__':
    get_permutationsrandom()