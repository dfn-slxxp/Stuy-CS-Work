from math import pi, sqrt

# Classwork

def radiusToArea(r):
    return pi * (r ** 2)

def triangleArea(b, h):
    return 0.5 * b * h



# Homework

def squareIt(x, y):
    return (x + y) ** 2
print(squareIt(4, 3))                               # Provided Test Case

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1 ) ** 2)



# Challenge

def militaryTime(h, m, s, ampm):
    match ampm.lower():
        case "am":
            return f"{h}:{m}:{s}"
        case "pm":
            return f"{h+12}:{m}:{s}"

        case _:
            return "Invalid Meridiem Indicator (AM/PM)"
        
print(militaryTime(11, 59, 23, "pm"))               # Provided Test Case