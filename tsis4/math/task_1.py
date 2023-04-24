import math
def degree_to_radian(d):
    return round(d*math.pi/180,6)

deg = int(input("write degree:"))

print("in radian:",degree_to_radian(deg))