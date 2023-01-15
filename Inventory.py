from Item import *

class Inventory:

    def __init__(self):
        self.inventory = {}
        self.potion_hp = Potion(json_objet('potion', 'hp'), 10)
        self.potion_mp = Potion(json_objet('potion', 'mp'), 10)
        self.potion_str = Potion_de_buff(json_objet('potion_buff', 'str'), 1)
        self.potion_spd = Potion_de_buff(json_objet('potion_buff', 'spd'), 1)
        self.potion_res = Potion_de_buff(json_objet('potion_buff', 'res'), 1)
        self.ankh = Potion_de_buff(json_objet('divers', 'ankh'), 1)


    def get_inventory(self):
        return self.inventory

    def update_item(self, item, quantity):
        for key, value in list(self.inventory.items()):
            if key.get_name() == item.get_name() :
                value += quantity
                self.inventory.update({key : value})

    def get_len_inventory(self):
        # return 6
        return len(self.inventory)

    def remove_objet(self, item):
        self.inventory.remove(item)

    def init_inventory(self) :
        self.inventory.update({self.potion_hp: self.potion_hp.get_quantity()})
        self.inventory.update({self.potion_mp: self.potion_mp.get_quantity()})
        self.inventory.update({self.potion_str: self.potion_str.get_quantity()})
        self.inventory.update({self.potion_res: self.potion_res.get_quantity()})
        self.inventory.update({self.potion_spd: self.potion_spd.get_quantity()})
        self.inventory.update({self.ankh: self.ankh.get_quantity()})

    def print_inventory(self) :
        print("\t[INVENTAIRE]\n")
        if len(self.inventory) == 0 :
            print("Votre inventaire est actuellement vide.\n")
        else :
            for index, (key, value) in enumerate(self.inventory.items()):
                print(f"[{index}] {value} x [{key.get_name()}]")
            print(f"[{self.get_len_inventory()}] Retour")
            
    def menu_detail_inventory(self, choice) :
        for index, (key, value) in enumerate(self.inventory.items()):
            if choice == index : 
                print(f"\n\t[{key.get_name().upper()}]\n")
                print(f"[1] Utiliser [{key.get_name()}]\n[2] Description de [{key.get_name()}]\n[3] Retour")

    def get_description(self, choice) :
        for index, (key, value) in enumerate(self.inventory.items()):
            if choice == index : 
                print(f"\n\t[DESCRIPTION DE {key.get_name().upper()}]\n")
                print(f"{key.get_description()}")

# i = Inventory()
# i.init_inventory()
# i.print_inventory()

# potion_hp = Potion_de_vie(json_objet('potion', 'hp'), 0)
# potion_hp2 = Potion_de_vie(json_objet('potion', 'hp'), 0)

# i.update_item(potion_hp, 1)
# i.update_item(potion_hp2, 1)

# print("\nAprès ajout de 2 x popo hp\n")

# i.print_inventory()
# print(i.get_len_inventory())
