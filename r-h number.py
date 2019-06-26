#This program randomly generates a Ramanujan-Hardy number

#a^3 + b^3 = c^3 + d^3

#examples:
#   1729 = 12^3 + 1^3 = 10^3 +9^3
#   4104 = 16^3 +2^3 = 15^3 + 9^3


import random
def find_rh():
    for a in range(1,1900000):
        reala = random.randint(1,100)
        realb = random.randint(1,100)
        realc = random.randint(1,100)
        reald = random.randint(1,100)
        if (reala*reala*reala) + (realb*realb*realb) == (realc*realc*realc) + (reald*reald*reald):
            if reala != realb:
                if reala != realc:
                    if reala != reald:
                        if realb != realc:
                            if realb != reald:
                                if realc != reald:
                                    print "{}^3 + {}^3 = {}^3 + {}^3 = {}".format(reala,realb,realc,reald,0)
                                    # print(reala,realb,realc,reald)

if __name__ == '__main__':
    find_rh()