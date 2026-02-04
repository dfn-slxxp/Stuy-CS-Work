# Classwork

def evenSequence():
    lst = []
    n = 0
    while n*2 < 30:
        n += 1
        lst.append(n*2)
    print(*lst)

def multiplesOf3Seq():
    lst = []
    n = 0
    while n * 3 + 9 < 60:
        n += 1
        lst.append(n * 3 + 9)
    print(*lst)



# Homework

def perfectSquares():
    lst = []
    n = 0
    while n ** 2 < 10000:
        n += 1
        lst.append(n ** 2)
    print(*lst)

def sumMultiplesOf5():
    s, n = 0, 0
    while n <= 3000:
        s += n if n % 5 == 0 else 0
        n += 1
    print(s)

def sumMultiplesOf5And7() :
    s, n = 0, 0
    while n <= 3000:
        s += n if n % 5 == 0 or n % 7 == 0 else 0
        n += 1
    print(s)