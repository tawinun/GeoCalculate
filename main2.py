# -*- coding: cp874 -*-
from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import Tkinter
import ttk
import ImageTk
import Tkinter as tk

#cursor
root = Tkinter.Tk()
root.geometry('800x680+10+6')
root.title("My Window")
root.iconbitmap("C:\Python27\Jommans-Mushroom-Search.ico")

##canvas = Canvas(width = 600, height = 600, bg = 'white')
##canvas.pack(expand = YES, fill = BOTH,side='top')
##----------------------------------------------------


##Bg back
frame = Frame(root)
frame.pack()
canvas = Canvas(frame, bg="black", width=800, height=650)
canvas.pack()
photoimage = ImageTk.PhotoImage(file="C:\Python27\Cartoon-landscape-vector-background2.jpg")
canvas.create_image(400, 340, image=photoimage)
##----------------------------------------------------



#button quit
def quitprogram():
    if tkMessageBox.askyesno("Quit", "You want to quit now?"):
        root.destroy()
B1 = Tkinter.Button(root, text = "Quit", command = quitprogram).place(x=745,y=10)
img_exit = PhotoImage(file="C:\Python27\Button-exit-icon.gif")
btn_exit = Button(root,bd=0, compound=CENTER, image=img_exit,cursor="X_cursor", command=quitprogram).place(x=745,y=10)


##----------------------------------------------------

##Calculate triangle
def new_win_():

    NewWin_r = tk.Toplevel(root)
    NewWin_r.title('triangle')
    NewWin_r.geometry('800x680')
def get_new_win():

    NewWin = tk.Toplevel(root)
    NewWin.title('triangle')
    NewWin.geometry('800x680')
    NewWin.iconbitmap("C:\Python27\Jommans-Mushroom-Search.ico")
    B1 = Tkinter.Button(NewWin, text = "Quit", command = get_new_win_r).place(x=745,y=10)

####    img_exit = PhotoImage(file="C:\Python27\animated.gif")
####    B1 = Tkinter.Button(NewWin,bd=0,compound=CENTER, image=img_exit).place(x=745,y=10)
##
##      
####    fields = ('base', 'height','radiau' 'area')
####
####    def area(entries):
####
####   # principal loan:
####       base = float(entries['base'].get())
####       height =  float(entries['height'].get())
####       radiau = float(entries['radiau'].get())
####   
####       area = 1.0/2.0*base*height
####       area = ("%.2f" % area).strip()
####    ##   entries['area'].delete(0,END)
####       entries['area'].insert(0, area )
####       print("area:" ,area)
####
####    def makeform(NewWin, fields):
####       entries = {}
####       for field in fields:
####          row = Frame(NewWin)
####          lab = Label(row, width=22, text=field+": ", anchor='w')
####          ent = Entry(row)
####          ent.insert(0,"0")
####          row.pack(side=TOP, fill=X, padx=5, pady=5)
####          lab.pack(side=LEFT)
####          ent.pack(side=RIGHT, expand=YES, fill=X)
####          entries[field] = ent
####       return entries
####
####    if __name__ == '__main__':
####       ents = makeform(NewWin, fields)
####       NewWin.bind('<Return>', (lambda event, e=ents: fetch(e)))   
####       b2 = Button(NewWin, text='Area',command=(lambda e=ents: area(e)))
####       b2.pack(side=LEFT, padx=5, pady=5)
####       b3 = Button(NewWin, text='Area3')
####       b3.pack(side=LEFT, padx=5, pady=5)
####       
####       
####    
######quit window
####    def quit_win():
####        NewWin.destroy()
####        
####
####    QuitButton = tk.Button(NewWin,text='Quit',command=quit_win)
####    QuitButton.pack(side=LEFT, padx=5, pady=5)
####    NewWin.protocol("WM_DELETE_WINDOW", quit_win)
    
img_good = PhotoImage(file="C:\Python27\Triangle.gif")
btn = Button(root,bd=0, compound=CENTER, image=img_good,cursor="X_cursor", command=get_new_win).place(x=82,y=500)




##Calculate Squre
def square_area():  #calculate square area สี่เหลี่ยมด้า่นเท่า

    NewWin_square = tk.Toplevel(root)
    NewWin_square.title('square_area')
    NewWin_square.geometry('800x680')
    fields = ('side','area')

    def area(entries):
   # period rate:

   # principal loan:
       side = float(entries['side'].get())

       area = side**2
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin_square, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin_square)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin_square, fields)
       NewWin_square.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin_square, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)


def rectangle_area(): #calculate rectangle area สีเหลี่ยมผืนผ้า

    NewWin_rectangle = tk.Toplevel(root)
    NewWin_rectangle.title('rectangle_area')
    NewWin_rectangle.geometry('800x680')
    fields = ('width','height','area')

    def area(entries):
   # period rate:

   # principal loan:
       width = float(entries['width'].get())
       height = float(entries['height'].get())

       area = width*height
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin_rectangle, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin_rectangle)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin_rectangle, fields)
       NewWin_rectangle.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin_rectangle, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)

