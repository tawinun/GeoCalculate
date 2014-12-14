# -*- coding: cp874 -*-
from Tkinter import *
from PIL import ImageTk, Image
from math import *
import tkMessageBox
import Tkinter
import ttk
import ImageTk
import Tkinter as tk

root = Tkinter.Tk()
root.geometry('800x680+235+8')
root.title("GeoCalculatE")
root.iconbitmap("Home.ico")
frame = Frame(root)
frame.pack()
canvas = Canvas(frame, bg = "black", width = 800, height = 650)
canvas.pack()
photoimage = ImageTk.PhotoImage(file = "Cartoon-bg.jpg")
canvas.create_image(400, 340, image = photoimage)

def quitprogram():
    """quit program button"""
    if tkMessageBox.askyesno("Quit", "You want to quit now?"):
        root.destroy()
img_exit = PhotoImage(file = "action_exit.gif")
btn_exit = Button(root, bd = 0, compound = CENTER, image = img_exit, cursor = "X_cursor", command = quitprogram).place(x = 745, y = 2)

#The calculation of triangles
def triangle_area():
    """the area of triangle"""
    NewWin_triangle = tk.Toplevel(root)
    NewWin_triangle.title('Triangle_area')
    NewWin_triangle.geometry('800x680+235+8')
    NewWin_triangle.iconbitmap("Femfoyou.ico")
    fields = ('Base', 'Height', 'Area')
    def area(entries):
        base = float(entries['Base'].get())
        height = float(entries['Height'].get())
        area = base * height
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_triangle, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_triangle, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#FF4500", text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side=TOP,padx=5, pady=5)
            lab.pack(side=TOP)
            ent.pack(side=RIGHT, expand=YES, fill=BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_, fields)
        NewWin_triangle.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_triangle, text = 'Area',fg = "white", bg = "#FF9900", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 200)
             
def equilateral_triangle_area():
    """the area of equilateral triangle"""
    NewWin_equilateral = tk.Toplevel(root)
    NewWin_equilateral.title('Equilateral_triangle_area')
    NewWin_equilateral.geometry('800x680+235+8')
    NewWin_equilateral.iconbitmap("Femfoyou.ico")
    fields = ('Side', 'Area')
    def area(entries):
        side = float(entries['Side'].get())
        area = (sqrt(3.0) / 4.0) * (side**2)
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area)
    def makeform(NewWin_equilateral, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_equilateral, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#FF4500", text = field + " : ", anchor = 'w')
            row.pack_propagate(0) 
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5) 
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_equilateral, fields)
        NewWin_equilateral.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_equilateral, text = 'Area', fg = "white", bg = "#FF9900", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 160)

def rightangled_triangle_area():
    """the area of right-angled triangle"""    
    NewWin_rightangled = tk.Toplevel(root)
    NewWin_rightangled.title('Rightangled_triangle_area')
    NewWin_rightangled.geometry('800x680+235+8')
    NewWin_rightangled.iconbitmap("Femfoyou.ico")
    fields = ('Cathetus1', 'Cathetus2', 'Area')
    def area(entries):
        cathetus1 = float(entries['Cathetus1'].get())
        cathetus2 = float(entries['Cathetus2'].get())
        area = (1.0 / 2.0) * cathetus1 * cathetus2
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_rightangled, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_rightangled, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#FF4500", text = field + " : ", anchor = 'w')
            row.pack_propagate(0) 
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5) 
            lab.pack(side = TOP) 
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_rightangled, fields)
        NewWin_rightangled.bind('<Return>', (lambda event, e = ents: fetch(e)))   
        b2 = Button(NewWin_rightangled, text = 'Area', fg = "white", bg = "#FF9900", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 200)

