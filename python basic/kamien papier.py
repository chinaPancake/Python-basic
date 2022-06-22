from tkinter import Tk, Button, Label
from random import choice

avb_choices = ['papier', 'kamien', 'nozyce']
cpu = choice(avb_choices)

def play(player, cpu):
    win_with = {'papier': 'kamien', 'kanien': 'nozyce', 'nozyce': 'papier'}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False

def play_cmd(player):
    global text_label
    cpu = choice(avb_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text='Remis zagrajmy jeszcze raz', fg='blue')
    elif is_user_winner:
        text_label.config(text='Wygrales zagrajmy jeszcze raz', fg='green')
    else:
        text_label.config(text='wygralem wygralem ', fg='red')


root = Tk()
root.title('Kamień, Papier, Nożyce')
root.geometry('500x500')

text_label = Label(root, font=40, text="Zagrajmy w kamien papier nozyce")
text_label.pack()

Button(
    root, text='papier', font= 40, width=10, command=lambda: play_cmd('papier')
).pack()

Button(
    root, text='kamien', font = 40, width=10, command=lambda: play_cmd('kamien')
).pack()

Button(
    root, text='nozyce', font = 40, width=10, command=lambda: play_cmd('nozyce')
).pack()



print(cpu)
root.mainloop()