def paralellogram_area(): #calculate paralellogram area สี่เหลี่ยมด้านขนาน
    
    NewWin_paralellogram = tk.Toplevel(root)
    NewWin_paralellogram.title('paralellogram_area')
    NewWin_paralellogram.geometry('800x680')
    fields = ('base','height','area')
    
    def area(entries):
   # period rate:

   # principal loan:
       base = float(entries['base'].get())
       height = float(entries['height'].get())

       area = base*height
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin_paralellogram, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin_paralellogram)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin_paralellogram, fields)
       NewWin_paralellogram.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin_paralellogram, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)

def rhombus_area():   #calculate rhombus area สี่เหลี่ยมเปียกปูน

    NewWin_rhombus = tk.Toplevel(root)
    NewWin_rhombus.title('square_area')
    NewWin_rhombus.geometry('800x680')
    fields = ('diagonal1','diagonal2','area')

    def area(entries):
   # period rate:

   # principal loan:
       diagonal1 = float(entries['diagonal1'].get())
       diagonal2 = float(entries['diagonal2'].get())
       p_diagonal = diagonal1*diagonal2
       area = (1.0/2.0)*p_diagonal
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin_rhombus, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin_rhombus)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin_rhombus, fields)
       NewWin_rhombus.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin_rhombus, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)

def trapezium_area():   #calculate trapezium area คางหมู

    NewWin_trapezium = tk.Toplevel(root)
    NewWin_trapezium.title('square_area')
    NewWin_trapezium.geometry('800x680')
    fields = ('diagonal',' branch1', 'branch2','area')
    
    def area(entries):
   # period rate:

   # principal loan:
       diagonal = float(entries['diagonal'].get())
       branch1 = float(entries['branch1'].get())
       branch2 = float(entries['branch2'].get())
       sum_branch = branch1+branch2
       area = (1.0/2.0)*diagonal*sum_branch
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin_trapezium, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin_trapezium)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin_trapezium, fields)
       NewWin_trapezium.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin_trapezium, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)       


##หน้าต่างใหม่ที่เลือกเมนูสี่เหลี่ยมจากหน้าแรก   มีเมนูให้เลือก    
def get_new_win():
    NewWin2 = tk.Toplevel(root)
    NewWin2.title('Calculate Squre')
    NewWin2.geometry('800x680')
    NewWin2.iconbitmap("C:\Python27\Jommans-Mushroom-Search.ico")
    

    B1 = Tkinter.Button(NewWin2, text = "square_area", command = square_area).place(x=400,y=100) # ปุ่มเรียก square_area
    B2 = Tkinter.Button(NewWin2, text = "rectangle_area", command = rectangle_area).place(x=400,y=130) # ปุ่มเรียก  rectangle area
    B3 = Tkinter.Button(NewWin2, text = "sparalellogram_area", command = paralellogram_area).place(x=400,y=170) # ปุ่มเรียก paralellogram area
    B4 = Tkinter.Button(NewWin2, text = "rhombus_area", command = rhombus_area).place(x=400,y=200) # ปุ่มเรียก rhombus area
    B5 = Tkinter.Button(NewWin2, text = "trapezium_area", command = trapezium_area).place(x=400,y=230) # ปุ่มเรียก trapezium
##  
    
##button image
img_good2 = PhotoImage(file="C:\Python27\Square.gif")
btn2 = Button(root,bd=0, compound=CENTER, image=img_good2,cursor="X_cursor", command=get_new_win).place(x=310,y=500)



##Calculate cricle

def get_new_win():

    NewWin3 = tk.Toplevel(root)
    NewWin3.title('Circle')
    NewWin3.geometry('400x400')
    fields = ('radius','area')

    def area(entries):
   # period rate:

   # principal loan:
       base = float(entries['radius'].get())

       area = 3.14*(base**2)
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin3, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin3)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin3, fields)
       NewWin3.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin3, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)
       
    
##quit window
    def quit_win():
        NewWin3.destroy()
        

    QuitButton = tk.Button(NewWin3,text='Quit',command=quit_win)
    QuitButton.pack(side=LEFT, padx=5, pady=5)
    NewWin3.protocol("WM_DELETE_WINDOW", quit_win)    
##NewWinButton = tk.Button(root,text='Circle',cursor="X_cursor", command=get_new_win).place(x=610,y=530)
##
img_good3 = PhotoImage(file="C:\Python27\Circle.gif")
btn3 = Button(root,bd=0, compound=CENTER, image=img_good3,cursor="X_cursor", command=get_new_win).place(x=551,y=500)


root.mainloop()
