from random import choice
from tkinter import *
from tkinter import messagebox
#a)
def list():
    L = ['porsche','book', 'label', 'pikatchu', 'yellow', 'nigger']
    word = choice(L)
    return (word)

def makeStars(s):
    return '*'*len(s)
#b)
def guess():
    
    global hards
    global to_show
    global T
    new_to_show = ''
    hards = hards - 1
    txt = myEntry.get()
    txt = txt.lower()
    print(txt)
    if txt in to_guess:
        for i in range(len(to_guess)):
            if txt==to_guess[i]:
                if txt in T:
                    showMsg2()
                else:
                    new_to_show += txt
                    T.append(txt)
                    
            else:
                new_to_show += to_show[i]
        to_show = new_to_show
        wordLabel.config(text = to_show)
    wordLabel2.config(text = hards)
    
    if hards == 0:
          showMsg()


def showMsg():
    msg = messagebox.showinfo(title = 'Вы не прошли!',
                              message = 'попытки закончились! Перезагрузите страницу чтоб начать заново!')
def showMsg2():
     msg = messagebox.showinfo(title = 'Вы вели повторяющую букву букву !',
                              message = 'закройте меседжбох и продолжите дальше!')

def delText():
    myEntry.delete(first = 0,
                   last = 'end')
             
T = []

to_guess = list()
to_show = makeStars(to_guess)
hards = len(to_show)+3

root = Tk()
root.geometry('500x500')
btnDel = Button(root,height=2, width=20,text = 'очистить',command = delText)
btnGet = Button(root,height=2, width=20,text = 'получить',command = guess,)

myEntry = Entry(root,bd = 10) 
wordLabel = Label(root,bg = '#ffffff',height=2, width=20, text = to_show,font=10)
wordLabel2 = Label(root,bg = 'yellow',height=2, width=5, text = hards)
wordLabel2.grid(row=0, column=1)
wordLabel.grid(row=0, column=0)
myEntry.grid(row=7, column=0)
btnDel.grid(row = 20, column = 0)
btnGet.grid(row = 10,column = 0)
root.mainloop()
