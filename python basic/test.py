from tkinter import Tk, Button, Label

clicks=0

def click_action(button):
    global clicks
    clicks +=1
    button.config(text=f"Wow! x {clicks}")




root = Tk()
root.geometry("200x200")


text_label = Label(root, text="some text")
click_button = Button(root, text="Click me!", width=8)



click_button.pack()
text_label.pack()
click_button.config(command=lambda: click_action(click_button))

root.mainloop()
