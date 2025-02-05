from kigyo import *
import random
'''a = int(input('Adj egy számot: '))

szam1 = int(input('Adj egy számot: '))
szam2 = int(input('Adj egy számot: '))
szam3 = int(input('Adj egy számot: '))

print(f'A háromszög({szam1} cm, {szam2} cm, {szam3} cm) szerkeszthető? : {szerkesztheto(szam1, szam2, szam3)}\nA kerülete: {kerulet(szam1, szam2, szam3)} cm\nTerülete: {terulet(szam1, szam2, szam3)} cm^2')
print(f'A páros számok összege {a}-ig: {parosossz(a)}')'''
jegyek = []
napok = ['hetfo', 'kedd', 'szerda', 'csutortok', 'pentek', 'szombat', 'vasarnap']
print(napok[0])

jegyek.append(5)
egyjegy = int(input('Masodik jegyed? '))
jegyek.append(egyjegy)
harmadik = random.randint(1,6)
jegyek.append(harmadik)
for i in range(len(jegyek)):
    print(f'{i+1}. jegy: {jegyek[i]}')