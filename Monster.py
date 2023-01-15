from Skill_monster import Skill_monster
from Loot_monster import Loot_monster
import random

import json

def json_monster(monster_id):

    with open ("resources\\json_datas\\monsters.json", "r", encoding= "utf-8") as f :
        data = json.load(f)
    get_monsters = data["monsters"]
    get_id = get_monsters[0]
    return get_id[monster_id]

class Monster:

    def __init__(self, info_monster):
        self.name = info_monster["name"]
        self.level = info_monster["level"]
        self.hp = info_monster["hp"]
        self.attack = info_monster["attack"]
        self.current_attack = info_monster["attack"]
        self.current_speed = info_monster["spd"]

        self.defense = info_monster["defense"]
        self.spd = info_monster["spd"]
        self.accuracy = info_monster["accuracy"]
        self.weakness = info_monster["weakness"]
        self.resistance = info_monster["resistance"]
        self.skill_1 = Skill_monster(info_monster["skills"]["skill1"])
        self.detail = info_monster["description"]
        self.exp = info_monster["exp"]
        self.gold = info_monster["gold"]
        self.sprite = info_monster["sprite"]
        self.loot1 = Loot_monster(info_monster["loot"]["item1"])
        self.is_boss = info_monster["is_boss"]

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level
    
    def get_hp(self):
        return self.hp

    def set_hp(self, hp) :
        self.hp = hp
    
    def get_attack(self):
        return self.attack

    def get_current_attack(self):
        return self.current_attack

    def get_current_speed(self):
        return self.current_speed

    def get_current_speed(self):
        return self.current_speed

    def set_current_attack(self, attack) :
        self.current_attack = attack
    
    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.spd
    
    def get_accuracy(self):
        return self.accuracy

    def get_weakness(self):
        return self.weakness

    def get_resistance(self):
        return self.resistance

    def get_skill_1(self):
        return self.skill_1
    
    def get_detail(self):
        return self.detail
    
    def get_exp(self):
        return self.exp

    def get_gold(self):
        return self.gold

    def get_sprite(self):
        return self.sprite

    def get_loot1(self):
        return self.loot1

    def get_is_boss(self):
        return self.is_boss

    def is_dead(self) :
        if self.hp <= 0 :
            return True
        else :
            return False
