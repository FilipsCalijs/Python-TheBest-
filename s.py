from tkinter import *
def change_player():
    global player

    if player == 'O':
        player = 'X'
    else:
        player = 'O'
root = Tk()
root.title('crstiki noliki')
root.geometry('600x400')

bclick = True
def uzd_6(btn):
    global bclick
    if btn['text'] == ' ' and bclick == True:
        btn['text'] = 'x'
        bclick = False
    elif btn["text"] == " " and bclick == False:
        btn["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1




buttons = StringVar()

myBtn1  = Button(root,text = ' ', command = lambda:uzd_6(myBtn1))

myBtn2 = Button(root,text = ' ',command = lambda:uzd_6(myBtn2))

myBtn3 = Button(root,text = ' ',command = lambda:uzd_6(myBtn3))

myBtn4 = Button(root,text = ' ',command = lambda:uzd_6(myBtn4))

myBtn5 = Button(root,text = ' ',command = lambda:uzd_6(myBtn5))

myBtn6 = Button(root,text = ' ',command = lambda:uzd_6(myBtn6))

myBtn7 = Button(root,text = ' ',command = lambda:uzd_6(myBtn7))

myBtn8 = Button(root,text = ' ',command = lambda:uzd_6(myBtn8))

myBtn9 = Button(root,text = ' ',command = lambda:uzd_6(myBtn9))
myBtn1.grid(row = 0, column = 1)
myBtn2.grid(row = 0 , column = 2)
myBtn3.grid(row = 0, column = 3)
myBtn4.grid(row = 1, column = 1)
myBtn5.grid(row = 1, column = 2)
myBtn6.grid(row = 1, column = 3)
myBtn7.grid(row = 2, column = 1)
myBtn8.grid(row = 2, column = 2)
myBtn9.grid(row = 2, column = 3)
root.mainloop()
