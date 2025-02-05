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

a = int(input('Adj egy számot: '))

'''szam1 = int(input('Adj egy számot: '))
szam2 = int(input('Adj egy számot: '))
szam3 = int(input('Adj egy számot: '))

print(f'A háromszög({szam1} cm, {szam2} cm, {szam3} cm) szerkeszthető? : {szerkesztheto(szam1, szam2, szam3)}\nA kerülete: {kerulet(szam1, szam2, szam3)} cm\nTerülete: {terulet(szam1, szam2, szam3)} cm^2')'''


print(f'A páros számok összege {a}-ig: {parosossz(a)}')