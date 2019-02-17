import time
import argpars
# Abhilash@DESKTOP-CH9BPUK MINGW64 ~/Documents/github/python (master)
#  /c/Python27/python.exe  microwave.py  -h

def get_args():
    parser = argparse.ArgumentParser(description='microwave')
    parser.add_argument('-t','--time', help='How much time', required = False)
    parser.add_argument('-d','--defr ost', help='How long to defrost')
    return vars(parser.parse_args())


def countdown_clock(seconds):
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)


def defrost_type(type):
    if type == 'meat':
        countdown_clock(120)
    if type == 'seafood':
        countdown_clock(240)


if __name__ == '__main__':
    arguments = get_args()
    print arguments
    countdown_clock(int(arguments['time']))
    defrost_type(str(arguments['defrost']))