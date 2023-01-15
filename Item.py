import json
from Character import *

# \\\_-_-_-_-_-_-_{[|^/---\^|]}_-_-_-_-_-_-_/// #
def json_objet(class_name, nom_item):
  with open ('resources\\json_datas\\items.json', "r", encoding='utf-8') as f :
      data = json.load(f)
  get_inventory = data["item"]
  get_id = get_inventory
  return get_id[class_name][nom_item]

class Objet:
  def __init__(self, item):
    self.name = item['name']
  
  def get_name(self) :
    return self.name

class Potion(Objet):
  def __init__(self, item, quantity):
    super().__init__(item)
    self.description = item['description']
    self.value = item['effect']['value']
    self.type_buff = item['effect']['type']
    self.quantity = quantity

  def get_description(self) :
    return self.description

  def get_value(self) :
    return self.value

  def get_type_buff(self) :
    return self.type_buff

  def get_quantity(self) :
    return self.quantity

  def is_potion(self) :
    if self.get_quantity() > 0 :
      return True
    else :
      return False

  def decrease_value(self) :
    if self.get_quantity() >= 1 :
      self.quantity -= 1
    else :
      print("Erreur, on ne peut pas décrémenter")

  def use_potion(self, character) :
    # verifie si le personnage a le max d'hp
    if self.get_type_buff() == 'hp' :
      if character.get_hp() >= character.get_hp_max() :
        print(f"{character.get_name()} a déjà ses HP au max !\n")
        return False
      else :
        # si il lui manque des hp, on decremente la quantité de la potion
        # on verifie si la potion lui donne plus d'hp qu'il est censé en avoir
        self.decrease_value()
        print("")
        print(f"[{self.get_name()}] a été consommée.")
        heal = int(character.get_hp_max() * self.get_value())
        if character.get_hp() + heal >= character.get_hp_max() :
          character.set_hp(character.get_hp_max())
          print(f"{character.get_name()} a récupéré {character.get_hp() + heal - character.get_hp_max()} HP.")
          print(f"{character.get_name()} a {character.get_hp()} HP.")

        else :
          character.set_hp(character.get_hp() + heal)
          print(f"{character.get_name()} a récupéré {heal} HP.")
          print(f"{character.get_name()} a {character.get_hp()} HP.")
        return True

    # pareil pour les mp
    elif self.get_type_buff() == 'mp' :
      if character.get_mp() >= character.get_mp_max() :
        print(f"{character.get_name()} a déjà ses MP au max !\n")
        return False
      else :
        self.decrease_value()
        print("")
        print(f"[{self.get_name()}] a été consommée.")
        regen_mp = int(character.get_mp_max() * self.get_value())
        if character.get_mp() + regen_mp >= character.get_mp_max() :
          character.set_hp(character.get_mp_max())
          print(f"{character.get_name()} a récupéré {character.get_mp() + regen_mp - character.get_mp_max()} MP.")
          print(f"{character.get_name()} a {character.get_hp()} MP.")

        else :
          character.set_hp(character.get_mp() + regen_mp)
          print(f"{character.get_name()} a récupéré {regen_mp} MP.")
          print(f"{character.get_name()} a {character.get_mp()} MP.")
          return True

class Potion_de_buff(Potion):
  def __init__(self, item, quantity):
    super().__init__(item, quantity)
    self.tour = item['effect']['tour']

  def use_potion(self, character) :
    if self.get_type_buff() == 'str':
      if character.get_is_buff_str() :
        print(f"{character.get_name()} deux fois {self.get_name()} en même temps !")
        return False
      else :
        self.decrease_value()
        str_bonus = round(character.get_attack() * self.get_value())
        character.set_is_buff_str(True)
        character.set_current_attack(character.get_attack() + str_bonus)
        print("")
        print(f"[{self.get_name()}] a été consommée.")
        print(f"{character.get_name()} obtient un bonus de {round(self.get_value() * 100)} % d'attaque pendant 3 tours !")
        print(f"{character.get_name()} gagne {str_bonus} d'ATK !")
        return True

        
    elif self.get_type_buff() == 'spd':
      if character.get_is_buff_spd() :
        print(f"{character.get_name()} deux fois {self.get_name()} en même temps !")
        return False
      else :
        self.decrease_value()
        spd_bonus = round(character.get_attack() * self.get_value())
        character.set_is_buff_spd(True)
        character.set_current_speed(character.get_speed() + spd_bonus)
        print("")
        print(f"[{self.get_name()}] a été consommée.")
        print(f"{character.get_name()} obtient un bonus de {round(self.get_value() * 100)} % de vitesse pendant 3 tours !")
        print(f"{character.get_name()} gagne {spd_bonus} de SPD !")
        return True

    elif self.get_type_buff() == 'resistance':
      if character.get_is_buff_res() :
        print(f"{character.get_name()} deux fois {self.get_name()} en même temps !")
        return False
      else :
        self.decrease_value()
        character.set_is_buff_res(True)
        character.set_current_resistance(self.get_value())
        print(f"[{self.get_name()}] a été consommée.")
        print(f"{character.get_name()} obtient un bonus de + {self.get_value()} sur toutes ses résistances pendant 3 tours !")
        character.print_current_resistance()
        return True

    elif self.get_type_buff() == 'ressurection' :
      if character.is_dead() :
        self.decrease_value()
        print(f"[{self.get_name()}] a été consommée.")
        character.set_hp(round(character.get_hp_max() * self.get_value()))
        print(f"{character.get_name()} a été ressucité et 50 % de ses HP max ont été restauré.")
        print("")
        return True
      else :
        print(f"\n{character.get_name()} n'est pas mort !")
        False