
from multiprocessing.dummy import Value
from pydoc import text
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import admin_page_modify
import admin_page_add
import admin_page_remove
import admin_page_view
import main_page
from backend import admin
import json
from tkinter import messagebox

class Admin_Page_Modify:

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
        self.chack = False

        top.geometry("600x700+474+45")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Admin_Modify")
        top.configure(background="#d1c9ad")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.combobox2 = tk.StringVar()

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
        self.Label3.place(relx=0.853, rely=0.181, height=82, width=74)
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
        self.Button_remove.place(relx=0.233, rely=0.2, height=45, width=110)
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
        self.Button_view.place(relx=0.65, rely=0.2, height=45, width=110)
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
        self.Button_home.place(relx=0.035, rely=0.913, height=45, width=110)
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
        self.Frame1.place(relx=0.033, rely=0.286, relheight=0.55, relwidth=0.942)

        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#f2ebe3")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.028, rely=0.044, height=31, width=184)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#f2ebe3")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Comic Sans MS} -size 18 -underline 1")
        self.Label2.configure(foreground="#6d5741")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''MODIFY MENU''')

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.018, rely=0.156, relheight=0.714
                , relwidth=0.965)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#f2ebe3")
        self.Frame2.configure(highlightbackground="#d1c9ad")
        self.Frame2.configure(highlightcolor="#d1c9ad")

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.037, rely=0.12, height=21, width=114)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#f2ebe3")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 12")
        self.Label4.configure(foreground="#6d5741")
        self.Label4.configure(text='''Menu Name  : ''')

        self.Label6 = tk.Label(self.Frame2)
        self.Label6.place(relx=0.037, rely=0.284, height=21, width=64)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#f2ebe3")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Comic Sans MS} -size 12")
        self.Label6.configure(foreground="#6d5741")
        self.Label6.configure(text='''Type  :''')

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.037, rely=0.582, height=21, width=74)
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#f2ebe3")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Comic Sans MS} -size 12")
        self.Label7.configure(foreground="#6d5741")
        self.Label7.configure(text='''Water  :''')

        self.Label8 = tk.Label(self.Frame2)
        self.Label8.place(relx=0.037, rely=0.731, height=21, width=54)
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#f2ebe3")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Comic Sans MS} -size 12")
        self.Label8.configure(foreground="#6d5741")
        self.Label8.configure(text='''Ice  :''')

        self.Label9 = tk.Label(self.Frame2)
        self.Label9.place(relx=0.514, rely=0.596, height=21, width=104)
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#f2ebe3")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Comic Sans MS} -size 12")
        self.Label9.configure(foreground="#6d5741")
        self.Label9.configure(text='''Milk Foam  :''')

        self.Label10 = tk.Label(self.Frame2)
        self.Label10.place(relx=0.037, rely=0.873, height=21, width=64)
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#f2ebe3")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Comic Sans MS} -size 12")
        self.Label10.configure(foreground="#6d5741")
        self.Label10.configure(text='''Milk  :''')

        self.Label11 = tk.Label(self.Frame2)
        self.Label11.place(relx=0.516, rely=0.742, height=21, width=64)
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#f2ebe3")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Comic Sans MS} -size 12")
        self.Label11.configure(foreground="#6d5741")
        self.Label11.configure(text='''Price  :''')

        self.Label12 = tk.Label(self.Frame2)
        self.Label12.place(relx=0.349, rely=0.469, height=21, width=164)
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#f2ebe3")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Comic Sans MS} -size 12 -underline 1")
        self.Label12.configure(foreground="#6d5741")
        self.Label12.configure(text='''Raw Materials Used''')

        self.TSeparator2 = ttk.Separator(self.Frame2)
        self.TSeparator2.place(relx=0.042, rely=0.516,  relwidth=0.292)

        self.Entry_name = tk.Entry(self.Frame2)
        self.Entry_name.place(relx=0.246, rely=0.116, height=25, relwidth=0.338)
        self.Entry_name.configure(background="white")
        self.Entry_name.configure(disabledforeground="#a3a3a3")
        self.Entry_name.configure(font="TkFixedFont")
        self.Entry_name.configure(foreground="#000000")
        self.Entry_name.configure(insertbackground="black")
        

        self.Combobox_type = ttk.Combobox(self.Frame2)
        self.Combobox_type.place(relx=0.16, rely=0.276, relheight=0.091
                , relwidth=0.152)
        self.Combobox_type.configure(textvariable=self.combobox)
        self.Combobox_type.configure(takefocus="")
        self.Combobox_type.configure(values=["Tea", "Coffee"])

        self.Entry_milk = tk.Entry(self.Frame2)
        self.Entry_milk.place(relx=0.156, rely=0.873, height=25, relwidth=0.103)
        self.Entry_milk.configure(background="white")
        self.Entry_milk.configure(disabledforeground="#a3a3a3")
        self.Entry_milk.configure(font="TkFixedFont")
        self.Entry_milk.configure(foreground="#000000")
        self.Entry_milk.configure(insertbackground="black")

        self.Entry_milk_foam = tk.Entry(self.Frame2)
        self.Entry_milk_foam.place(relx=0.708, rely=0.578, height=25
                , relwidth=0.117)
        self.Entry_milk_foam.configure(background="white")
        self.Entry_milk_foam.configure(disabledforeground="#a3a3a3")
        self.Entry_milk_foam.configure(font="TkFixedFont")
        self.Entry_milk_foam.configure(foreground="#000000")
        self.Entry_milk_foam.configure(insertbackground="black")

        self.Entry_price = tk.Entry(self.Frame2)
        self.Entry_price.place(relx=0.64, rely=0.735, height=25, relwidth=0.117)
        self.Entry_price.configure(background="white")
        self.Entry_price.configure(disabledforeground="#a3a3a3")
        self.Entry_price.configure(font="TkFixedFont")
        self.Entry_price.configure(foreground="#000000")
        self.Entry_price.configure(insertbackground="black")

        self.Entry_water = tk.Entry(self.Frame2)
        self.Entry_water.place(relx=0.182, rely=0.56, height=25, relwidth=0.099)
        self.Entry_water.configure(background="white")
        self.Entry_water.configure(disabledforeground="#a3a3a3")
        self.Entry_water.configure(font="TkFixedFont")
        self.Entry_water.configure(foreground="#000000")
        self.Entry_water.configure(insertbackground="black")

        self.Entry_ice = tk.Entry(self.Frame2)
        self.Entry_ice.place(relx=0.138, rely=0.713, height=25, relwidth=0.099)
        self.Entry_ice.configure(background="white")
        self.Entry_ice.configure(disabledforeground="#a3a3a3")
        self.Entry_ice.configure(font="TkFixedFont")
        self.Entry_ice.configure(foreground="#000000")
        self.Entry_ice.configure(insertbackground="black")

        self.TSeparator3 = ttk.Separator(self.Frame2)
        self.TSeparator3.place(relx=0.64, rely=0.516,  relwidth=0.317)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.842, rely=0.894, height=34, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#6d5741")
        self.Button1.configure(compound='left')
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#f2ebe3")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''SAVE''')
        self.Button1.configure(command=self.admin_modify_menu)
        

        self.Combobox_id = ttk.Combobox(self.Frame1)
        self.Combobox_id.place(relx=0.566, rely=0.052, relheight=0.065
                , relwidth=0.147)
        self.Combobox_id.configure(textvariable=self.combobox2)
        self.Combobox_id.configure(takefocus="")
        self.Combobox_id.configure(values=[*range(1, len(self.menu)+1)])

        self.Button_search = tk.Button(self.Frame1)
        self.Button_search.place(relx=0.742, rely=0.034, height=34, width=77)
        self.Button_search.configure(activebackground="#ececec")
        self.Button_search.configure(activeforeground="#000000")
        self.Button_search.configure(background="#6d5741")
        self.Button_search.configure(compound='left')
        self.Button_search.configure(disabledforeground="#a3a3a3")
        self.Button_search.configure(foreground="#f2ebe3")
        self.Button_search.configure(highlightbackground="#d9d9d9")
        self.Button_search.configure(highlightcolor="black")
        self.Button_search.configure(pady="0")
        self.Button_search.configure(relief="groove")
        self.Button_search.configure(text='''Search''')
        self.Button_search.configure(command=self.open_menu_modify)

        self.Label13 = tk.Label(self.Frame1)
        self.Label13.place(relx=0.402, rely=0.044, height=31, width=84)
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#f2ebe3")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Comic Sans MS} -size 12")
        self.Label13.configure(foreground="#6d5741")
        self.Label13.configure(text='''Select ID :''')

        self.Button_modify = tk.Button(self.top)
        self.Button_modify.place(relx=0.445, rely=0.2, height=45, width=110)
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

    def open_admin_add(self):
        self.top.destroy()
        admin_page_add.main_loop()

    def open_admin_remove(self):
        self.top.destroy()
        admin_page_remove.main_loop()

    def open_admin_view(self):
        self.top.destroy()
        admin_page_view.main_loop()

    def open_admin_home(self):
        self.top.destroy()
        main_page.main_loop()

    def open_menu_modify(self):
        self.chack = True
        self.menu_modify = self.menu[int(self.Combobox_id.get())-1]
        if self.chack == True :
            self.Entry_name.delete(0, END)
            self.Entry_ice.delete(0, END)
            self.Entry_milk.delete(0, END)
            self.Entry_milk_foam.delete(0, END)
            self.Entry_water.delete(0, END)
            self.Entry_price.delete(0, END)
            self.Combobox_type.delete(0, END)
            self.Entry_name.insert(END,f'{self.menu_modify["Name"]}')
            self.Entry_ice.insert(END,f'{self.menu_modify["Ice"]}')
            self.Entry_milk.insert(END,f'{self.menu_modify["Milk"]}')
            self.Entry_milk_foam.insert(END,f'{self.menu_modify["Milk_Foam"]}')
            self.Entry_water.insert(END,f'{self.menu_modify["Water"]}')
            self.Entry_price.insert(END,f'{self.menu_modify["Price"]}')
            self.Combobox_type.insert(END,f'{self.menu_modify["Type"]}')

    def admin_modify_menu(self):
        messagebox.showinfo("Save Modify", "Save successfully !!!")
        self.dict_menu = {}
        admin_modify = admin.Admin()

        name = self.Entry_name.get()
        type = self.Combobox_type.get()
        water = self.Entry_water.get()
        ice = self.Entry_ice.get()
        milk = self.Entry_milk.get()
        milk_foam = self.Entry_milk_foam.get()
        price = self.Entry_price.get()

        self.dict_menu.update({"Name" : name})
        self.dict_menu.update({"Type" : type})
        self.dict_menu.update({"Water" : int(water)})
        self.dict_menu.update({"Ice" : int(ice)})
        self.dict_menu.update({"Milk" : int(milk)})
        self.dict_menu.update({"Milk_Foam" : int(milk_foam)})
        self.dict_menu.update({"Price" : int(price)})
        
        admin_modify.modify_menu(int(self.Combobox_id.get()), self.dict_menu)

def main_loop(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Admin_Page_Modify(_top1)
    root.mainloop()

if __name__ == '__main__':
    main_loop()
