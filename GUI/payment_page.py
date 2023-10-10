
import json
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import menu_page
import end_page
from backend import main
from tkinter import messagebox



class Payment_Page:
    
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

        top.geometry("600x700+483+80")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Payment")
        top.configure(background="#d1c9ad")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.data = json.load(open('backend/receipt.json'))
        self.price = main.Scan_Menu.calculate()


        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.282, rely=0.157, height=70, width=264)
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
        self.Label1.configure(text='''PAY MENT''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.397, rely=-0.004, height=131, width=124)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d1c9ad")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        photo_location = "menu/logo2.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.067, rely=0.243, relheight=0.72, relwidth=0.875)

        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#f2ebe3")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Image_menu = tk.Label(self.Frame1)
        self.Image_menu.place(relx=0.324, rely=0.054, height=185, width=184)
        self.Image_menu.configure(activebackground="#f9f9f9")
        self.Image_menu.configure(activeforeground="black")
        self.Image_menu.configure(anchor='w')
        self.Image_menu.configure(background="#f2ebe3")
        self.Image_menu.configure(compound='left')
        self.Image_menu.configure(disabledforeground="#a3a3a3")
        self.Image_menu.configure(foreground="#000000")
        self.Image_menu.configure(highlightbackground="#d9d9d9")
        self.Image_menu.configure(highlightcolor="black")
        photo_location = f'menu/{self.data["Name"]}.png'
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Image_menu.configure(image=_img1)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.019, rely=0.437, relheight=0.546
                , relwidth=0.962)
        self.Frame2.configure(relief='flat')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#f2ebe3")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="#6f5235")

        self.TSeparator1 = ttk.Separator(self.Frame2)
        self.TSeparator1.place(relx=0.556, rely=0.095,  relheight=0.604)
        self.TSeparator1.configure(orient="vertical")

        self.Label_price_total = tk.Label(self.Frame2)
        self.Label_price_total.place(relx=0.604, rely=0.353, height=51
                , width=174)
        self.Label_price_total.configure(activebackground="#f9f9f9")
        self.Label_price_total.configure(activeforeground="black")
        self.Label_price_total.configure(anchor='w')
        self.Label_price_total.configure(background="#f2ebe3")
        self.Label_price_total.configure(borderwidth="45")
        self.Label_price_total.configure(disabledforeground="#a3a3a3")
        self.Label_price_total.configure(font="-family {Comic Sans MS} -size 36")
        self.Label_price_total.configure(foreground="#332615")
        self.Label_price_total.configure(highlightbackground="#d9d9d9")
        self.Label_price_total.configure(highlightcolor="black")
        self.Label_price_total.configure(text=f'{self.price}  ฿')

        self.Button_credit_card = tk.Button(self.Frame2)
        self.Button_credit_card.place(relx=0.725, rely=0.793, height=45
                , width=110)
        self.Button_credit_card.configure(activebackground="#ececec")
        self.Button_credit_card.configure(activeforeground="#000000")
        self.Button_credit_card.configure(background="#f2ebe3")
        self.Button_credit_card.configure(compound='left')
        self.Button_credit_card.configure(cursor="hand2")
        self.Button_credit_card.configure(disabledforeground="#a3a3a3")
        self.Button_credit_card.configure(foreground="#000000")
        self.Button_credit_card.configure(highlightbackground="#d9d9d9")
        self.Button_credit_card.configure(highlightcolor="black")
        photo_location = "menu/credit_card.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button_credit_card.configure(image=_img2)
        self.Button_credit_card.configure(pady="0")
        self.Button_credit_card.configure(relief="flat")
        self.Button_credit_card.configure(command=self.credit_payment)

        self.Label6 = tk.Label(self.Frame2)
        self.Label6.place(relx=0.028, rely=0.062, height=31, width=74)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#f2ebe3")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Comic Sans MS} -size 12")
        self.Label6.configure(foreground="#6d5741")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Blended :''')

        self.Button_cancel = tk.Button(self.Frame2)
        self.Button_cancel.place(relx=0.105, rely=0.8, height=45, width=110)
        self.Button_cancel.configure(activebackground="#ececec")
        self.Button_cancel.configure(activeforeground="#000000")
        self.Button_cancel.configure(background="#f2ebe3")
        self.Button_cancel.configure(compound='left')
        self.Button_cancel.configure(cursor="hand2")
        self.Button_cancel.configure(disabledforeground="#a3a3a3")
        self.Button_cancel.configure(foreground="#000000")
        self.Button_cancel.configure(highlightbackground="#d9d9d9")
        self.Button_cancel.configure(highlightcolor="black")
        photo_location = "menu/cancel.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button_cancel.configure(image=_img3)
        self.Button_cancel.configure(pady="0")
        self.Button_cancel.configure(relief="flat")
        self.Button_cancel.configure(command=self.open_menu)

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.024, rely=0.215, height=21, width=144)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#f2ebe3")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Comic Sans MS} -size 12")
        self.Label7.configure(foreground="#6d5741")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Sweetness Level  :''')

        self.Label8 = tk.Label(self.Frame2)
        self.Label8.place(relx=0.026, rely=0.338, height=31, width=114)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#f2ebe3")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Comic Sans MS} -size 12")
        self.Label8.configure(foreground="#6d5741")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Coffee Level  :''')

        self.Label9 = tk.Label(self.Frame2)
        self.Label9.place(relx=0.028, rely=0.629, height=21, width=64)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#f2ebe3")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Comic Sans MS} -size 12")
        self.Label9.configure(foreground="#6d5741")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Straw  :''')

        self.Label10 = tk.Label(self.Frame2)
        self.Label10.place(relx=0.026, rely=0.495, height=21, width=84)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#f2ebe3")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Comic Sans MS} -size 12")
        self.Label10.configure(foreground="#6d5741")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Other  :''')

        self.Label_blended = tk.Label(self.Frame2)
        self.Label_blended.place(relx=0.178, rely=0.073, height=21, width=174)
        self.Label_blended.configure(activebackground="#f9f9f9")
        self.Label_blended.configure(activeforeground="black")
        self.Label_blended.configure(anchor='w')
        self.Label_blended.configure(background="#f2ebe3")
        self.Label_blended.configure(compound='left')
        self.Label_blended.configure(disabledforeground="#a3a3a3")
        self.Label_blended.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_blended.configure(foreground="#332615")
        self.Label_blended.configure(highlightbackground="#d9d9d9")
        self.Label_blended.configure(highlightcolor="black")
        self.Label_blended.configure(text=f'{self.data["blended"]}')

        self.Label_sweet_level = tk.Label(self.Frame2)
        self.Label_sweet_level.place(relx=0.301, rely=0.218, height=21
                , width=124)
        self.Label_sweet_level.configure(activebackground="#f9f9f9")
        self.Label_sweet_level.configure(activeforeground="black")
        self.Label_sweet_level.configure(anchor='w')
        self.Label_sweet_level.configure(background="#f2ebe3")
        self.Label_sweet_level.configure(compound='left')
        self.Label_sweet_level.configure(disabledforeground="#a3a3a3")
        self.Label_sweet_level.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_sweet_level.configure(foreground="#332615")
        self.Label_sweet_level.configure(highlightbackground="#d9d9d9")
        self.Label_sweet_level.configure(highlightcolor="black")
        self.Label_sweet_level.configure(text=f'{self.data["sugar"]}')

        self.Label_coffee_level = tk.Label(self.Frame2)
        self.Label_coffee_level.place(relx=0.257, rely=0.364, height=16
                , width=160)
        self.Label_coffee_level.configure(activebackground="#f9f9f9")
        self.Label_coffee_level.configure(activeforeground="black")
        self.Label_coffee_level.configure(anchor='w')
        self.Label_coffee_level.configure(background="#f2ebe3")
        self.Label_coffee_level.configure(compound='left')
        self.Label_coffee_level.configure(disabledforeground="#a3a3a3")
        self.Label_coffee_level.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_coffee_level.configure(foreground="#332615")
        self.Label_coffee_level.configure(highlightbackground="#d9d9d9")
        self.Label_coffee_level.configure(highlightcolor="black")
        if self.data["Type"] == "Coffee":
            if "coffee_lavel" in self.data:
                self.Label_coffee_level.configure(text=f'{self.data["coffee_lavel"]}')
            else:
                self.Label_coffee_level.configure(text=f'-')
        if self.data["Type"] == "Tea":
            self.Label_coffee_level.configure(text=f'-')

        self.Label_other = tk.Label(self.Frame2)
        self.Label_other.place(relx=0.19, rely=0.498, height=21, width=155)
        self.Label_other.configure(activebackground="#f9f9f9")
        self.Label_other.configure(activeforeground="black")
        self.Label_other.configure(anchor='w')
        self.Label_other.configure(background="#f2ebe3")
        self.Label_other.configure(compound='left')
        self.Label_other.configure(disabledforeground="#a3a3a3")
        self.Label_other.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_other.configure(foreground="#332615")
        self.Label_other.configure(highlightbackground="#d9d9d9")
        self.Label_other.configure(highlightcolor="black")
        if self.data["Type"] == "Coffee":
            if "coffee_shot" in self.data:
                if self.data["coffee_shot"] == "Yes":
                    self.Label_other.configure(text=f'Coffee Shot')
                else:
                    self.Label_other.configure(text=f'{self.data["coffee_shot"]}')
            else:
                self.Label_other.configure(text=f'-')
        if self.data["Type"] == "Tea":
            if "bubble" in self.data:
                if self.data["bubble"] == "Yes":
                    self.Label_other.configure(text=f'Bubble')
                if self.data["bubble"] == "No":
                    self.Label_other.configure(text=f'-')
            else:
                self.Label_other.configure(text=f'-')

        self.Label_straw = tk.Label(self.Frame2)
        self.Label_straw.place(relx=0.19, rely=0.618, height=30, width=184)
        self.Label_straw.configure(activebackground="#f9f9f9")
        self.Label_straw.configure(activeforeground="black")
        self.Label_straw.configure(anchor='w')
        self.Label_straw.configure(background="#f2ebe3")
        self.Label_straw.configure(compound='left')
        self.Label_straw.configure(disabledforeground="#a3a3a3")
        self.Label_straw.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_straw.configure(foreground="#332615")
        self.Label_straw.configure(highlightbackground="#d9d9d9")
        self.Label_straw.configure(highlightcolor="black")
        self.Label_straw.configure(text=f'{self.data["straw"]}')

        self.Button_cash = tk.Button(self.Frame2)
        self.Button_cash.place(relx=0.41, rely=0.8, height=45, width=110)
        self.Button_cash.configure(activebackground="#ececec")
        self.Button_cash.configure(activeforeground="#000000")
        self.Button_cash.configure(background="#f2ebe3")
        self.Button_cash.configure(compound='left')
        self.Button_cash.configure(cursor="hand2")
        self.Button_cash.configure(disabledforeground="#a3a3a3")
        self.Button_cash.configure(foreground="#000000")
        self.Button_cash.configure(highlightbackground="#d9d9d9")
        self.Button_cash.configure(highlightcolor="black")
        photo_location = "menu/cash.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button_cash.configure(image=_img4)
        self.Button_cash.configure(pady="0")
        self.Button_cash.configure(relief="flat")
        self.Button_cash.configure(command=self.cash_payment)
        

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.623, rely=0.444, height=41, width=154)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#f2ebe3")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 21")
        self.Label4.configure(foreground="#6d5741")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Price Total''')

    def open_menu(self):
        self.top.destroy()
        menu_page.main_loop()

    def open_end_page(self):
        self.top.destroy()
        end_page.main_loop()

    def cash_payment(self):
        self.pay = "cash"
        self.payment_menu()

    def credit_payment(self):
        self.pay = "credit"
        self.payment_menu()


    def payment_menu(self):
        customer_payment = main.Payment(self.pay)
        admin_wallet = main.Wallet(customer_payment.get_status())
        admin_wallet.add_wallet()
        if customer_payment.get_status() :
                self.material_check = main.Scan_Menu.material()
                if self.material_check :
                    self.open_end_page()
                else :
                    messagebox.showwarning('Notification', 'This menu is sold out.')
                    print("หมด")

def main_loop(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Payment_Page(_top1)
    root.mainloop()

if __name__ == '__main__':
    main_loop()


