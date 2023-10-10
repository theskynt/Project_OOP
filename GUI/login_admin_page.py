
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from typing_extensions import Self

import admin_page
import main_page
from backend import admin
from tkinter import messagebox

class Login_Admin:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x700+448+31")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Login")
        top.configure(background="#d1c9ad")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.235, rely=0.264, height=91, width=324)
        self.Label1.configure(activebackground="#d1c9ad")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d1c9ad")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Comic Sans MS} -size 30")
        self.Label1.configure(foreground="#6d5741")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''LOG IN ADMIN''')

        self.Image_admin = tk.Label(self.top)
        self.Image_admin.place(relx=0.42, rely=0.127, height=101, width=94)
        self.Image_admin.configure(activebackground="#d1c9ad")
        self.Image_admin.configure(activeforeground="black")
        self.Image_admin.configure(anchor='w')
        self.Image_admin.configure(background="#d1c9ad")
        self.Image_admin.configure(compound='left')
        self.Image_admin.configure(disabledforeground="#a3a3a3")
        self.Image_admin.configure(foreground="#000000")
        self.Image_admin.configure(highlightbackground="#d9d9d9")
        self.Image_admin.configure(highlightcolor="black")
        photo_location = "./menu/addmin.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Image_admin.configure(image=_img0)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.083, rely=0.4, relheight=0.321, relwidth=0.842)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#e0d7c9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Entry_user = tk.Entry(self.Frame1)
        self.Entry_user.place(relx=0.436, rely=0.32, height=30, relwidth=0.384)
        self.Entry_user.configure(background="white")
        self.Entry_user.configure(disabledforeground="#a3a3a3")
        self.Entry_user.configure(font="TkFixedFont")
        self.Entry_user.configure(foreground="#000000")
        self.Entry_user.configure(highlightbackground="#d9d9d9")
        self.Entry_user.configure(highlightcolor="black")
        self.Entry_user.configure(insertbackground="black")
        self.Entry_user.configure(selectbackground="blue")
        self.Entry_user.configure(selectforeground="white")

        self.Entry_password = tk.Entry(self.Frame1)
        self.Entry_password.place(relx=0.436, rely=0.578, height=30
                , relwidth=0.384)
        self.Entry_password.configure(background="white")
        self.Entry_password.configure(disabledforeground="#a3a3a3")
        self.Entry_password.configure(font="TkFixedFont")
        self.Entry_password.configure(foreground="#000000")
        self.Entry_password.configure(highlightbackground="#d9d9d9")
        self.Entry_password.configure(highlightcolor="black")
        self.Entry_password.configure(insertbackground="black")
        self.Entry_password.configure(selectbackground="blue")
        self.Entry_password.configure(selectforeground="white")
        self.Entry_password.configure(show= '*')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.178, rely=0.316, height=31, width=124)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#e0d7c9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 12")
        self.Label4.configure(foreground="#6d5741")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''USER NAME  :''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.188, rely=0.596, height=21, width=124)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#e0d7c9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5.configure(foreground="#6d5741")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''PASSWORD  :''')

        self.Button_login = tk.Button(self.top)
        self.Button_login.place(relx=0.388, rely=0.747, height=44, width=127)
        self.Button_login.configure(activebackground="#ececec")
        self.Button_login.configure(activeforeground="#000000")
        self.Button_login.configure(background="#6d5741")
        self.Button_login.configure(compound='left')
        self.Button_login.configure(disabledforeground="#a3a3a3")
        self.Button_login.configure(font="-family {Comic Sans MS} -size 14")
        self.Button_login.configure(foreground="#ffffff")
        self.Button_login.configure(highlightbackground="#d9d9d9")
        self.Button_login.configure(highlightcolor="black")
        self.Button_login.configure(pady="0")
        self.Button_login.configure(relief="groove")
        self.Button_login.configure(text='''LOG IN''')
        self.Button_login.configure(command=self.open_admin_page)

        self.Button_home = tk.Button(self.top)
        self.Button_home.place(relx=0.002, rely=0.891, height=74, width=77)
        self.Button_home.configure(activebackground="#ececec")
        self.Button_home.configure(activeforeground="#000000")
        self.Button_home.configure(background="#d1c9ad")
        self.Button_home.configure(compound='left')
        self.Button_home.configure(disabledforeground="#a3a3a3")
        self.Button_home.configure(foreground="#000000")
        self.Button_home.configure(highlightbackground="#d9d9d9")
        self.Button_home.configure(highlightcolor="black")
        photo_location = "./menu/Logo3.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button_home.configure(image=_img1)
        self.Button_home.configure(pady="0")
        self.Button_home.configure(relief="flat")
        self.Button_home.configure(command=self.open_home)

    def open_admin_page(self):
        admin_login = admin.Admin()
        self.log = admin_login.login(self.Entry_user.get(), self.Entry_password.get())
        if self.log == True :
            self.top.destroy()
            admin_page.main_loop()
            print("pass")
        else:
            messagebox.showwarning("Warning!!!", "User or password is incorrect.!")
            print("error")

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
    _w1 = Login_Admin(_top1)
    root.mainloop()

if __name__ == '__main__':
    main_loop()