def Isosceles_area():
    """the area of Isosceles Triangles"""
    NewWin_Isosceles = tk.Toplevel(root)
    NewWin_Isosceles.title('Isosceles_area')
    NewWin_Isosceles.geometry('800x680+235+8')
    NewWin_Isosceles.iconbitmap("Femfoyou.ico")
    fields = ('Leg1', 'Leg2', 'Base', 'Area')
    def area(entries):
        leg1 = float(entries['Leg1'].get())
        leg2 = float(entries['Leg1'].get())
        base = float(entries['Base'].get())
        area = (base / 4.0) * sqrt((4.0 * leg2 **2) - (leg1**2))
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area)
    def makeform(NewWin_Isosceles, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_Isosceles, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#FF4500" , text = field + " : ", anchor = 'w')
            row.pack_propagate(0) 
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5) 
            lab.pack(side = TOP) 
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_Isosceles, fields)
        NewWin_Isosceles.bind('<Return>', (lambda event, e=ents: fetch(e)))
        b2 = Button(NewWin_Isosceles, text = 'Area', fg = "white", bg = "#FF9900", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 260)
            
#new window for select tritangle menu    
def get_new_win():
    """open new window"""
    NewWin2 = tk.Toplevel(root)
    NewWin2.title('Calculate Triangle')
    NewWin2.geometry('800x680+235+8')
    NewWin2.iconbitmap("Jommans-Mushroom-Search.ico")
    #button menu
    btn1 = Button(NewWin2, bd = 0, compound = CENTER, image = img_b1, cursor = "circle",
                  command = triangle_area).place(x= 180, y = 130) # call triangle_area
    btn2 = Button(NewWin2, bd = 0, compound = CENTER, image = img_b2, cursor = "circle",
                  command = equilateral_triangle_area).place(x = 420, y = 130) # call equilateral_triangle_area
    btn3 = Button(NewWin2, bd = 0, compound = CENTER, image = img_b3, cursor = "circle",
                  command = rightangled_triangle_area).place(x = 160, y = 330) # call rightangled_triangle_area
    btn4 = Button(NewWin2, bd = 0, compound = CENTER, image = img_b4, cursor = "circle",
                  command = Isosceles_area).place(x = 440, y = 330) # call Isosceles_area
    btn5 = Button(NewWin2, bd = 0, compound = CENTER, image = img_bg).place(x = 75, y = 540)
    btn6 = Button(NewWin2, bd = 0, compound = CENTER, image = img_bg2).place(x = 185, y = 10)
img_b1 = PhotoImage(file = "Triangle_1.gif")
img_b2 = PhotoImage(file = "Triangle_2.gif")
img_b3 = PhotoImage(file = "Triangle_3.gif")
img_b4 = PhotoImage(file = "Triangle_4.gif")
img_bg = PhotoImage(file = "line1.gif")
img_bg2 = PhotoImage(file = "menu_tri.gif")
img_good = PhotoImage(file = "Triangle.gif")    
btn = Button(root, bd = 0, compound = CENTER, image = img_good, cursor = "X_cursor", command = get_new_win).place(x = 82, y = 500)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

#The calculation of squre
def square_area():
    """the area of square"""
    NewWin_square = tk.Toplevel(root)
    NewWin_square.title('Square_area')
    NewWin_square.geometry('800x680+235+8')
    NewWin_square.iconbitmap("Femfoyou.ico")
    fields = ('Side', 'Area')
    def area(entries):
        side = float(entries['Side'].get())
        area = side ** 2
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_square, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_square, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#D15FEE", text = field + " : ", anchor = 'w')
            row.pack_propagate(0) 
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_square, fields)
        NewWin_square.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_square, text = 'Area' ,fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 160)

def rectangle_area():
    """the area of rectangle"""
    NewWin_rectangle = tk.Toplevel(root)
    NewWin_rectangle.title('Rectangle_area')
    NewWin_rectangle.geometry('800x680+235+8')
    NewWin_rectangle.iconbitmap("Femfoyou.ico")
    fields = ('Width', 'Height', 'Area')
    def area(entries):
        width = float(entries['Width'].get())
        height = float(entries['Height'].get())
        area = width * height
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_rectangle, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_rectangle, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13),fg = "#D15FEE", text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP) 
            ent.pack(side = RIGHT, expand  =YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_rectangle, fields)
        NewWin_rectangle.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_rectangle, text = 'Area', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e=ents: area(e))).place(x = 360, y = 200)

