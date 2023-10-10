
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from traceback import print_list

import menu_page
import payment_page
from backend import main
import json
from tkinter import messagebox

class Coffee_Page:
        
    def __init__(self, top=None, arg1=None):
        self.name = arg1
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

        top.geometry("600x700+462+31")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Ship_Ba_Coffee")
        top.configure(background="#d1c9ad")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.checkbox1 = tk.IntVar()
        self.checkbox2 = tk.IntVar()
        self.checkbox3 = tk.IntVar()
        self.checkbox4 = tk.IntVar()
        self.checkbox5 = tk.IntVar()
        self.checkbox6 = tk.IntVar()
        self.checkbox7 = tk.IntVar()
        self.topping_check = tk.IntVar()
        self.straw_check = tk.IntVar()

        # self.true_var = tk.IntVar()
        self.image_coffee = tk.Label(self.top)
        self.image_coffee.place(relx=0.267, rely=0.029, height=175, width=266)
        self.image_coffee.configure(activebackground="#f9f9f9")
        self.image_coffee.configure(activeforeground="black")
        self.image_coffee.configure(anchor='w')
        self.image_coffee.configure(background="#d1c9ad")
        self.image_coffee.configure(borderwidth="45")
        self.image_coffee.configure(compound='left')
        self.image_coffee.configure(disabledforeground="#a3a3a3")
        self.image_coffee.configure(foreground="#d1c9ad")
        self.image_coffee.configure(highlightbackground="#d9d9d9")
        self.image_coffee.configure(highlightcolor="black")
        photo_location = f'./menu/{self.name}.png'
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.image_coffee.configure(image=_img0)

        self.Frame1 = tk.LabelFrame(self.top)
        self.Frame1.place(relx=0.05, rely=0.357, relheight=0.123, relwidth=0.9)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(font="-family {Comic Sans MS} -size 12 -underline 1")
        self.Frame1.configure(foreground="#400000")
        self.Frame1.configure(text='''SWEETNESS LEVEL''')
        self.Frame1.configure(background="#f2ebe3")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.checkbox_1 = tk.Checkbutton(self.Frame1)
        self.checkbox_1.place(relx=0.056, rely=0.465, relheight=0.291
                , relwidth=0.2, bordermode='ignore')
        self.checkbox_1.configure(activebackground="#ececec")
        self.checkbox_1.configure(activeforeground="#000000")
        self.checkbox_1.configure(anchor='w')
        self.checkbox_1.configure(background="#f2ebe3")
        self.checkbox_1.configure(compound='left')
        self.checkbox_1.configure(cursor="hand2")
        self.checkbox_1.configure(disabledforeground="#a3a3a3")
        self.checkbox_1.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_1.configure(foreground="#513820")
        self.checkbox_1.configure(highlightbackground="#d9d9d9")
        self.checkbox_1.configure(highlightcolor="black")
        self.checkbox_1.configure(justify='left')
        self.checkbox_1.configure(text='''No Sugar''')
        self.checkbox_1.configure(variable=self.checkbox1)
        


        self.checkbox_2 = tk.Checkbutton(self.Frame1)
        self.checkbox_2.place(relx=0.296, rely=0.465, relheight=0.291
                , relwidth=0.237, bordermode='ignore')
        self.checkbox_2.configure(activebackground="#3c2917")
        self.checkbox_2.configure(activeforeground="white")
        self.checkbox_2.configure(activeforeground="#000000")
        self.checkbox_2.configure(anchor='w')
        self.checkbox_2.configure(background="#f2ebe3")
        self.checkbox_2.configure(compound='left')
        self.checkbox_2.configure(cursor="hand2")
        self.checkbox_2.configure(disabledforeground="#a3a3a3")
        self.checkbox_2.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_2.configure(foreground="#513820")
        self.checkbox_2.configure(highlightbackground="#d9d9d9")
        self.checkbox_2.configure(highlightcolor="black")
        self.checkbox_2.configure(justify='left')
        self.checkbox_2.configure(text='''Less Sweet''')
        self.checkbox_2.configure(variable=self.checkbox2)

        self.checkbox_3 = tk.Checkbutton(self.Frame1)
        self.checkbox_3.place(relx=0.574, rely=0.465, relheight=0.291
                , relwidth=0.181, bordermode='ignore')
        self.checkbox_3.configure(activebackground="#ececec")
        self.checkbox_3.configure(activeforeground="#000000")
        self.checkbox_3.configure(anchor='w')
        self.checkbox_3.configure(background="#f2ebe3")
        self.checkbox_3.configure(compound='left')
        self.checkbox_3.configure(cursor="hand2")
        self.checkbox_3.configure(disabledforeground="#a3a3a3")
        self.checkbox_3.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_3.configure(foreground="#513820")
        self.checkbox_3.configure(highlightbackground="#d9d9d9")
        self.checkbox_3.configure(highlightcolor="black")
        self.checkbox_3.configure(justify='left')
        self.checkbox_3.configure(text='''Normal''')
        self.checkbox_3.configure(variable=self.checkbox3)

        self.checkbox_4 = tk.Checkbutton(self.Frame1)
        self.checkbox_4.place(relx=0.796, rely=0.465, relheight=0.291
                , relwidth=0.163, bordermode='ignore')
        self.checkbox_4.configure(activebackground="#ececec")
        self.checkbox_4.configure(activeforeground="#000000")
        self.checkbox_4.configure(anchor='w')
        self.checkbox_4.configure(background="#f2ebe3")
        self.checkbox_4.configure(compound='left')
        self.checkbox_4.configure(cursor="fleur")
        self.checkbox_4.configure(disabledforeground="#a3a3a3")
        self.checkbox_4.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_4.configure(foreground="#513820")
        self.checkbox_4.configure(highlightbackground="#d9d9d9")
        self.checkbox_4.configure(highlightcolor="black")
        self.checkbox_4.configure(justify='left')
        self.checkbox_4.configure(text='''Sweet''')
        self.checkbox_4.configure(variable=self.checkbox4)

        self.Frame2 = tk.LabelFrame(self.top)
        self.Frame2.place(relx=0.05, rely=0.5, relheight=0.121, relwidth=0.9)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(font="-family {Comic Sans MS} -size 12 -underline 1")
        self.Frame2.configure(foreground="#400000")
        self.Frame2.configure(text='''COFFEE INTENSITY LEVEL''')
        self.Frame2.configure(background="#f2ebe3")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.checkbox_5 = tk.Checkbutton(self.Frame2)
        self.checkbox_5.place(relx=0.063, rely=0.494, relheight=0.329
                , relwidth=0.237, bordermode='ignore')
        self.checkbox_5.configure(activebackground="#ececec")
        self.checkbox_5.configure(activeforeground="#000000")
        self.checkbox_5.configure(anchor='w')
        self.checkbox_5.configure(background="#f2ebe3")
        self.checkbox_5.configure(compound='left')
        self.checkbox_5.configure(cursor="hand2")
        self.checkbox_5.configure(disabledforeground="#a3a3a3")
        self.checkbox_5.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_5.configure(foreground="#513820")
        self.checkbox_5.configure(highlightbackground="#d9d9d9")
        self.checkbox_5.configure(highlightcolor="black")
        self.checkbox_5.configure(justify='left')
        self.checkbox_5.configure(text='''Light Roast''')
        self.checkbox_5.configure(variable=self.checkbox5)

        self.checkbox_6 = tk.Checkbutton(self.Frame2)
        self.checkbox_6.place(relx=0.352, rely=0.471, relheight=0.341
                , relwidth=0.274, bordermode='ignore')
        self.checkbox_6.configure(activebackground="#ececec")
        self.checkbox_6.configure(activeforeground="#000000")
        self.checkbox_6.configure(background="#f2ebe3")
        self.checkbox_6.configure(compound='left')
        self.checkbox_6.configure(cursor="hand2")
        self.checkbox_6.configure(disabledforeground="#a3a3a3")
        self.checkbox_6.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_6.configure(foreground="#513820")
        self.checkbox_6.configure(highlightbackground="#d9d9d9")
        self.checkbox_6.configure(highlightcolor="black")
        self.checkbox_6.configure(justify='left')
        self.checkbox_6.configure(text='''Medium Roast''')
        self.checkbox_6.configure(variable=self.checkbox6)

        self.checkbox_7 = tk.Checkbutton(self.Frame2)
        self.checkbox_7.place(relx=0.704, rely=0.471, relheight=0.329
                , relwidth=0.237, bordermode='ignore')
        self.checkbox_7.configure(activebackground="#ececec")
        self.checkbox_7.configure(activeforeground="#000000")
        self.checkbox_7.configure(background="#f2ebe3")
        self.checkbox_7.configure(compound='left')
        self.checkbox_7.configure(cursor="hand2")
        self.checkbox_7.configure(disabledforeground="#000000")
        self.checkbox_7.configure(font="-family {Comic Sans MS} -size 14")
        self.checkbox_7.configure(foreground="#513820")
        self.checkbox_7.configure(highlightbackground="#000000")
        self.checkbox_7.configure(highlightcolor="black")
        self.checkbox_7.configure(justify='left')
        self.checkbox_7.configure(text='''Dark Roast''')
        self.checkbox_7.configure(variable=self.checkbox7)

        self.Frame3 = tk.LabelFrame(self.top)
        self.Frame3.place(relx=0.05, rely=0.643, relheight=0.093, relwidth=0.9)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(font="-family {Comic Sans MS} -size 12 -underline 1")
        self.Frame3.configure(foreground="#400000")
        self.Frame3.configure(text='''EXTRA TOPPING''')
        self.Frame3.configure(background="#f2ebe3")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Checkbutton_toppimg = tk.Checkbutton(self.Frame3)
        self.Checkbutton_toppimg.place(relx=0.926, rely=0.308, relheight=0.538
                , relwidth=0.057, bordermode='ignore')
        self.Checkbutton_toppimg.configure(activebackground="#ececec")
        self.Checkbutton_toppimg.configure(activeforeground="#000000")
        self.Checkbutton_toppimg.configure(anchor='w')
        self.Checkbutton_toppimg.configure(background="#f2ebe3")
        self.Checkbutton_toppimg.configure(compound='left')
        self.Checkbutton_toppimg.configure(cursor="hand2")
        self.Checkbutton_toppimg.configure(disabledforeground="#a3a3a3")
        self.Checkbutton_toppimg.configure(foreground="#000000")
        self.Checkbutton_toppimg.configure(highlightbackground="#d9d9d9")
        self.Checkbutton_toppimg.configure(highlightcolor="black")
        self.Checkbutton_toppimg.configure(justify='left')
        self.Checkbutton_toppimg.configure(variable=self.topping_check)

        self.Label3 = tk.Label(self.Frame3)
        self.Label3.place(relx=0.056, rely=0.462, height=21, width=244
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#f2ebe3")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Comic Sans MS} -size 14")
        self.Label3.configure(foreground="#513820")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''1 Shot of Espresso (+10฿)''')

        self.Frame4 = tk.LabelFrame(self.top)
        self.Frame4.place(relx=0.05, rely=0.757, relheight=0.093, relwidth=0.9)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(font="-family {Comic Sans MS} -size 12 -underline 1")
        self.Frame4.configure(foreground="#400000")
        self.Frame4.configure(text='''STRAW''')
        self.Frame4.configure(background="#f2ebe3")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Checkbutton_straw = tk.Checkbutton(self.Frame4)
        self.Checkbutton_straw.place(relx=0.926, rely=0.308, relheight=0.538
                , relwidth=0.039, bordermode='ignore')
        self.Checkbutton_straw.configure(activebackground="#ececec")
        self.Checkbutton_straw.configure(activeforeground="#000000")
        self.Checkbutton_straw.configure(anchor='w')
        self.Checkbutton_straw.configure(background="#f2ebe3")
        self.Checkbutton_straw.configure(compound='left')
        self.Checkbutton_straw.configure(cursor="hand2")
        self.Checkbutton_straw.configure(disabledforeground="#a3a3a3")
        self.Checkbutton_straw.configure(foreground="#000000")
        self.Checkbutton_straw.configure(highlightbackground="#d9d9d9")
        self.Checkbutton_straw.configure(highlightcolor="black")
        self.Checkbutton_straw.configure(justify='left')
        self.Checkbutton_straw
        self.Checkbutton_straw.configure(variable=self.straw_check)

        self.Label4 = tk.Label(self.Frame4)
        self.Label4.place(relx=0.074, rely=0.462, height=21, width=164
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#f2ebe3")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 14")
        self.Label4.configure(foreground="#513820")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''I want a straw''')

        self.Button_next = tk.Button(self.top)
        self.Button_next.place(relx=0.767, rely=0.914, height=54, width=117)
        self.Button_next.configure(activebackground="#ececec")
        self.Button_next.configure(activeforeground="#000000")
        self.Button_next.configure(background="#d1c9ad")
        self.Button_next.configure(borderwidth="0")
        self.Button_next.configure(compound='left')
        self.Button_next.configure(disabledforeground="#a3a3a3")
        self.Button_next.configure(foreground="#d1c9ad")
        self.Button_next.configure(highlightbackground="#d9d9d9")
        self.Button_next.configure(highlightcolor="black")
        photo_location = "./menu/next.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button_next.configure(image=_img1)
        self.Button_next.configure(pady="0")
        self.Button_next.configure(relief="groove")
        self.Button_next.configure(command=self.open_payment_page)

        self.Combobox_blended = ttk.Combobox(self.top)
        self.Combobox_blended.place(relx=0.463, rely=0.31, relheight=0.03
                , relwidth=0.188)
        self.Combobox_blended.configure(textvariable=self.combobox)
        self.Combobox_blended.configure(takefocus="")
        self.Combobox_blended.configure(values=["Hot", "Cool", "Mix"])

        self.Label_blended = tk.Label(self.top)
        self.Label_blended.place(relx=0.318, rely=0.304, height=31, width=84)
        self.Label_blended.configure(activebackground="#f9f9f9")
        self.Label_blended.configure(activeforeground="black")
        self.Label_blended.configure(anchor='w')
        self.Label_blended.configure(background="#d1c9ad")
        self.Label_blended.configure(compound='left')
        self.Label_blended.configure(disabledforeground="#a3a3a3")
        self.Label_blended.configure(font="-family {Comic Sans MS} -size 12")
        self.Label_blended.configure(foreground="#400000")
        self.Label_blended.configure(highlightbackground="#d9d9d9")
        self.Label_blended.configure(highlightcolor="black")
        self.Label_blended.configure(text='''BLENDED''')
        
        self.Button_back = tk.Button(self.top)
        self.Button_back.place(relx=0.033, rely=0.914, height=54, width=117)
        self.Button_back.configure(activebackground="#ececec")
        self.Button_back.configure(activeforeground="#000000")
        self.Button_back.configure(background="#d1c9ad")
        self.Button_back.configure(borderwidth="0")
        self.Button_back.configure(compound='left')
        self.Button_back.configure(disabledforeground="#a3a3a3")
        self.Button_back.configure(foreground="#d1c9ad")
        self.Button_back.configure(highlightbackground="#d9d9d9")
        self.Button_back.configure(highlightcolor="black")
        photo_location = "./menu/back.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button_back.configure(image=_img2)
        self.Button_back.configure(pady="0")
        self.Button_back.configure(relief="groove")
        self.Button_back.configure(command=self.open_menu_page)

        self.Logo_icon = tk.Label(self.top)
        self.Logo_icon.place(relx=0.017, rely=0.014, height=63, width=74)
        self.Logo_icon.configure(activebackground="#f9f9f9")
        self.Logo_icon.configure(activeforeground="black")
        self.Logo_icon.configure(anchor='w')
        self.Logo_icon.configure(background="#d1c9ad")
        self.Logo_icon.configure(compound='left')
        self.Logo_icon.configure(disabledforeground="#a3a3a3")
        self.Logo_icon.configure(foreground="#000000")
        self.Logo_icon.configure(highlightbackground="#d9d9d9")
        self.Logo_icon.configure(highlightcolor="black")
        photo_location = "./menu/Logo3.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Logo_icon.configure(image=_img3)

    def open_menu_page(self):
        self.top.destroy()
        menu_page.main_loop()

    def open_payment_page(self):
        if self.checkbox1.get() == 1 :
                self.sugar = '0'
        elif self.checkbox2.get() == 1 :
                self.sugar = '25'
        elif self.checkbox3.get() == 1 :
                self.sugar = '50'
        elif self.checkbox4.get() == 1 :
                self.sugar = '75'

        if self.checkbox5.get() == 1 :
                self.coffee_lavel = 'Light Roast'
        elif self.checkbox6.get() == 1 :
                self.coffee_lavel = 'Medium Roast'
        elif self.checkbox7.get() == 1 :
                self.coffee_lavel = 'Dark Roast'

        if self.topping_check.get() == 1 :
                self.coffee_shot = 'Yes'
        else :
                self.coffee_shot = 'No'

        if self.straw_check.get() == 1 :
                self.straw = 'Yes'
        else :
                self.straw = 'No'

        main.Customer.selected(self.name)
        menu_chack = main.Menu_Coffee
        try:
                menu_chack.selected_menu_coffee(self.coffee_lavel, self.coffee_shot, self.sugar, self.Combobox_blended.get(), self.straw)
                # with open('backend/receipt.json', 'w') as json_file:
                #         json.dump(data, json_file)     
                self.top.destroy()
                payment_page.main_loop()
        except: 
                messagebox.showerror("Error", "Please choose sweetness and coffee level.")
                print("error")

def main_loop(arg):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    # _w1 = coffee_page.Toplevel1(_top1)
    _w1 = Coffee_Page(_top1,arg)
    root.mainloop()


if __name__ == '__main__':
    main_loop()

