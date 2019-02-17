#this program assumes the basket is at a 90 degree angle from the ground.
import math

def get_hypotenuse():
    hypotenuse = math.sqrt((distance * distance) + (height * height))
    print(hypotenuse)


def get_throw_angle(height,distance):
    toa = float(height)/float(distance)
    angle_throw = math.degrees(math.atan(toa))
    return angle_throw


if __name__ == '__main__':
    distance = input("How far away is the object from the ground, in feet")
    height = input("How high is the object from the ground, in feet")
    print(get_throw_angle(height,distance))
