import random

#input
r_number=input('Guess numer from 1-10 : ')

#pc random number
pc_random = random.randint(1,10)

#if r_number = input then print("u guessesd right") if not print("try again")

if r_number == pc_random:
    print('You guessed right ')
else:
    print('try again, right answer was: ', pc_random)
