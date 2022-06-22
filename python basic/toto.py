import random


liczba = random.randint(1,10)
print('Wylosowana liczba to: ', liczba)

for i in range(3):
    odp = input('Jaką liczbę mam na myśli: ')

    if liczba == int(odp):
        print(f'to twoja {i+1} proba')
        print('Zgadłes')
        break
    elif i ==2:
        print('Miałem na myśli liczbę: ', liczba)
    else:
        print(f'to twoja {i + 1} proba, sproboj jeszcze raz')
