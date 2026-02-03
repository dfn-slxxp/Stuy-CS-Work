from math import pi, sqrt

# Classwork

def facesOnMoney() :
    try:
        m = int(input("Please enter a denomination of Money: $"))
    except Exception as e:
        print("Please enter a valid number")
    else:
        match m:
            case 1:
                print("George Washington")
            case 2:
                print("Thomas Jefferson")
            case 5:
                print("Abraham Lincoln")
            case 10:
                print("Alexander Hamilton")
            case 20:
                print("Andrew Jackson")
            case 50:
                print("Usysses S. Grant")
            case 100:
                print("Benjamin Franklin")
            
            case _:
                print("Invalid Denomination of Money")

def nameThatTriangle():
    try:
        inp = input("Please enter 3 sides of a triangle separated by spaces: ").split()
        m = [int(nm) for nm in inp]
        m.sort()
    except Exception as e:
        print("Please input numbers separated by spaces!")
    else:
        if (m[0] + m[1] < m[2]):
            print("This is not a real triangle. Please input a valid triangle.")
        else:
            if(m[0] == m[1] == m[2]):
                print("This is an Equilateral Triangle")
            elif(m[0] == m[1] or m[1] == m[2] or m[0] == m[2]):
                print("This is an isosceles Triangle")
            else:
                print("This is a Scalene Triangle")



# Homework

def isLeapYear(y):
    if(y % 4 == 0):
        return(False if y % 100 == 0 and y % 400 != 0 else True)
    else:
        return(False)
isLeapYear(2000)                                # Test Cases Provided By Problem
isLeapYear(2004)                                # Test Cases Provided By Problem
isLeapYear(2008)                                # Test Cases Provided By Problem
isLeapYear(2009)                                # Test Cases Provided By Problem
isLeapYear(2100)                                # Test Cases Provided By Problem
isLeapYear(2104)                                # Test Cases Provided By Problem
isLeapYear(2200)                                # Test Cases Provided By Problem
isLeapYear(2300)                                # Test Cases Provided By Problem
isLeapYear(2400)                                # Test Cases Provided By Problem

def daysInMonth(m, y):
    if(m == 2):
        return(29 if isLeapYear(y) else 28)
    else:
        return(31 if m in [1, 3, 5, 7, 8, 10, 12] else 30)
print(daysInMonth(1, 2010))                     # Test Cases Provided By Problem
print(daysInMonth(2, 2011))                     # Test Cases Provided By Problem
print(daysInMonth(2, 2024))                     # Test Cases Provided By Problem
print(daysInMonth(4, 2011))                     # Test Cases Provided By Problem



# Challenge

def make_bricks(short, long, goal):
    if(5 * long + short < goal):
        return False
    else:
        if(short > goal):
            return True
        elif((goal - short) - 5 * long <= 0 and ((goal % 5) <= short or goal % 5 == 0)):
            return True
        else:
            return False