def parallelogram_area():
    """the area of parallelogram"""
    NewWin_parallelogram = tk.Toplevel(root)
    NewWin_parallelogram.title('Paralellogram_area')
    NewWin_parallelogram.geometry('800x680+235+8')
    NewWin_parallelogram.iconbitmap("Femfoyou.ico")
    fields = ('Base', 'Height', 'Area')
    def area(entries):
        base = float(entries['Base'].get())
        height = float(entries['Height'].get())
        area = base * height
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_parallelogram, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_parallelogram, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#D15FEE", text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_parallelogram, fields)
        NewWin_parallelogram.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_parallelogram, text = 'Area', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 200)

def rhombus_area():
    """the area of rhombus"""
    NewWin_rhombus = tk.Toplevel(root)
    NewWin_rhombus.title('Rhombus_area')
    NewWin_rhombus.geometry('800x680+235+8')
    NewWin_rhombus.iconbitmap("Femfoyou.ico")
    fields = ('Diagonal1', 'Diagonal2', 'Area')
    def area(entries):
        diagonal1 = float(entries['Diagonal1'].get())
        diagonal2 = float(entries['Diagonal2'].get())
        p_diagonal = diagonal1*diagonal2
        area = (1.0 / 2.0) * p_diagonal
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_rhombus, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_rhombus, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#D15FEE", text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_rhombus, fields)
        NewWin_rhombus.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_rhombus, text = 'Area', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command=(lambda e = ents: area(e))).place(x = 360, y = 200)

def trapezium_area():
    """the area of trapezium"""
    NewWin_trapezium = tk.Toplevel(root)
    NewWin_trapezium.title('Trapezium_area')
    NewWin_trapezium.geometry('800x680+235+8')
    NewWin_trapezium.iconbitmap("Femfoyou.ico")
    fields = ('Diagonal', 'Branch1', 'Branch2', 'Area')
    def area(entries):
        diagonal = float(entries['Diagonal'].get())
        branch1 = float(entries['Branch1'].get())
        branch2 = float(entries['Branch2'].get())
        sum_branch = branch1+branch2
        area = (1.0 / 2.0) * diagonal * sum_branch
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_trapezium, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_trapezium, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#D15FEE" , text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_trapezium, fields)
        NewWin_trapezium.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_trapezium, text = 'Area', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 260)

def kite_area():
    """the area of rectangular shaped kites"""
    NewWin_kite = tk.Toplevel(root)
    NewWin_kite.title('Kite_area')
    NewWin_kite.geometry('800x680+235+8')
    NewWin_kite.iconbitmap("Femfoyou.ico")
    fields = ('Diagonal1', 'Diagonal2', 'Area')
    def area(entries):
        diagonal1 = float(entries['Diagonal1'].get())
        diagonal2 = float(entries['Diagonal2'].get())
        p_diagonal = diagonal1 * diagonal2
        area = (1.0 / 2.0) * p_diagonal
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_kite, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_kite, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#D15FEE", text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_kite, fields)
        NewWin_kite.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_kite, text = 'Area', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 200)
       
def cuboid_volume():
    """the area of cuboid volume"""
    NewWin_cuboid = tk.Toplevel(root)
    NewWin_cuboid.title('Volume')
    NewWin_cuboid.geometry('800x680+235+8')
    NewWin_cuboid.iconbitmap("Femfoyou.ico")
    fields = ('Width', 'Length', 'Height', 'Volume')
    def volume(entries):
        width = float(entries['Width'].get())
        length = float(entries['Length'].get())
        height = float(entries['Height'].get())
        volume = width * length * height
        volume = ("%.2f" % volume).strip()
        entries['Volume'].delete(0,END)
        entries['Volume'].insert(0, volume )
    def makeform(NewWin_cuboid, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_cuboid, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#D15FEE", text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side=TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_cuboid, fields)
        NewWin_cuboid.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_cuboid, text = 'Volume', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: volume(e))).place(x = 360, y = 260)

