from tkinter import *

def onClick(event):
    print(event)
    cnv.create_line(event.x, event.y, event.x+1, event.y)
    

root = Tk()
root.geometry('500x500')


cnv = Canvas(root, bg = 'white',
             height = 400, width = 400)
cnv.bind('<Motion>', onClick)
cnv.grid(row = 0, column = 0)


root.mainloop()
