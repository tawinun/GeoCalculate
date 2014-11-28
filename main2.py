# -*- coding: cp874 -*-
from Tkinter import *
from PIL import ImageTk, Image
from math import *
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
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##Bg back
frame = Frame(root)
frame.pack()
canvas = Canvas(frame, bg="black", width=800, height=650)
canvas.pack()
photoimage = ImageTk.PhotoImage(file="C:\Python27\Cartoon-landscape-vector-background2.jpg")
canvas.create_image(400, 340, image=photoimage)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

#button quit window
def quitprogram():
    if tkMessageBox.askyesno("Quit", "You want to quit now?"):
        root.destroy()
B1 = Tkinter.Button(root, text = "Quit", command = quitprogram).place(x=745,y=10)
img_exit = PhotoImage(file="C:\Python27\Button-exit-icon.gif")
btn_exit = Button(root,bd=0, compound=CENTER, image=img_exit,cursor="X_cursor", command=quitprogram).place(x=745,y=10)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##Calculate triangle ส่วนของคำนวณสามเหลี่ยมทั้งหมด
def triangle_area(): #calculate triangle area พื้นที่สามเหลี่ยม
    NewWin_square = tk.Toplevel(root)
    NewWin_square.title('Triangle_area')
    NewWin_square.geometry('800x680')
    fields = ('base', 'height','area')
    
    def area(entries):
       base = float(entries['base'].get())
       height = float(entries['height'].get())
       area = base*height
       area = ("%.2f" % area).strip()
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


def equilateral_triangle_area(): #calculate equilateral triangle area สามเหลี่ยมด้านเท่า
    NewWin_rectangle = tk.Toplevel(root)
    NewWin_rectangle.title('Equilateral_triangle_area')
    NewWin_rectangle.geometry('800x680')
    fields = ('side','area')
    
    def area(entries):
       side = float(entries['side'].get())
       area = (sqrt(3.0)/4.0)*side*side
       area = ("%.2f" % area).strip()
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


def rightangled_triangle_area(): #calculate rightangled triangle area สามเหลี่ยมมุมฉาก    
    NewWin_paralellogram = tk.Toplevel(root)
    NewWin_paralellogram.title('Rightangled_triangle_area')
    NewWin_paralellogram.geometry('800x680')
    fields = ('cathetus1','cathetus2','area')
    
    def area(entries):
       cathetus1 = float(entries['cathetus1'].get())
       cathetus2 = float(entries['cathetus2'].get())
       area = (1.0/2.0)*cathetus1*cathetus2
       area = ("%.2f" % area).strip()
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
    NewWin_rhombus.title('Rhombus_area')
    NewWin_rhombus.geometry('800x680')
    fields = ('diagonal1','diagonal2','area')

    def area(entries):
       diagonal1 = float(entries['diagonal1'].get())
       diagonal2 = float(entries['diagonal2'].get())
       p_diagonal = diagonal1*diagonal2
       area = (1.0/2.0)*p_diagonal
       area = ("%.2f" % area).strip()
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
    NewWin_trapezium.title('Trapezium_area')
    NewWin_trapezium.geometry('800x680')
    fields = ('diagonal',' branch1', 'branch2','area')
    
    def area(entries):
       diagonal = float(entries['diagonal'].get())
       branch1 = float(entries['branch1'].get())
       branch2 = float(entries['branch2'].get())
       sum_branch = branch1+branch2
       area = (1.0/2.0)*diagonal*sum_branch
       area = ("%.2f" % area).strip()
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


##หน้าต่างใหม่ที่เลือกเมนูสามเหลี่ยมจากหน้าแรก   มีเมนูให้เลือก    
def get_new_win():
    NewWin2 = tk.Toplevel(root)
    NewWin2.title('Calculate Triangle')
    NewWin2.geometry('800x680')
    NewWin2.iconbitmap("C:\Python27\Jommans-Mushroom-Search.ico")
    canvas = Canvas(NewWin2 , bg="#CCFF66", width=800, height=650)
    canvas.pack()
        
    B1 = Tkinter.Button(NewWin2, text = "triangle_area", command = triangle_area,cursor="circle",
                        fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=100) # ปุ่มเรียก square_area
    B2 = Tkinter.Button(NewWin2, text = "equilateral_triangle_area", command = equilateral_triangle_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=170) # ปุ่มเรียก  rectangle area
    B3 = Tkinter.Button(NewWin2, text = "rightangled_triangle_area", command = rightangled_triangle_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=240) # ปุ่มเรียก paralellogram area
    B4 = Tkinter.Button(NewWin2, text = "rhombus_area", command = rhombus_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=300) # ปุ่มเรียก rhombus area
    B5 = Tkinter.Button(NewWin2, text = "trapezium_area", command = trapezium_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=370) # ปุ่มเรียก trapezium
    
