def rhnumber():
    for a in range(1,100):
        for b in range (1,100):
            if a == b:
                continue
            for c in range(1,100):
                if c in [a,b]:
                    continue
                for d in range(1,100):
                    if d in [a,b,c]:
                        continue
                    acubed = (a*a*a)
                    bcubed =(b*b*b)
                    ccubed = (c*c*c)
                    dcubed = (d*d*d)
                    if acubed + bcubed == ccubed + dcubed:
                          print(a,b,c,d)
                          exit()

if __name__ == '__main__':
    rhnumber()