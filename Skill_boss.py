from Skill_monster import Skill_monster

class Skill_boss(Skill_monster):
    def __init__(self, info_skill):
        super().__init__(info_skill)
        self.cd = info_skill["effect"]["cooldown"]

    def get_cd(self):
        return self.cd