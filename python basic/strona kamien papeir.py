from random import choice
from tkinter import Tk, Label, Button

wynik = 0
wynik_cpu = 0
available_choices = ["paper", "rock", "scissors"]
def play(player, cpu):
    win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:

        return True
    else:
        return False
def play_cmd(player):
    global text_label
    global wynik
    global wynik_cpu
    global text_score
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text=f"Tie! Try again! and i chosed {cpu}", fg="blue")
    elif is_user_winner:
        text_label.config(text=f"You win... Let's play again and i chosed {cpu} ", fg="green")
        wynik +=1
        text_score.config(text=f' player {wynik} : cpu {wynik_cpu}')
    else:
        text_label.config(text=f"I win, I win! and i chosed {cpu}", fg="red")
        wynik_cpu +=1
        text_score.config(text=f' player {wynik} : cpu {wynik_cpu}')

root = Tk()
root.title("Paper, Rock, Scissors")
root.geometry("800x600")
text_label = Label(root, font=40, text="Let's play paper, rock, scissors!")
text_label.pack()
text_score = Label(root, font= 40,)
text_score.pack()

Button(
    root, text="📃 Paper", font=40, width=10, command=lambda: play_cmd("paper")
).pack()
Button(
    root, text="🤘 Rock", font=40, width=10, command=lambda: play_cmd("rock")
).pack()
Button(
    root, text="✂ Scissors", font=40, width=10, command=lambda: play_cmd("scissors")
).pack()


root.mainloop()