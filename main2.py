
from Tkinter import *
from PIL import ImageTk
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
B1 = Tkinter.Button(root, text = "Quit", command = quitprogram).place(x=550,y=280)
##----------------------------------------------------


##buttons layout
b1 = Tkinter.Button(root, text='button1',cursor="X_cursor").place(x=550,y=180)
b2 = Tkinter.Button(root, text='button2',cursor="X_cursor").place(x=550,y=220)



##Calculate triangle

def get_new_win():

    NewWin = tk.Toplevel(root)
    NewWin.title('triangle')
    NewWin.geometry('400x400')
    fields = ('base', 'height', 'area')

    def area(entries):
   # period rate:

   # principal loan:
       base = float(entries['base'].get())
       height =  float(entries['height'].get())
   
       area = 1.0/2.0*base*height
       area = ("%.2f" % area).strip()
    ##   entries['area'].delete(0,END)
       entries['area'].insert(0, area )
       print("area:" ,area)

    def makeform(NewWin, fields):
       entries = {}
       for field in fields:
          row = Frame(NewWin)
          lab = Label(row, width=22, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries

    if __name__ == '__main__':
       ents = makeform(NewWin, fields)
       NewWin.bind('<Return>', (lambda event, e=ents: fetch(e)))   
       b2 = Button(NewWin, text='Area',command=(lambda e=ents: area(e)))
       b2.pack(side=LEFT, padx=5, pady=5)
       
    

    def quit_win():
        NewWin.destroy()
        

    QuitButton = tk.Button(NewWin,text='Quit',command=quit_win)
    QuitButton.pack(side=LEFT, padx=5, pady=5)
    NewWin.protocol("WM_DELETE_WINDOW", quit_win)
        
    

NewWinButton = tk.Button(root,text='New Window', command=get_new_win).place(x=550,y=150)

####Text entry
##svalue = StringVar() # defines the widget state as string
##w = Entry(root,textvariable=svalue) # adds a textarea widget
##w.pack()
##def act():
##    print "you entered"
##    print '%s' % svalue.get()
##foo = Button(root,text="Press Me", command=act)
##foo.pack()



root.mainloop()
