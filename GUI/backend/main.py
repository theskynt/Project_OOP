import json

class Customer():

    # @staticmethod
    # def show_menu():
    #     menulist = json.load(open('backend/menu.json'))
    #     for menu in range(0, len(menulist)):
    #         print(menulist[menu]["Name"])

    @staticmethod
    def selected(name):
        return Page_Menu.selected_menu(name)


class Page_Menu():
    menu = {}
    def __init__(self, id = '', name = '', type = '', water = '', ice = '', milk = '', milk_foam = '', price = '',**kwargs):
        super().__init__(**kwargs)
        self._menulist = []
        self._id = id
        self._name_menu = name
        self._type = type
        self._water = water
        self._ice = ice
        self._milk = milk
        self._milk_foam = milk_foam
        self._price = price
        self._menulist = json.load(open('backend/menu.json'))

    @staticmethod
    def selected_menu(name):
        menulist = json.load(open('backend/menu.json'))
        for index,menu in enumerate(menulist):
            if menu["Name"] == name:
                Page_Menu.menu.update(menulist[index])
                return Page_Menu.menu['Type']
            
    @staticmethod
    def print_menu():
        menu_now = {}
        id = Page_Menu.menu["ID"]
        name = Page_Menu.menu["Name"]
        type = Page_Menu.menu["Type"]
        water = Page_Menu.menu["Water"]
        ice = Page_Menu.menu["Ice"]
        milk = Page_Menu.menu["Milk"]
        milk_foam = Page_Menu.menu["Milk_Foam"]
        price = Page_Menu.menu["Price"]

        menu_now.update({"ID" : id})
        menu_now.update({"Name" : name})
        menu_now.update({"Type" : type})
        menu_now.update({"Water" : water})
        menu_now.update({"Ice" : ice})
        menu_now.update({"Milk" : milk})
        menu_now.update({"Milk_Foam" : milk_foam})
        menu_now.update({"Price" : price})
        return menu_now

class Page_Tea():
    def __init__(self, bubble = '', **kwargs):
        super().__init__(**kwargs)
        self._bubble = bubble

    @staticmethod
    def add_bubble(bubble):
        menu_now = {}

        menu_now.update({"bubble" : bubble})
        return menu_now

class Page_Coffee():
    def __init__(self, coffee_lavel = '', coffee_shot = '', **kwargs):
        super().__init__(**kwargs)
        self._coffee_lavel : coffee_lavel
        self._coffee_shot : coffee_shot

    @staticmethod
    def add_coffee(coffee_lavel, coffee_shot):
        menu_now = {}
        
        menu_now.update({"coffee_lavel" : coffee_lavel})
        menu_now.update({"coffee_shot" : coffee_shot})
        return menu_now


class Page_Add_other():

    def __init__(self, sugar = '', blended = '', straw = '',**kwargs):
        super().__init__(**kwargs)
        self._sugar = sugar
        self._blended = blended
        self._straw = straw

    @staticmethod
    def add_other(sugar, blended, straw):
        menu_now = {}
        
        menu_now.update({"sugar" : sugar})
        menu_now.update({"blended" : blended})
        menu_now.update({"straw" : straw})
        return menu_now

class Menu_Tea(Page_Menu, Page_Tea, Page_Add_other):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def selected_menu_tea(bubble, sugar, blended, straw):
        menu = Page_Menu.print_menu()
        bubble_dict = Page_Tea.add_bubble(bubble)
        other = Page_Add_other.add_other(sugar, blended, straw)
        listmenu_tea = menu | bubble_dict | other
        with open('backend/receipt.json', 'w') as json_file:
                        json.dump(listmenu_tea, json_file)  
        return listmenu_tea


class Menu_Coffee(Page_Menu, Page_Coffee, Page_Add_other):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def selected_menu_coffee(coffee_lavel, coffee_shot, sugar, blended, straw):
        menu = Page_Menu.print_menu()
        coffee = Page_Coffee.add_coffee(coffee_lavel, coffee_shot)
        other = Page_Add_other.add_other(sugar, blended, straw)
        listmenu_coffee = menu | coffee | other
        with open('backend/receipt.json', 'w') as json_file:
                        json.dump(listmenu_coffee, json_file)  
        return listmenu_coffee
        
class Scan_Menu():

    @staticmethod
    def calculate():
        menu = json.load(open('backend/receipt.json', 'r'))
        type = menu["Type"]
        price = int(menu["Price"])
        try:
            if type == "Tea" :
                if menu["bubble"] == "Yes" :
                    price += 10
                if menu["blended"] == "Cool" :
                    price += 5
                if menu["blended"] == "Mix" :
                    price += 10
            elif type == "Coffee" :
                if menu["coffee_shot"] == "Yes" :
                    price += 10
                if menu["blended"] == "Cool" :
                    price += 5
                if menu["blended"] == "Mix" :
                    price += 10
            return price
        except: 
            print("error calculate")

    @staticmethod
    def material():
        menu = json.load(open('backend/receipt.json', 'r'))
        raw = json.load(open('backend/raw_material.json', 'r'))
        type = menu["Type"]
        try:
            if type == "Tea" :
                tea = int(raw["tea_coco"]) - 20
                raw["tea_coco"] = tea
                if menu["bubble"] == "Yes" :
                    bubble = int(raw["bubble"]) - 1
                    raw["bubble"] = bubble

            elif type == "Coffee" :
                coffee = int(raw["coffee"]) - 20
                raw["coffee"] = coffee
                if menu["coffee_shot"] == "Yes" :
                    coffee -= 10
                    raw["coffee"] = coffee

            if menu["straw"] == "Yes" :
                straw = int(raw["straw"]) - 1
                raw["straw"] = straw
        except: 
            print("error material")

        water = int(raw["Water"]) - int(menu["Water"])
        ice = int(raw["Ice"]) - int(menu["Ice"])
        milk = int(raw["Milk"]) - int(menu["Milk"])
        milk_foam = int(raw["Milk_Foam"]) - int(menu["Milk_Foam"])
        sugar = int(raw["sugar"]) - int(menu["sugar"])
        
        raw["Water"] = water
        raw["Ice"] = ice
        raw["Milk"] = milk
        raw["Milk_Foam"] = milk_foam
        raw["sugar"] = sugar
        
        if raw["coffee"] < 0 or raw["tea_coco"] < 0 or raw["Water"] < 0 or raw["Ice"] < 0 or raw["Milk"] < 0 or raw["Milk_Foam"] < 0 or raw["bubble"] < 0 or raw["sugar"] < 0 or raw["straw"] < 0  :
            return False
        else:
            raw_up = open('backend/raw_material.json', 'w')
            json.dump(raw, raw_up)
            return True


class Payment():

    def __init__(self,pay):
        self._status = Payment.transaction(pay)

    @staticmethod
    def transaction(pay) :
        if pay == "cash" or pay == "credit" :
            return True
        else :
            return False

    def get_status(self):
        return self._status


class Wallet():

    def __init__(self, status):
        self._total = json.load(open('backend/wallet.json', 'r'))
        self._wallet = int(self._total["Total Amount"])
        self._status = status

    def add_wallet(self) :
        if self._status == True :
            price = Scan_Menu.calculate()
            self._total["Total Amount"] = self._wallet + price
            total_up = open('backend/wallet.json', 'w')
            json.dump(self._total, total_up)
        else:
            print("Cancel")
            pass

