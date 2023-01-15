from Monster import Monster
from Skill_boss import Skill_boss
from Loot_monster import Loot_monster

import json
with open ("..\\json\\monsters.json", "r", encoding= "utf-8") as f :
    data = json.load(f)
get_monsters = data["boss"]
get_id = get_monsters[0]
info_loki = get_id["1"]

class Boss(Monster):

    def __init__(self, info_monster):
        super().__init__(info_monster)
        self.skill_1 = Skill_boss(info_monster["skills"]["skill1"])
        self.skill_2 = Skill_boss(info_monster["skills"]["skill2"])
        self.ultime = Skill_boss(info_monster["skills"]["ultime"])
        self.loot2 = Loot_monster(info_monster["loot"]["item2"])


    def get_skill_2(self):
        return self.skill_2

    def get_ultime(self):
        return self.ultime

    def get_loot2(self):
        return self.loot2