def cube_volume():
    """the area of cube volume"""
    NewWin_cube = tk.Toplevel(root)
    NewWin_cube.title('Volume')
    NewWin_cube.geometry('800x680+235+8')
    NewWin_cube.iconbitmap("Femfoyou.ico")
    fields = ('Side', 'Volume')
    def volume(entries):
        side = float(entries['Side'].get())
        volume = side ** 3
        volume = ("%.2f" % volume).strip()
        entries['Volume'].delete(0,END)
        entries['Volume'].insert(0, volume )
    def makeform(NewWin_cube, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_cube, width = 140, height = 50)
            lab = Label(row, width  =22, font = ("Helvetica", 13), fg = "#D15FEE" , text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify='center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_cube, fields)
        NewWin_cube.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_cube, text = 'Volume', fg = "white", bg = "#CC66FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: volume(e))).place(x = 360, y = 160)    

#new window for select squre menu   
def get_new_win():
    NewWin2 = tk.Toplevel(root)
    NewWin2.title('Calculate Squre')
    NewWin2.geometry('800x680+235+8')
    NewWin2.iconbitmap("Jommans-Mushroom-Search.ico")
    canvas = Canvas(NewWin2 , bg = "#EEEEEE", width = 800, height = 650)
    canvas.pack()
    btn1 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t1, cursor = "circle",
                  command = square_area).place(x = 20, y = 130) #call square_area
    btn2 = Button(NewWin2, bd = 0, compound = CENTER, image =img_t2, cursor = "circle",
                  command = rectangle_area).place(x = 215, y = 130) #call rectangle_area
    btn3 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t3, cursor = "circle",
                  command = parallelogram_area).place(x = 408, y = 130)#call parallelogram_area
    btn4 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t4, cursor = "circle",
                  command = rhombus_area).place(x = 600, y = 130)#call rhombus_area
    btn5 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t5, cursor = "circle",
                  command = trapezium_area).place(x = 20, y = 330) #call trapezium_area
    btn6 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t6, cursor = "circle",
                  command = kite_area).place(x = 215, y = 330) #call kite_area
    btn7 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t7, cursor = "circle",
                  command = cuboid_volume).place(x = 408, y = 330)#call cuboid_volume
    btn8 = Button(NewWin2, bd = 0, compound = CENTER, image = img_t8, cursor = "circle",
                  command = cube_volume).place(x = 600, y = 330)#call cube_volume
    btn5 = Button(NewWin2, bd = 0,compound = CENTER, image = img_bg).place(x = 75, y = 540)
    btn6 = Button(NewWin2, bd = 0, compound = CENTER, image = img_tg2).place(x = 195, y = 10)
img_t1 = PhotoImage(file = "Square_1.gif")
img_t2 = PhotoImage(file = "Square_2.gif")
img_t3 = PhotoImage(file = "Square_3.gif")
img_t4 = PhotoImage(file = "Square_4.gif")
img_t5 = PhotoImage(file = "Square_5.gif")
img_t6 = PhotoImage(file = "Square_6.gif")
img_t7 = PhotoImage(file = "Volume-cuboid.gif")
img_t8 = PhotoImage(file = "Volume-cube.gif")
img_tg = PhotoImage(file = "line1.gif")
img_tg2 = PhotoImage(file = "menu_squ.gif")
img_good2 = PhotoImage(file = "Square.gif")
btn2 = Button(root, bd = 0, compound = CENTER, image = img_good2, cursor = "X_cursor", command = get_new_win).place(x = 310,y = 500)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##The calculation of circle
def circle_area():
    """the area of circle"""
    NewWin_circle_area = tk.Toplevel(root)
    NewWin_circle_area.title('Circle_area')
    NewWin_circle_area.geometry('800x680+235+8')
    NewWin_circle_area.iconbitmap("Femfoyou.ico")
    fields = ('Radian', 'Area', 'Circumference')
    def area(entries):
        radian = float(entries['Radian'].get())
        area = pi * (radian**2)
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def circumference(entries):
        radian = float(entries['Radian'].get())
        circumference = 2.0 * pi * radian
        circumference = ("%.2f" %circumference ).strip()
        entries['Circumference'].delete(0,END)
        entries['Circumference'].insert(0, circumference )
    def makeform(NewWin_circle_area, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_circle_area, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#1E90FF",text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_circle_area, fields)
        NewWin_circle_area.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_circle_area, text = 'Area', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 190)
        b3 = Button(NewWin_circle_area, text = 'Circumference', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: circumference(e))).place(x = 318, y = 250)
        
