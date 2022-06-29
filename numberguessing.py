import random

#global var of player score and computer score
global player_score, computer_score
player_score = 0
computer_score = 0

trials = int(input('Podaj liczbe ile razy chcesz spróbować: '))
for trails in range (0 , trials):
    #input
    r_number=int(input('Guess numer from 1-10 : '))

    #pc random number
    pc_random = random.randint(1,10)

    #if r_number = input then print("u guessesd right") if not print("try again")
    if r_number == pc_random:
        print('You guessed right ')
        player_score += 1
    else:
        print('try again, right answer was: ', pc_random)
        computer_score += 1

    #print scoreof player and computer
    print('player score: ', player_score, 'computer socre: ', computer_score)
    trials -=1