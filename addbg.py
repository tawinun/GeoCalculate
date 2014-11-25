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
B1 = Tkinter.Button(root, text = "Quit", command = quitprogram).place(x=450,y=280)
##----------------------------------------------------


##buttons layout
b1 = Tkinter.Button(root, text='button1',cursor="X_cursor").place(x=550,y=210)
b2 = Tkinter.Button(root, text='button2',cursor="X_cursor").place(x=410,y=200)


##combo box

class View(tk.Frame):
    count = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        b = tk.Button(self, text="Open new window", command=self.new_window)
        b.pack(side="right")

    def new_window(self):
        self.count += 1
        id = "New window #%s" % self.count
        window = tk.Toplevel(self)
        label = tk.Label(window, text=id)
        label.pack(side="top", fill="both", padx=10, pady=10)

if __name__ == "__main__":

    view = View(root)
    view.pack(side="top", fill="both", expand=True)



root.mainloop()
