import json
class Admin:

    def __init__(self):
        self._menulist = []
        self._username = "admin"
        self._password = "1234"

    def login(self,username,password):
        if username == self._username and password == self._password :
            return True
        else:
            return False

    def add_menu(self, id = '', name = '', type = '', water = '', ice = '', milk = '', milk_foam = '', price = ''):
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

        self._menulist.append({"ID" : self._id,
                            "Name" : self._name_menu,
                            "Type" : self._type,
                            "Water" : self._water,
                            "Ice" : self._ice,
                            "Milk" : self._milk,
                            "Milk_Foam" : self._milk_foam,
                            "Price" : self._price})

        
        with open('backend/menu.json', 'w') as json_file:
            json.dump(self._menulist, json_file, 
                        indent=4,  
                        separators=(',',': '))
                        
        print('Successfully Appended Menu')
    
    def get_menu(self) :
        self._menulist = json.load(open('backend/menu.json'))
        return self._menulist

    def del_menu(self, id) : 
        self._menulist = json.load(open('backend/menu.json'))

        for index,menu in enumerate(self._menulist):
            if menu["ID"] == id : 
                print(menu["ID"])
                self._menulist.pop(index)

        with open('backend/menu.json', 'w') as json_file:
            json.dump(self._menulist, json_file, 
                        indent=4,  
                        separators=(',',': '))
                        
            print('Successfully Delete Menu')

    def modify_menu(self, id, fix_menu):
        if isinstance(fix_menu, dict):
            self._menulist = json.load(open('backend/menu.json'))

            for menu in self._menulist:
                if (menu["ID"] == id):
                    menu["Name"] = fix_menu["Name"]
                    menu["Type"] = fix_menu["Type"]
                    menu["Water"] = fix_menu["Water"]
                    menu["Ice"] = fix_menu["Ice"]
                    menu["Milk"] = fix_menu["Milk"]
                    menu["Milk_Foam"] = fix_menu["Milk_Foam"]
                    menu["Price"] = fix_menu["Price"]

            with open('backend/menu.json', 'w') as json_file:
                json.dump(self._menulist, json_file, 
                            indent=4,  
                            separators=(',',': '))
                
                print('Successfully Modify Menu')
        else:
            print('error')
                           
                        
        

    def view_material(self):
        self._material = json.load(open('backend/raw_material.json'))
        return print(self._material)

    def view_wallet(self):
        self._wallet = json.load(open('backend/wallet.json'))
        return print(self._wallet)


# my_admin = Admin()
# username = input("username :")
# password = input("password :")
# print(my_admin.login(username,password))
# my_admin.view_wallet()
# my_admin.add_menu(4,"Cocoa", "Tea", 100, 50, 30, 10, 30)
# r ={'Name': 'asdasdasd', 'Type': 'Coffee', 'Water': 100, 'Ice': 20, 'Milk': 30, 'Milk_Foam': 10, 'Price': 30}
# print(r)
# my_admin.modify_menu(5, r)
# my_admin.del_menu(3)

# print(menu.get_menu())
# for i in range(0, len(my_admin.get_menu())) :
#     print(my_admin.get_menu()[i]["Name"])


