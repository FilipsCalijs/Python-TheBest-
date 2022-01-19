from tkinter import *
from random import randint
from random import *
X = randint(1,100)


def yes(event):
 btnYes.place(x = randint(0,500), y = randint(0,500))

root = Tk()
root.geometry('500x400')

root.bind_all('a', yes)
btnYes = Label(root,text = "if you klick you get 100$",bg = 'white')
btnYes.bind('<Enter>',yes)

btnYes.place (x = 170,y = 100)
root.mainloop()
