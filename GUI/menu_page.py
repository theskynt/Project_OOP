
from ast import Str, arg
import json
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from typing_extensions import Self

import main_page
import coffee_page
import tea_page
import login_admin_page

class Menu_Page:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x700+453+36")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Menu")
        top.configure(background="#d1c9ad")

        self.top = top

        self.Label_menu = tk.Label(self.top)
        self.Label_menu.place(relx=0.412, rely=0.029, height=80, width=414)
        self.Label_menu.configure(anchor='w')
        self.Label_menu.configure(background="#d1c9ad")
        self.Label_menu.configure(compound='left')
        self.Label_menu.configure(disabledforeground="#a3a3a3")
        self.Label_menu.configure(font="-family {Comic Sans MS} -size 48 -underline 1")
        self.Label_menu.configure(foreground="#6d5741")
        self.Label_menu.configure(text='''MENU''')

        self.Label_shipba = tk.Label(self.top)
        self.Label_shipba.place(relx=0.417, rely=0.14, height=41, width=154)
        self.Label_shipba.configure(anchor='w')
        self.Label_shipba.configure(background="#d1c9ad")
        self.Label_shipba.configure(compound='left')
        self.Label_shipba.configure(disabledforeground="#a3a3a3")
        self.Label_shipba.configure(font="-family {Comic Sans MS} -size 16")
        self.Label_shipba.configure(foreground="#6d5741")
        self.Label_shipba.configure(text='''SHIPBA CAFE''')
    

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.017, rely=0.227, relheight=0.636
                , relwidth=0.975)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#d1c9ad")
        

        list_menu = json.load(open('backend/menu.json'))
        x = 0
        x2 = 0
        btn_list = []
        btn_list2 = []
        self.img_list = []
        self.obj_name = []
        self.obj_type = []
        
        for o in list_menu:
            photo_location = f'./menu/{o["Name"]}.png'
            img = tk.PhotoImage(file=photo_location)
            self.img_list.append(img)
            self.obj_name.append(o["Name"])
            self.obj_type.append(o["Type"])
        
        for i in range(0,3):
            Button_1 = tk.Button(self.Frame1)
            Button_1.configure(activebackground="#ececec")
            Button_1.configure(activeforeground="#000000")
            Button_1.configure(background="#d1c9ad")
            Button_1.configure(compound='left')
            Button_1.configure(cursor="hand2")
            Button_1.configure(disabledforeground="#a3a3a3")
            Button_1.configure(foreground="#000000")
            Button_1.configure(highlightbackground="#d9d9d9")
            Button_1.configure(highlightcolor="black")
            Button_1.configure(image=self.img_list[i])
            Button_1.configure(pady="0")
            Button_1.configure(relief="flat")

            Button_1.name = self.obj_name[i]
            self.name = Button_1.name
            Button_1.type = self.obj_type[i]
            
            if Button_1.type == "Coffee":
                command = lambda arg=self.name: self.open_coffee_page(arg)
                Button_1.configure(command=command)
            if Button_1.type == "Tea":
                command = lambda arg=self.name: self.open_tea_page(arg)
                Button_1.configure(command=command)

            Button_1.place(relx=x, rely=0.0, height=200, width=190)
            btn_list.append(Button_1)
            x += 0.33

        for i in range(3,6):
            if len(self.img_list) <= i: break
            Button_1 = tk.Button(self.Frame1)
            Button_1.configure(activebackground="#ececec")
            Button_1.configure(activeforeground="#000000")
            Button_1.configure(background="#d1c9ad")
            Button_1.configure(compound='left')
            Button_1.configure(cursor="hand2")
            Button_1.configure(disabledforeground="#a3a3a3")
            Button_1.configure(foreground="#000000")
            Button_1.configure(highlightbackground="#d9d9d9")
            Button_1.configure(highlightcolor="black")
            Button_1.configure(image=self.img_list[i])
            Button_1.configure(pady="0")
            Button_1.configure(relief="flat")
            
            Button_1.name = self.obj_name[i]
            self.name = Button_1.name
            Button_1.type = self.obj_type[i]
            if Button_1.type == "Coffee":
                command = lambda arg=self.name: self.open_coffee_page(arg)
                Button_1.configure(command=command)
            if Button_1.type == "Tea":
                command = lambda arg=self.name: self.open_tea_page(arg)
                Button_1.configure(command=command)
            
            Button_1.place(relx=x2, rely=0.55, height=200, width=190)
            btn_list2.append(Button_1)
            x2 += 0.33

        #print(btn_list)
        #print(btn_list2)

        self.Button_home = tk.Button(self.top)
        self.Button_home.place(relx=0.033, rely=0.914, height=44, width=107)
        self.Button_home.configure(activebackground="#d1c9ad")
        self.Button_home.configure(activeforeground="#000000")
        self.Button_home.configure(background="#d1c9ad")
        self.Button_home.configure(compound='left')
        self.Button_home.configure(cursor="hand2")
        self.Button_home.configure(disabledforeground="#a3a3a3")
        self.Button_home.configure(foreground="#000000")
        self.Button_home.configure(highlightbackground="#d9d9d9")
        self.Button_home.configure(highlightcolor="black")
        photo_location = "./menu/home.png"
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.Button_home.configure(image=_img6)
        self.Button_home.configure(pady="0")
        self.Button_home.configure(relief="flat")
        self.Button_home.configure(command=self.open_home)

        self.Button_admin = tk.Button(self.top)
        self.Button_admin.place(relx=0.883, rely=0.9, height=57, width=57)
        self.Button_admin.configure(activebackground="#d1c9ad")
        self.Button_admin.configure(activeforeground="#000000")
        self.Button_admin.configure(background="#d1c9ad")
        self.Button_admin.configure(compound='left')
        self.Button_admin.configure(cursor="hand2")
        self.Button_admin.configure(disabledforeground="#a3a3a3")
        self.Button_admin.configure(foreground="#000000")
        self.Button_admin.configure(highlightbackground="#d9d9d9")
        self.Button_admin.configure(highlightcolor="black")
        photo_location = "./menu/admin2.png"
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.Button_admin.configure(image=_img7)
        self.Button_admin.configure(pady="0")
        self.Button_admin.configure(relief="flat")
        self.Button_admin.configure(command=self.open_login_admin_page)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.232, rely=0.029, height=115, width=115)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d1c9ad")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = "./menu/logo2.png"
        global _img8
        _img8 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img8)

    def open_home(self):
        self.top.destroy()
        main_page.main_loop()

    def open_coffee_page(self,name):
        self.top.destroy()
        coffee_page.main_loop(name)
        print(name)

    def open_tea_page(self,name):
        self.top.destroy()
        tea_page.main_loop(name)
        print(name)

    def open_login_admin_page(self):
        self.top.destroy()
        login_admin_page.main_loop()

    def select_menu(self):
        data = json.d


def main_loop(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    # _w1 = menu_page.Toplevel1(_top1)
    _w1 = Menu_Page(_top1)
    root.mainloop()

if __name__ == '__main__':
    main_loop()