from tkinter import messagebox
from tkinter import *
StringVar
root = Tk()
root.title('креситики и нолики')
root.geometry('600x400')

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

bclick = True
f = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def uzd_6(btn):
    global bclick, f
    global bclick
    if btn['text'] == ' ' and bclick == True:
        btn['text'] = 'X'
        bclick = False
        checkForWin()
        f = f+1
    elif btn["text"] == " " and bclick == False:
        btn["text"] = "O"
        bclick = True
        checkForWin()
   
    f = f+1
def checkForWin():
    if (myBtn1['text'] == 'X' and myBtn2['text'] == 'X' and myBtn3['text'] == 'X' or
        myBtn4['text'] == 'X' and myBtn5['text'] == 'X' and myBtn6['text'] == 'X' or
        myBtn7['text'] == 'X' and myBtn8['text'] == 'X' and myBtn9['text'] == 'X' or
        myBtn1['text'] == 'X' and myBtn5['text'] == 'X' and myBtn9['text'] == 'X' or
        myBtn3['text'] == 'X' and myBtn5['text'] == 'X' and myBtn7['text'] == 'X' or
        myBtn3['text'] == 'X' and myBtn6['text'] == 'X' and myBtn9['text'] == 'X' or
        myBtn1['text'] == 'X' and myBtn4['text'] == 'X' and myBtn7['text'] == 'X' or
        myBtn2['text'] == 'X' and myBtn5['text'] == 'X' and myBtn8['text'] == 'X' or
        myBtn7['text'] == 'X' and myBtn6['text'] == 'X' and myBtn9['text'] == 'X'):
        
        messagebox.showinfo("Крестики-Нолики",'X выйграл!')

    

    elif (myBtn1['text'] == 'O' and myBtn2['text'] == 'O' and myBtn3['text'] == 'O' or
          myBtn4['text'] == 'O' and myBtn5['text'] == 'O' and myBtn6['text'] == 'O' or
          myBtn7['text'] == 'O' and myBtn8['text'] == 'O' and myBtn9['text'] == 'O' or
          myBtn1['text'] == 'O' and myBtn5['text'] == 'O' and myBtn9['text'] == 'O' or
          myBtn3['text'] == 'O' and myBtn5['text'] == 'O' and myBtn7['text'] == 'O' or
          myBtn3['text'] == 'O' and myBtn6['text'] == 'O' and myBtn9['text'] == 'O' or
          myBtn1['text'] == 'O' and myBtn4['text'] == 'O' and myBtn7['text'] == 'O' or
          myBtn2['text'] == 'O' and myBtn5['text'] == 'O' and myBtn8['text'] == 'O' or
          myBtn7['text'] == 'O' and myBtn6['text'] == 'O' and myBtn9['text'] == 'O'):
        
        messagebox.showinfo("Крестики-Нолики", 'O выйграл!')
    elif (f == 10):
        messagebox.showinfo("Крестики-Нолики", 'ничья, ПОПЫТайтесь заново')
buttons = StringVar()

myBtn1  = Button(root,height=2, width=2,text = ' ', command = lambda:uzd_6(myBtn1))

myBtn2 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn2))

myBtn3 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn3))

myBtn4 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn4))

myBtn5 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn5))

myBtn6 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn6))

myBtn7 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn7))

myBtn8 = Button(root, height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn8))

myBtn9 = Button(root,height=2, width=2,text = ' ',command = lambda:uzd_6(myBtn9))
myBtn1.grid(row = 0, column = 1,)
myBtn2.grid(row = 0 , column = 2)
myBtn3.grid(row = 0, column = 3)
myBtn4.grid(row = 1, column = 1)
myBtn5.grid(row = 1, column = 2)
myBtn6.grid(row = 1, column = 3)
myBtn7.grid(row = 2, column = 1)
myBtn8.grid(row = 2, column = 2)
myBtn9.grid(row = 2, column = 3)
root.mainloop()
