from tkinter import *

x = 0
y = 0
toggle = False
def onClick(event):
    global x, y, toggle
    if toggle == 0:
        x = event.x
        y = event.y
    else:
        cnv.create_rectangle(x,y, event.x, event.y, fill = 'red')
    toggle = not toggle
    
        

root = Tk()
root.geometry('500x500')


cnv = Canvas(root, bg = 'black',
             height = 400, width = 400)
cnv.bind('<Button>', onClick)
cnv.grid(row = 0, column = 0)


root.mainloop()
