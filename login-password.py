from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title('some title')

L = "kingsss"
P = '0000'
myEntry = Entry(root,
                bd = 5)
myEntry2 = Entry(root,
                bd = 5)
def login():
    txt = myEntry.get()
    print('Вы ввели:')
    print(txt)
    if L == txt:
        msg = messagebox.showinfo(title = 'login',
                            message = txt+' это правельный пароль')
    else:
        msg = messagebox.showinfo(title = 'login',
                            message = txt+' это не правельный пароль, попробуй другой!')      
    
def password():
    txt = myEntry2.get()
    print('Вы ввели:')
    print(txt)
    if L == txt:
        msg = messagebox.showinfo(title = 'Password',
                            message = txt+' это правельный пароль')
    else:
        msg = messagebox.showinfo(title = 'Password',
                            message = txt+' это не правельный пароль, попробуй другой!')      
    
def signin():
    txt = myEntry2.get()
    txt2 = myEntry.get()
    if L and P == txt and txt2:
        msg = messagebox.showinfo(title = 'Signin',
                            message = 'вы зарегестрированы!')
    print ('f')

myEntry.grid(row = 0, column = 0)
myEntry2.grid(row = 0,column = 1)
myBtn = Button(root, text = 'print your login',
               command = login)
myBtn2 = Button(root, text = 'print your password',
               command = password)

myBtn3 = Button(root, text = 'signin',
               command = signin)
myBtn.grid(row = 1, column = 0)
myBtn2.grid(row = 1, column = 1)
myBtn3.grid(row = 0, column = 3)
root.mainloop()
