from random import choice
from tkinter import *
def l():
    L = ['1980','2006', '1979', '1953', '0000', '2491']
    word = choice(L)
    return (word)
st0 = l()
print ("правила! с лево в  белом углу находится быки, те которые правельно расположены на своем месте, с лева, коровы, это правельная цифра но стоит она на в другом порядке! желтым обозначено число попыток ")
def uzd_5():
    global bulls
    global cows
    global num
    global st0

 

    if bulls != 4:
         
        while True:
            print(u'nomer popitki: ',num)
            st = myEntry.get()
            num = num+ 1
            ls = list(st)
            ls0 = list(st0)

            bulls = 0
            for j in range(4):
                if ls[j] == ls0[j]:
                    bulls +=1;
                    ls[j] = ' ';
                    ls0[j] = '*';
      
            break
        cows = 0
        for j in range (4):
            n = ls[j]
            for k in range(4):
                if n == ls0[k]:
                    cows = cows+1
                    ls0[k] = "*";
    if bulls == 4:
        print('вы угадали!')            
    print ("быков",bulls)
    print ("коров",cows)
    wordLabel2.config(text = cows)
    wordLabel1.config(text = bulls)
    wordLabelh.config(text = num)
num = 0
bulls = 0
cows = 0
def delText():
    myEntry.delete(first = 0,
                   last = 'end')
             
root = Tk()
root.geometry('500x500')
btnDel = Button(root,height=2, width=20,text = 'очистить',command = delText)
btnGet = Button(root,height=2, width=20,text = 'получить',command = uzd_5)
myEntry = Entry(root,bd = 10)
wordLabel1 = Label(root,bg = '#ffffff',height=2, width=20, font=10,text = bulls)
wordLabel2 = Label(root,bg = '#ffffff',height=2, width=20, font=10,text = cows)
wordLabelh = Label(root,bg = 'yellow',height=2, width=5,text = cows )
wordLabelh.grid(row=1, column=1)
wordLabel2.grid(row=0, column=1)
wordLabel1.grid(row=0, column=0)
myEntry.grid(row=1, column=0)
btnDel.grid(row = 20, column = 0)
btnGet.grid(row = 10,column = 0)
root.mainloop()