img_good = PhotoImage(file="C:\Python27\Triangle.gif")
btn = Button(root,bd=0, compound=CENTER, image=img_good,cursor="X_cursor", command=get_new_win).place(x=82,y=500)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##Calculate Squre ส่วนของคำนวณสี่เหลี่ยมทั้งหมด
def square_area():  #calculate square area สี่เหลี่ยมด้านเท่า
    NewWin_square = tk.Toplevel(root)
    NewWin_square.title('Square_area')
    NewWin_square.geometry('800x680')
    fields = ('side','area')

    def area(entries):
       side = float(entries['side'].get())
       area = side**2
       area = ("%.2f" % area).strip()
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
    NewWin_rectangle.title('Rectangle_area')
    NewWin_rectangle.geometry('800x680')
    fields = ('width','height','area')

    def area(entries):
       width = float(entries['width'].get())
       height = float(entries['height'].get())
       area = width*height
       area = ("%.2f" % area).strip()
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
    NewWin_paralellogram.title('Paralellogram_area')
    NewWin_paralellogram.geometry('800x680')
    fields = ('base','height','area')
    
    def area(entries):
       base = float(entries['base'].get())
       height = float(entries['height'].get())
       area = base*height
       area = ("%.2f" % area).strip()
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
    NewWin_rhombus.title('Rhombus_area')
    NewWin_rhombus.geometry('800x680')
    fields = ('diagonal1','diagonal2','area')

    def area(entries):
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
    NewWin_trapezium.title('Trapezium_area')
    NewWin_trapezium.geometry('800x680')
    fields = ('diagonal','branch1', 'branch2','area')

    def area(entries):
       diagonal = float(entries['diagonal'].get())
       branch1 = float(entries['branch1'].get())
       branch2 = float(entries['branch2'].get())
       sum_branch = branch1+branch2
       area = (1.0/2.0)*diagonal*sum_branch
       area = ("%.2f" % area).strip()
       entries['area'].delete(0,END)
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

def kite_area():   #calculate rhombus area สี่เหลี่ยมรูปว่าว
    NewWin_rhombus = tk.Toplevel(root)
    NewWin_rhombus.title('Kite_area')
    NewWin_rhombus.geometry('800x680')
    fields = ('diagonal1','diagonal2','area')

    def area(entries):
       diagonal1 = float(entries['diagonal1'].get())
       diagonal2 = float(entries['diagonal2'].get())
       p_diagonal = diagonal1*diagonal2
       area = (1.0/2.0)*p_diagonal
       area = ("%.2f" % area).strip()
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

def cube_volume():   #calculate cube_volume ปริมาตรลูกบาสก์
    NewWin_trapezium = tk.Toplevel(root)
    NewWin_trapezium.title('Volume')
    NewWin_trapezium.geometry('800x680')
    fields = ('side','volume')

    def volume(entries):
       side = float(entries['side'].get())
       volume = side**3
       volume = ("%.2f" % volume).strip()
       entries['volume'].insert(0, volume )
       print("volume:" ,volume)

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
       b2 = Button(NewWin_trapezium, text='Volume',command=(lambda e=ents: volume(e)))
       b2.pack(side=LEFT, padx=5, pady=5)     

##หน้าต่างใหม่ที่เลือกเมนูสี่เหลี่ยมจากหน้าแรก   มีเมนูให้เลือก    
def get_new_win():
    NewWin2 = tk.Toplevel(root)
    NewWin2.title('Calculate Squre')
    NewWin2.geometry('800x680')
    NewWin2.iconbitmap("C:\Python27\Jommans-Mushroom-Search.ico")
    canvas = Canvas(NewWin2 , bg="#99FF99", width=800, height=650)
    canvas.pack()
    
    B1 = Tkinter.Button(NewWin2, text = "square_area", command = square_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=100) # ปุ่มเรียก square_area
    B2 = Tkinter.Button(NewWin2, text = "rectangle_area", command = rectangle_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=170) # ปุ่มเรียก  rectangle area
    B3 = Tkinter.Button(NewWin2, text = "sparalellogram_area", command = paralellogram_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=240) # ปุ่มเรียก paralellogram area
    B4 = Tkinter.Button(NewWin2, text = "rhombus_area", command = rhombus_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=300) # ปุ่มเรียก rhombus area
    B5 = Tkinter.Button(NewWin2, text = "trapezium_area", command = trapezium_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=370) # ปุ่มเรียก trapezium
    B6 = Tkinter.Button(NewWin2, text = "kite_area", command = kite_area,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=440) # ปุ่มเรียก trapezium
    B7 = Tkinter.Button(NewWin2, text = "cube_volume", command = cube_volume,cursor="circle",
                         fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=500) # ปุ่มเรียก cube_volume
    
