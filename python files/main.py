from tkinter import *
from tkinter import messagebox

#Main Window
main_win = Tk()
main_win.geometry('1000x800')
main_win.title("The List of To-Do's")
main_win.resizable(width=False, height=False)
main_win.config(bg='#223441')

#Framing inside main window
frame = Frame(main_win)
frame.pack(pady=10)

#List box
listbox1 = Listbox(frame,width=25,height=8,font=('Times',18),bd=0,highlightthickness=1,selectbackground='#a6a6a6',activestyle="none",)
listbox1.pack(side=LEFT, fill=BOTH)

test_list =['get apples','get milk','get eggs','get bullets']

for item in test_list:
    listbox1.insert(END, item)


#scroll bar

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=BOTH)
listbox1.config(yscrollcommand=scroll.set)
scroll.config(command=listbox1.yview)

#Entry Box
user_entry = Entry(main_win, font=('times', 24))
user_entry.pack(pady=20)

#frame for another button
button_frame = Frame(main_win)
button_frame.pack(pady=20)


def newTask():
    task= user_entry.get()
    if task != "":
        listbox1.insert(END, task)
        user_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deltask():
    listbox1.delete(ANCHOR)





#Buttons
addTsk_btn = Button(button_frame, text = 'Add new Task', font = ('times 14'),bg='#c5f776',padx=20,pady=10,command=newTask)
addTsk_btn.pack(fill=BOTH, expand=True,side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deltask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


def deltask():
    listbox1.delete(ANCHOR)

main_win.mainloop()