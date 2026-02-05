# Classwork

def sumFromZeroToN(n):
    if n <= 0:
        return 0
    else:
        counter = 0
        while True:
            if(n == 0):
                break
            else:
                counter += n
                n -= 1
        return counter



# Homework

def sumDigits(n):
    n = abs(n)
    count = 0
    while True:
        if n == 0:
            break
        else:
            count += n % 10
            n = n // 10
    return count