img_good2 = PhotoImage(file="C:\Python27\Square.gif")
btn2 = Button(root,bd=0, compound=CENTER, image=img_good2,cursor="X_cursor", command=get_new_win).place(x=310,y=500)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##


##Calculate cricle ส่วนของคำนวณวงกลมทั้งหมด

def circle_area(): #calculate circle_area พื้นที่วงกลม
    NewWin_square = tk.Toplevel(root)
    NewWin_square.title('Circle_area')
    NewWin_square.geometry('800x680')
    fields = ('radian','area','circumference')

    def area(entries):
       radian = float(entries['radian'].get())
       print("radian", radian)
       area = pi*(radian**2)
       area = ("%.2f" % area).strip()
       entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)
    def circumference(entries): #เส้นรอบวง
        radian = float(entries['radian'].get())
        print("radian", radian)
        circumference = 2.0*pi*radian
        circumference = ("%.2f" %circumference ).strip()
        entries['circumference'].insert(0, circumference )
        entries['circumference'].delete(0,END)
        entries['circumference'].insert(0, circumference )
        print("circumference:" ,circumference)
        
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
       b3 = Button(NewWin_square, text='Circumference',command=(lambda e=ents: circumference(e)))
       b3.pack(side=LEFT, padx=5, pady=5)


def circle_surface_area(): #calculate sphere_surface_area พื้นที่ผิววงกลม
    NewWin_rectangle = tk.Toplevel(root)
    NewWin_rectangle.title('Circle_surface_area')
    NewWin_rectangle.geometry('800x680')
    fields = ('radian','area')
    
    def area(entries):
       radian = float(entries['radian'].get())
       area = 4.0*pi*(radian**2)
       area = ("%.2f" % area).strip()
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

def cylinder_surface_area():#calculate cylinder_surfaceside_area  พื้นที่ผิวทรงกระบอก    
    NewWin_paralellogram = tk.Toplevel(root)
    NewWin_paralellogram.title('Cylinder_area')
    NewWin_paralellogram.geometry('800x680')
    fields =('radian','height','area','surfaceside')
    
    def area(entries):
       radian = float(entries['radian'].get())
       height = float(entries['height'].get())
       area = (2.0*pi*radian*height)+(2.0*pi*(radian**2))
       area = ("%.2f" % area).strip()
       entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)
    def surfaceside(entries): #พื้นที่ผิวข้างกระบอก
        radian = float(entries['radian'].get())
        height = float(entries['height'].get())
        surfaceside = 2.0*pi*radian*height
        surfaceside = ("%.2f" % surfaceside).strip()
        entries['surfaceside'].delete(0,END)
        entries['surfaceside'].insert(0, surfaceside )
        print("surfaceside:", surfaceside)
        
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
       b3 = Button(NewWin_paralellogram, text='surfaceside',command=(lambda e=ents: surfaceside(e)))
       b3.pack(side=LEFT, padx=5, pady=5)


def cone_surface_area():#calculate cylinder_surfaceside_area  พื้นที่ผิวทรงกรวย    
    NewWin_paralellogram = tk.Toplevel(root)
    NewWin_paralellogram.title('Cone_surface_area')
    NewWin_paralellogram.geometry('800x680')
    fields =('radian','lenght','area','surfaceside')

    def area(entries):
       radian = float(entries['radian'].get())
       lenght = float(entries['lenght'].get())
       area = (pi*radian*lenght)+(pi*(radian**2))
       area = ("%.2f" % area).strip()
       entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)
    def surfaceside(entries): #พื้นที่ผิวข้างกรวย
        radian = float(entries['radian'].get())
        lenght = float(entries['lenght'].get())
        surfaceside = pi*radian*lenght
        surfaceside = ("%.2f" % surfaceside).strip()
        entries['surfaceside'].delete(0,END)
        entries['surfaceside'].insert(0, surfaceside )
        print("surfaceside:", surfaceside)
        
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
       b3 = Button(NewWin_paralellogram, text='surfaceside',command=(lambda e=ents: surfaceside(e)))
       b3.pack(side=LEFT, padx=5, pady=5)
       