def circle_surface_area():
    """the area of circle surface"""
    NewWin_circle = tk.Toplevel(root)
    NewWin_circle.title('Circle_surface_area')
    NewWin_circle.geometry('800x680+235+8')
    NewWin_circle.iconbitmap("Femfoyou.ico")
    fields = ('Radian', 'Area')
    def area(entries):
        radian = float(entries['Radian'].get())
        area = 4.0 * pi * (radian**2)
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def makeform(NewWin_circle, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_circle, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#1E90FF",text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_circle, fields)
        NewWin_circle.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_circle, text = 'Area', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 160)

def cylinder_surface_area():
    """the area of cylinder surface"""    
    NewWin_cylinder = tk.Toplevel(root)
    NewWin_cylinder.title('Cylinder_area')
    NewWin_cylinder.geometry('800x680+235+8')
    NewWin_cylinder.iconbitmap("Femfoyou.ico")
    fields =('Radian', 'Height', 'Area', 'Surfaceside')
    def area(entries):
        radian = float(entries['Radian'].get())
        height = float(entries['Height'].get())
        area = (2.0 *pi*radian*height) + (2.0 * pi*(radian**2))
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def surfaceside(entries):
        radian = float(entries['Radian'].get())
        height = float(entries['Height'].get())
        surfaceside = 2.0*pi*radian*height
        surfaceside = ("%.2f" % surfaceside).strip()
        entries['Surfaceside'].delete(0,END)
        entries['Surfaceside'].insert(0, surfaceside )
    def makeform(NewWin_cylinder, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_cylinder, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#1E90FF",text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_cylinder, fields)
        NewWin_cylinder.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_cylinder, text = 'Area', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 260)
        b3 = Button(NewWin_cylinder, text = 'Surfaceside', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: surfaceside(e))).place(x = 330, y = 320)

def cone_surface_area():
    """the area of cone surface"""
    NewWin_cone = tk.Toplevel(root)
    NewWin_cone.title('Cone_surface_area')
    NewWin_cone.geometry('800x680+235+8')
    NewWin_cone.iconbitmap("Femfoyou.ico")
    fields =('Radian', 'Lenght', 'Area', 'Surfaceside')
    def area(entries):
        radian = float(entries['Radian'].get())
        lenght = float(entries['Lenght'].get())
        area = (pi * radian*lenght) + (pi * (radian**2))
        area = ("%.2f" % area).strip()
        entries['Area'].delete(0,END)
        entries['Area'].insert(0, area )
    def surfaceside(entries):
        radian = float(entries['Radian'].get())
        lenght = float(entries['Lenght'].get())
        surfaceside = pi*radian*lenght
        surfaceside = ("%.2f" % surfaceside).strip()
        entries['Surfaceside'].delete(0,END)
        entries['Surfaceside'].insert(0, surfaceside )
    def makeform(NewWin_cone, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_cone, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#1E90FF",text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_cone, fields)
        NewWin_cone.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_cone, text = 'Area', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: area(e))).place(x = 360, y = 260)
        b3 = Button(NewWin_cone, text = 'Surfaceside', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: surfaceside(e))).place(x = 330, y = 320)

