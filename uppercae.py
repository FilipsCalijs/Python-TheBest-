from tkinter import *

def changeCase():
    if option.get() == 1:
        text = myEntry.get()
        text = text.lower()
        myEntry.delete(first = 0, last = "end")
        myEntry.insert(0, text)

    if option.get() == 2:
        text = myEntry.get()
        text = text.upper()
        myEntry.delete(first = 0, last = "end")
        myEntry.insert(0, text)
    if option.get() == 3:
        text = myEntry.get()
        text = text.capitalize()
        myEntry.delete(first = 0, last = "end")
        myEntry.insert(0, text)
    if option.get() == 4:
        
        text = myEntry.get()
        text = text.capitalize()
        myEntry.delete(first = 0, last = "end")
        myEntry.insert(0, text)
                

root = Tk()
root.geometry('500x500')

myEntry = Entry(root)
myEntry.grid(row = 0,column = 0)

option = IntVar()
rb1 = Radiobutton(root, text = 'lowercase', variable = option, value = 1)
rb2 = Radiobutton(root, text = 'UPPERCASE', variable = option, value = 2)
rb3 = Radiobutton(root, text = 'Sentence case', variable = option, value = 3)
rb4 = Radiobutton(root, text = 'Capitalize Each Word', variable = option, value = 4)
rb5 = Radiobutton(root, text = 'tOGGLE cASE', variable = option, value = 5)

rb1.grid(row = 1,column = 0)
rb2.grid(row = 2,column = 0)
rb3.grid(row = 3,column = 0)
rb4.grid(row = 4,column = 0)
rb5.grid(row = 5,column = 0)

btn = Button(root, text = 'change case', command = changeCase)
btn.grid(row = 6, column = 0)
root.mainloop()
