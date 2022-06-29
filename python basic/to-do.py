from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != '':
        lb.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('warning', 'please enter some task.')

def deleteTask():
    lb.delete(ANCHOR)

def quit():
    window.destroy()

#create a window
window = Tk()
window.geometry('500x450+500+200')
window.title('To-do list')
window.config(bg='#223441')
window.resizable(width=False, height=False)

frame = Frame(window)
frame.pack(pady=10)


lb = Listbox(
    frame,
    width = 25,
    height= 8,
    font=('Times', 18),
    bd = 0,
    fg = '#464646',
    highlightthickness = 0,
    selectbackground = '#a6a6a6',
    activestyle = 'none',
)

lb.pack(side=LEFT, fill=BOTH)

task_list = [

]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    window,
    font=('times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


delTask_btn = Button(
    button_frame,
    text='delete task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

window.bind('<Return>', lambda event:newTask())
window.bind('<Escape>', lambda event:quit())
window.bind('<Delete>', lambda event: deleteTask())

window.mainloop()