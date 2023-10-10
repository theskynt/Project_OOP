
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import menu_page

class Main_Page():
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 

        top.geometry("600x700+498+40")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Home")
        top.configure(background="#d1c9ad")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.215, rely=0.091, height=95, width=336)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d1c9ad")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {Comic Sans MS} -size 48 -weight bold")
        self.Label1.configure(foreground="#6d5741")
        self.Label1.configure(text='''WELCOME''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.017, rely=0.0, height=51, width=84)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d1c9ad")
        self.Label2.configure(compound='left')
        self.Label2.configure(font="-family {Comic Sans MS} -size 28")
        self.Label2.configure(foreground="#6d5741")
        self.Label2.configure(text='''G8''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.283, rely=0.853, height=61, width=254)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d1c9ad")
        self.Label3.configure(compound='left')
        self.Label3.configure(font="-family {Comic Sans MS} -size 18")
        self.Label3.configure(foreground="#6d5741")
        self.Label3.configure(text='''......SHIP BA CAFE......''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.168, rely=0.257, height=384, width=397)
        self.Button2.configure(activebackground="#b59c82")
        self.Button2.configure(background="#d1c9ad")
        self.Button2.configure(compound='left')
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(foreground="#000000")
        photo_location = "./menu/Logo.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img0)
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(command=self.open_menu)

    def open_menu(self):
        self.top.destroy()
        menu_page.main_loop()

def main_loop(*args):
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = Main_Page(_top1)
    root.mainloop()

if __name__ == '__main__':
    main_loop()


