'''import random
jegyek = []

elso = int(input('Adj jegyet: '))
jegyek.append(elso)
for i in range(1,7):
    jegyek.append(random.randrange(1,6))
    print(f'{i}. jegy: {jegyek[i-1]}')


def lista(jegyek:list):
    for egyjegy in jegyek:
        print(egyjegy, end=' ')

lista(jegyek)

for index, érték in enumerate(jegyek):
    print(f'{index}. indexű elem értéke {érték}')


for betu in nev:
    print(betu)

for betuhelye in range(len(nev)):
    print(f'{betuhelye}. betű {nev[betuhelye]}')'''

nev = 'Tizedikdé Ketteske'

for index, érték in enumerate(nev):
    print(f'{index}. elem: {érték}')

for index, érték in enumerate(nev):
    if index % 2 != 0:
        print(f'{index+1}. elem: {érték}')