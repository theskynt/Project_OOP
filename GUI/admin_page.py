
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import admin_page_add
import admin_page_remove
import admin_page_modify
import admin_page_view
import main_page

class Admin_Page:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x700+455+44")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Admin")
        top.configure(background="#d1c9ad")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.197, rely=0.027, height=91, width=194)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d1c9ad")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Comic Sans MS} -size 36")
        self.Label1.configure(foreground="#6d5741")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ADMIN''')

        self.Admin_logo = tk.Label(self.top)
        self.Admin_logo.place(relx=0.033, rely=0.014, height=111, width=94)
        self.Admin_logo.configure(activebackground="#f9f9f9")
        self.Admin_logo.configure(activeforeground="black")
        self.Admin_logo.configure(anchor='w')
        self.Admin_logo.configure(background="#d1c9ad")
        self.Admin_logo.configure(compound='left')
        self.Admin_logo.configure(disabledforeground="#a3a3a3")
        self.Admin_logo.configure(foreground="#000000")
        self.Admin_logo.configure(highlightbackground="#d9d9d9")
        self.Admin_logo.configure(highlightcolor="black")
        photo_location = "./menu/addmin.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Admin_logo.configure(image=_img0)

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.89, rely=0.183, height=82, width=74)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d1c9ad")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        photo_location = "./menu/Logo3.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img1)

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.533, rely=0.093,  relwidth=0.467)

        self.Button_add = tk.Button(self.top)
        self.Button_add.place(relx=0.037, rely=0.2, height=45, width=120)
        self.Button_add.configure(activebackground="#ececec")
        self.Button_add.configure(activeforeground="#000000")
        self.Button_add.configure(background="#d1c9ad")
        self.Button_add.configure(compound='left')
        self.Button_add.configure(cursor="hand2")
        self.Button_add.configure(disabledforeground="#a3a3a3")
        self.Button_add.configure(foreground="#000000")
        self.Button_add.configure(highlightbackground="#d9d9d9")
        self.Button_add.configure(highlightcolor="black")
        photo_location = "./menu/Button_add.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button_add.configure(image=_img2)
        self.Button_add.configure(pady="0")
        self.Button_add.configure(relief="flat")
        self.Button_add.configure(command=self.open_admin_add)

        self.Button_remove = tk.Button(self.top)
        self.Button_remove.place(relx=0.26, rely=0.2, height=45, width=110)
        self.Button_remove.configure(activebackground="#ececec")
        self.Button_remove.configure(activeforeground="#000000")
        self.Button_remove.configure(background="#d1c9ad")
        self.Button_remove.configure(compound='left')
        self.Button_remove.configure(cursor="hand2")
        self.Button_remove.configure(disabledforeground="#a3a3a3")
        self.Button_remove.configure(foreground="#000000")
        self.Button_remove.configure(highlightbackground="#d9d9d9")
        self.Button_remove.configure(highlightcolor="black")
        photo_location = "./menu/Button_remove.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button_remove.configure(image=_img3)
        self.Button_remove.configure(pady="0")
        self.Button_remove.configure(relief="flat")
        self.Button_remove.configure(command=self.open_admin_remove)

        self.Button_view = tk.Button(self.top)
        self.Button_view.place(relx=0.71, rely=0.199, height=45, width=110)
        self.Button_view.configure(activebackground="#ececec")
        self.Button_view.configure(activeforeground="#000000")
        self.Button_view.configure(background="#d1c9ad")
        self.Button_view.configure(compound='left')
        self.Button_view.configure(cursor="hand2")
        self.Button_view.configure(disabledforeground="#a3a3a3")
        self.Button_view.configure(foreground="#000000")
        self.Button_view.configure(highlightbackground="#d9d9d9")
        self.Button_view.configure(highlightcolor="black")
        photo_location = "./menu/Button_view.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button_view.configure(image=_img4)
        self.Button_view.configure(pady="0")
        self.Button_view.configure(relief="flat")
        self.Button_view.configure(command=self.open_admin_view)

        self.Button_home = tk.Button(self.top)
        self.Button_home.place(relx=0.033, rely=0.914, height=45, width=110)
        self.Button_home.configure(activebackground="#ececec")
        self.Button_home.configure(activeforeground="#000000")
        self.Button_home.configure(background="#d1c9ad")
        self.Button_home.configure(compound='left')
        self.Button_home.configure(cursor="hand2")
        self.Button_home.configure(disabledforeground="#a3a3a3")
        self.Button_home.configure(foreground="#000000")
        self.Button_home.configure(highlightbackground="#d9d9d9")
        self.Button_home.configure(highlightcolor="black")
        photo_location = "./menu/home.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.Button_home.configure(image=_img5)
        self.Button_home.configure(pady="0")
        self.Button_home.configure(relief="flat")
        self.Button_home.configure(command=self.open_admin_home)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.032, rely=0.286, relheight=0.55, relwidth=0.942)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#f2ebe3")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Button_modify = tk.Button(self.top)
        self.Button_modify.place(relx=0.483, rely=0.2, height=44, width=117)
        self.Button_modify.configure(activebackground="#ececec")
        self.Button_modify.configure(activeforeground="#000000")
        self.Button_modify.configure(background="#d1c9ad")
        self.Button_modify.configure(compound='left')
        self.Button_modify.configure(cursor="hand2")
        self.Button_modify.configure(disabledforeground="#a3a3a3")
        self.Button_modify.configure(foreground="#000000")
        self.Button_modify.configure(highlightbackground="#d9d9d9")
        self.Button_modify.configure(highlightcolor="black")
        photo_location = "./menu/modify.png"
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.Button_modify.configure(image=_img6)
        self.Button_modify.configure(pady="0")
        self.Button_modify.configure(relief="flat")
        self.Button_modify.configure(command=self.open_admin_modify)

    def open_admin_add(self):
        self.top.destroy()
        admin_page_add.main_loop()

    def open_admin_remove(self):
        self.top.destroy()
        admin_page_remove.main_loop()

    def open_admin_modify(self):
        self.top.destroy()
        admin_page_modify.main_loop()

    def open_admin_view(self):
        self.top.destroy()
        admin_page_view.main_loop()

    def open_admin_home(self):
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
    # _w1 = admin_page.Toplevel1(_top1)
    _w1 = Admin_Page(_top1)
    root.mainloop()


if __name__ == '__main__':
    main_loop()