def sphere_volume():
    """the area of sphere volume"""
    NewWin_sphere = tk.Toplevel(root)
    NewWin_sphere.title('Volume')
    NewWin_sphere.geometry('800x680+235+8')
    NewWin_sphere.iconbitmap("Femfoyou.ico")
    fields =('Radian', 'Height', 'Volume', 'Cylinder_volume', 'Cone_volume')
    def volume(entries):
        radian = float(entries['Radian'].get())
        volume = (4.0 / 3.0) * pi * (radian**3)
        volume = ("%.2f" % volume).strip()
        entries['Volume'].delete(0,END)
        entries['Volume'].insert(0,volume )
    def cylinder_volume(entries):
        radian = float(entries['Radian'].get())
        height = float(entries['Height'].get())
        cylinder_volume = pi * (radian**2) * height
        cylinder_volume = ("%.2f" % cylinder_volume).strip()
        entries['Cylinder_volume'].delete(0,END)
        entries['Cylinder_volume'].insert(0, cylinder_volume)
    def cone_volume(entries):
        radian = float(entries['Radian'].get())
        height = float(entries['Height'].get())
        cone_volume = (1.0 / 3.0) * pi * (radian**2) * height
        cone_volume = ("%.2f" % cone_volume).strip()
        entries['Cone_volume'].delete(0,END)
        entries['Cone_volume'].insert(0, cone_volume)
    def makeform(NewWin_sphere, fields):
        entries = {}
        for field in fields:
            row = Frame(NewWin_sphere, width = 140, height = 50)
            lab = Label(row, width = 22, font = ("Helvetica", 13), fg = "#1E90FF",text = field + " : ", anchor = 'w')
            row.pack_propagate(0)
            ent = Entry(row, justify = 'center', font = 14)
            ent.insert(0,"0")
            row.pack(side = TOP, padx = 5, pady = 5)
            lab.pack(side = TOP)
            ent.pack(side = RIGHT, expand = YES, fill = BOTH)
            entries[field] = ent
        return entries
    if __name__ == '__main__':
        ents = makeform(NewWin_sphere, fields)
        NewWin_sphere.bind('<Return>', (lambda event, e = ents: fetch(e)))
        b2 = Button(NewWin_sphere, text = 'Volume', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: volume(e))).place(x = 360, y = 320)
        b2 = Button(NewWin_sphere, text = 'Cylinder_volume', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: cylinder_volume(e))).place(x = 320, y = 380)
        b2 = Button(NewWin_sphere, text = 'Cone_volume', fg = "white", bg = "#6699FF", font = ("Helvetica", 16),
                    command = (lambda e = ents: cone_volume(e))).place(x = 333, y = 440)

#new window for select circle menu    
def get_new_win():
    NewWin2 = tk.Toplevel(root)
    NewWin2.title('Calculate Circle')
    NewWin2.geometry('800x680+235+8')
    NewWin2.iconbitmap("Jommans-Mushroom-Search.ico")
    canvas = Canvas(NewWin2, bg = "#EEEEEE", width = 800, height = 650)
    canvas.pack()
    btn1 = Button(NewWin2, bd = 0, compound = CENTER, image = img_c1, cursor = "circle",
                  command = circle_area).place(x = 20, y = 140) #call circle_area
    btn2 = Button(NewWin2, bd = 0, compound = CENTER, image = img_c2, cursor = "circle",
                  command = circle_surface_area).place(x = 215, y = 140) #call circle_surface_area
    btn3 = Button(NewWin2, bd = 0, compound = CENTER, image = img_c3, cursor = "circle",
                  command = cylinder_surface_area).place(x = 408, y =140)#call cylinder_surface_area
    btn4 = Button(NewWin2, bd = 0, compound = CENTER, image = img_c4, cursor = "circle",
                  command = cone_surface_area).place(x = 600, y = 140)#call cone_surface_area
    btn5 = Button(NewWin2, bd = 0, compound = CENTER, image = img_c5, cursor = "circle",
                  command = sphere_volume).place(x = 200, y = 350) #call sphere_volume    
    btn5 = Button(NewWin2, bd = 0, compound = CENTER, image = img_bg).place(x = 75, y = 540)
    btn6 = Button(NewWin2, bd = 0, compound = CENTER, image = img_cg2).place(x = 240, y = 10)  
img_c1 = PhotoImage(file = "Circle_1.gif")
img_c2 = PhotoImage(file = "Circle_2.gif")
img_c3 = PhotoImage(file = "Circle_3.gif")
img_c4 = PhotoImage(file = "Circle_4.gif")
img_c5 = PhotoImage(file = "Circle_5.gif")
img_cg = PhotoImage(file = "line1.gif")
img_cg2 = PhotoImage(file = "menu_cri.gif")    
img_good3 = PhotoImage(file = "Circle.gif")
btn3 = Button(root, bd = 0, compound = CENTER, image = img_good3, cursor = "X_cursor", command = get_new_win).place(x = 551, y = 500)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

root.mainloop()
