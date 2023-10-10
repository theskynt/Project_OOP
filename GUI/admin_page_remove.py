
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import admin_page_remove
import admin_page_add
import admin_page_modify
import admin_page_view
import main_page
from backend import admin
import json
from tkinter import messagebox

class Admin_Page_Remove:

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

        self.menu = json.load(open('backend/menu.json'))

        top.geometry("600x700+455+44")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Admin_Remove")
        top.configure(background="#d1c9ad")

        self.top = top
        self.combobox = tk.StringVar()

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.197, rely=0.027, height=91, width=194)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d1c9ad")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {Comic Sans MS} -size 36")
        self.Label1.configure(foreground="#6d5741")
        self.Label1.configure(text='''ADMIN''')

        self.Admin_logo = tk.Label(self.top)
        self.Admin_logo.place(relx=0.033, rely=0.014, height=111, width=94)
        self.Admin_logo.configure(activebackground="#f9f9f9")
        self.Admin_logo.configure(anchor='w')
        self.Admin_logo.configure(background="#d1c9ad")
        self.Admin_logo.configure(compound='left')
        self.Admin_logo.configure(foreground="#000000")
        photo_location = "./menu/addmin.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Admin_logo.configure(image=_img0)

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.853, rely=0.181, height=82, width=74)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d1c9ad")
        self.Label3.configure(compound='left')
        self.Label3.configure(foreground="#000000")
        photo_location = "./menu/Logo3.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img1)

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.533, rely=0.093,  relwidth=0.467)

        self.Button_add = tk.Button(self.top)
        self.Button_add.place(relx=0.062, rely=0.203, height=45, width=110)
        self.Button_add.configure(activebackground="#ececec")
        self.Button_add.configure(background="#d1c9ad")
        self.Button_add.configure(compound='left')
        self.Button_add.configure(cursor="hand2")
        self.Button_add.configure(foreground="#000000")
        photo_location = "./menu/Button_add.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button_add.configure(image=_img2)
        self.Button_add.configure(pady="0")
        self.Button_add.configure(relief="flat")
        self.Button_add.configure(command=self.open_admin_add)

        self.Button_remove = tk.Button(self.top)
        self.Button_remove.place(relx=0.258, rely=0.2, height=45, width=110)
        self.Button_remove.configure(activebackground="#ececec")
        self.Button_remove.configure(background="#d1c9ad")
        self.Button_remove.configure(compound='left')
        self.Button_remove.configure(cursor="hand2")
        self.Button_remove.configure(foreground="#000000")
        photo_location = "./menu/Button_remove.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button_remove.configure(image=_img3)
        self.Button_remove.configure(pady="0")
        self.Button_remove.configure(relief="flat")

        self.Button_view = tk.Button(self.top)
        self.Button_view.place(relx=0.663, rely=0.2, height=45, width=110)
        self.Button_view.configure(activebackground="#ececec")
        self.Button_view.configure(background="#d1c9ad")
        self.Button_view.configure(compound='left')
        self.Button_view.configure(cursor="hand2")
        self.Button_view.configure(foreground="#000000")
        photo_location = "./menu/Button_view.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button_view.configure(image=_img4)
        self.Button_view.configure(pady="0")
        self.Button_view.configure(relief="flat")
        self.Button_view.configure(command=self.open_admin_view)

        self.Button_home = tk.Button(self.top)
        self.Button_home.place(relx=0.035, rely=0.913, height=45, width=110)
        self.Button_home.configure(activebackground="#ececec")
        self.Button_home.configure(background="#d1c9ad")
        self.Button_home.configure(compound='left')
        self.Button_home.configure(cursor="hand2")
        self.Button_home.configure(foreground="#000000")
        photo_location = "./menu/home.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.Button_home.configure(image=_img5)
        self.Button_home.configure(pady="0")
        self.Button_home.configure(relief="flat")
        self.Button_home.configure(command=self.open_admin_home)

        self.Button_remov = tk.Frame(self.top)
        self.Button_remov.place(relx=0.033, rely=0.286, relheight=0.323
                , relwidth=0.942)
        self.Button_remov.configure(relief='groove')
        self.Button_remov.configure(borderwidth="2")
        self.Button_remov.configure(relief="groove")
        self.Button_remov.configure(background="#f2ebe3")


        self.Label2 = tk.Label(self.Button_remov)
        self.Label2.place(relx=0.035, rely=0.044, height=48, width=194)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#f2ebe3")
        self.Label2.configure(compound='left')
        self.Label2.configure(font="-family {Comic Sans MS} -size 18 -underline 1")
        self.Label2.configure(foreground="#6d5741")
        self.Label2.configure(text='''REMOVE MENU''')

        self.Combobox_id_menu = ttk.Combobox(self.Button_remov)
        self.Combobox_id_menu.place(relx=0.372, rely=0.35, relheight=0.111
                , relwidth=0.129)
        self.Combobox_id_menu.configure(font="-family {Comic Sans MS} -size 12")
        self.Combobox_id_menu.configure(textvariable=self.combobox)
        self.Combobox_id_menu.configure(takefocus="")
        self.Combobox_id_menu.configure(cursor="hand2")
        self.Combobox_id_menu.configure(values=[*range(1, len(self.menu)+1)])

        self.Label4 = tk.Label(self.Button_remov)
        self.Label4.place(relx=0.074, rely=0.332, height=32, width=164)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#f2ebe3")
        self.Label4.configure(compound='left')
        self.Label4.configure(font="-family {Comic Sans MS} -size 13")
        self.Label4.configure(foreground="#6d5741")
        self.Label4.configure(text='''Select Menu ID  :''')

        self.Button1 = tk.Button(self.Button_remov)
        self.Button1.place(relx=0.832, rely=0.796, height=34, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(background="#6d5741")
        self.Button1.configure(compound='left')
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(foreground="#f2ebe3")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''REMOVE''')
        self.Button1.configure(command=self.remove_menu)

        self.Label5 = tk.Label(self.Button_remov)
        self.Label5.place(relx=0.078, rely=0.619, height=25, width=114)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#f2ebe3")
        self.Label5.configure(compound='left')
        self.Label5.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5.configure(foreground="#6d5741")
        self.Label5.configure(text='''Menu Name  :''')

        self.Label_name_menu = tk.Label(self.Button_remov)
        self.Label_name_menu.place(relx=0.292, rely=0.619, height=25, width=300)
        self.Label_name_menu.configure(anchor='w')
        self.Label_name_menu.configure(background="#f2ebe3")
        self.Label_name_menu.configure(compound='left')
        self.Label_name_menu.configure(cursor="arrow")
        self.Label_name_menu.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_name_menu.configure(foreground="#6d5741")
        self.Label_name_menu.configure(text='''-''')

        self.Button2 = tk.Button(self.Button_remov)
        self.Button2.place(relx=0.549, rely=0.354, height=24, width=57)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#6d5741")
        self.Button2.configure(compound='left')
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#f2ebe3")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Check''')
        self.Button2.configure(command=self.open_menu)

        self.Button_modify = tk.Button(self.top)
        self.Button_modify.place(relx=0.46, rely=0.2, height=45, width=110)
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

    def open_admin_modify(self):
        self.top.destroy()
        admin_page_modify.main_loop()

    def open_admin_view(self):
        self.top.destroy()
        admin_page_view.main_loop()

    def open_admin_home(self):
        self.top.destroy()
        main_page.main_loop()

    def open_menu(self):
        self.id = int(self.Combobox_id_menu.get())
        self.Label_name_menu.configure(text=f'''{self.menu[self.id-1]["Name"]}''')

    def remove_menu(self):
        messagebox.showinfo("Remove Menu", "Remove successfully")
        admin_remove = admin.Admin()
        admin_remove.del_menu(self.id)


def main_loop(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Admin_Page_Remove(_top1)
    root.mainloop()


if __name__ == '__main__':
    main_loop()