def sphere_volume():#calculate sphere_volume ปริมาตรทรงกลม
    NewWin_paralellogram = tk.Toplevel(root)
    NewWin_paralellogram.title('Volume')
    NewWin_paralellogram.geometry('800x680')
    fields =('radian','height','volume','cylinder_volume','cone_volume')
    
    def volume(entries):
       radian = float(entries['radian'].get())
       volume = (4.0/3.0)*pi*(radian**3)
       volume = ("%.2f" % volume).strip()
       entries['volume'].delete(0,END)
       entries['volume'].insert(0,volume )
       print("volume:" , volume)
    def cylinder_volume(entries):# ปริมาตรทรงกระบอก
        radian = float(entries['radian'].get())
        height = float(entries['height'].get())
        cylinder_volume = pi*(radian**2)*height
        cylinder_volume = ("%.2f" % cylinder_volume).strip()
        entries['cylinder_volume'].delete(0,END)
        entries['cylinder_volume'].insert(0, cylinder_volume)
        print("cylinder_volume:", cylinder_volume)
    def cone_volume(entries):#ปริมาตรทรงกรวย
        radian = float(entries['radian'].get())
        height = float(entries['height'].get())
        cone_volume = (1.0/3)*pi*(radian**2)*height
        cone_volume = ("%.2f" % cone_volume).strip()
        entries['cone_volume'].delete(0,END)
        entries['cone_volume'].insert(0, cone_volume)
        print("cone_volume:", cone_volume)
        
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
       b2 = Button(NewWin_paralellogram, text='Volume',command=(lambda e=ents: volume(e)))
       b2.pack(side=LEFT, padx=5, pady=5)
       b2 = Button(NewWin_paralellogram, text='cylinder_volume',command=(lambda e=ents: cylinder_volume(e)))
       b2.pack(side=LEFT, padx=5, pady=5)
       b2 = Button(NewWin_paralellogram, text='cone_volume',command=(lambda e=ents: cone_volume(e)))
       b2.pack(side=LEFT, padx=5, pady=5)

##หน้าต่างใหม่ที่เลือกเมนูสามเหลี่ยมจากหน้าแรก   มีเมนูให้เลือก    
def get_new_win():
    NewWin2 = tk.Tk()
    NewWin2.title('Calculate Circle')
    NewWin2.geometry('800x680')
    NewWin2.iconbitmap("C:\Python27\Jommans-Mushroom-Search.ico")
    canvas = Canvas(NewWin2 , bg="#66FFCC", width=800, height=650)
    canvas.pack()
##    FILENAME = 'C:\Python27\img18.gif'
##    canvas = tk.Canvas( NewWin2, width=700, height=600)
##    canvas.pack()
##    tk_img = ImageTk.PhotoImage(file = FILENAME)
##    canvas.create_image(125, 125, image=tk_img)
    
    B1 = Tkinter.Button(NewWin2, text = "circle_area", command = circle_area,cursor="circle",
                        fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=100) # ปุ่มเรียก circle_area
    B2 = Tkinter.Button(NewWin2, text = "circle_surface_area", command = circle_surface_area,cursor="circle",
                        fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=170) # ปุ่มเรียก  circle_surface_area
    B3 = Tkinter.Button(NewWin2, text = "cylinder_surface_area", command = cylinder_surface_area,cursor="circle",
                        fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=240) # ปุ่มเรียก cylinder_surface_area
    B4 = Tkinter.Button(NewWin2, text = "cone_surface_area", command = cone_surface_area,cursor="circle",
                        fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=310) # ปุ่มเรียก cone_surface_area
    B5 = Tkinter.Button(NewWin2, text = "sphere_volume", command = sphere_volume,cursor="circle",
                        fg="white",bg="#00CC99",font=("Helvetica", 16)).place(x=400,y=360) # ปุ่มเรียก sphere_volume 
    
img_good3 = PhotoImage(file="C:\Python27\Circle.gif")
btn3 = Button(root,bd=0, compound=CENTER, image=img_good3,cursor="X_cursor", command=get_new_win).place(x=551,y=500)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

root.mainloop()
