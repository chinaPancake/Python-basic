import random

try:
    ile_liczb = int(input('Podaj ile liczb chcesz losować: '))
    maks_liczba = int(input ('Z ilu liczb chcesz losować: '))

    if ile_liczb > maks_liczba:
        print('błędne dane')
        exit()

except ValueError:
    print('Błędne dane!')
    exit()

liczby = []
i = 0

while i < ile_liczb:
    liczba = random.randint(1, maks_liczba) #tutaj losuje nam liczby
    if liczby.count(liczba) == 0: #tutaj liczy ile liczb jest wpisanych
        liczby.append(liczba)
        i += 1 #inkrementujemy i

#petla while otowrzy się tyle razy ile chcę wylosować liczb
for i in range(3):
    print("Wytypuj %s z %s liczb: " % (ile_liczb, maks_liczba))
    typy = set()
    i = 0
    while i < (ile_liczb):
        try:
            typ = int(input('podaj liczbę %s: ' % (i+1)))
        except ValueError:
            print('Błędne dane')
            continue

        if 0 < typ <=maks_liczba and typ not in typy:
            typy.add(typ)
            i += 1

    trafione = set(liczby) & typy
    if trafione:
        print('\nIlośc trafień: %s' % len(trafione))
        print('Trafione liczby: ', trafione)
    else:
        print('brak trafien. sprobuj jeszcze raz')

    print('\n' + 'x' * 40 + '\n') #wypisuje 40 znakow x

print('Wylsoowane liczby to:', liczby)