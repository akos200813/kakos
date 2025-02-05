import math

def szerkesztheto(a:int, b:int, c:int):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def kerulet(a:int, b:int, c:int):
    return a+b+c

def terulet(a:int, b:int, c:int):
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def parosossz(a:int):
    osszeg = 0
    for i in range(1, a+1):
        if i % 2 == 0:
            osszeg += i
    return osszeg

def atlag(osszeg, db):
    return osszeg / db