
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import main_page

class End_Page:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x700+493+50")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Cafe")
        top.configure(background="#d1c9ad")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.283, rely=0.043, height=121, width=354)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d1c9ad")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Comic Sans MS} -size 36")
        self.Label1.configure(foreground="#6d5741")
        self.Label1.configure(text='''SHIP BA CAFE''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.115, rely=0.029, height=141, width=104)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d1c9ad")
        self.Label2.configure(compound='left')
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        photo_location = "./menu/logo2.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.202, rely=0.663, height=42, width=354)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d1c9ad")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Comic Sans MS} -size 28")
        self.Label3.configure(foreground="#6d5741")
        self.Label3.configure(text='''Successful Payment''')

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.312, rely=0.286, height=210, width=210)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d1c9ad")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        photo_location = "./menu/succeed.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label4.configure(image=_img1)

        self.Button_home = tk.Button(self.top)
        self.Button_home.place(relx=0.0, rely=0.9, height=54, width=607)
        self.Button_home.configure(activebackground="#ececec")
        self.Button_home.configure(activeforeground="#000000")
        self.Button_home.configure(background="#6d5741")
        self.Button_home.configure(compound='left')
        self.Button_home.configure(cursor="hand2")
        self.Button_home.configure(disabledforeground="#a3a3a3")
        self.Button_home.configure(font="-family {Comic Sans MS} -size 24")
        self.Button_home.configure(foreground="#f2ebe3")
        self.Button_home.configure(highlightbackground="#d9d9d9")
        self.Button_home.configure(highlightcolor="black")
        self.Button_home.configure(pady="0")
        self.Button_home.configure(relief="flat")
        self.Button_home.configure(text='''>>>>>>>>>>>>>> Go Home <<<<<<<<<<<<<<<''')
        self.Button_home.configure(command=self.open_home)

    
    def open_home(self):
        self.top.destroy()
        main_page.main_loop()

def main_loop(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = End_Page(_top1)
    root.mainloop()


if __name__ == '__main__':
    main_loop()
