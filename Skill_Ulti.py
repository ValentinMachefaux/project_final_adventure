from Skill import Skill

class Skill_ulti(Skill) :
    def __init__(self, info_skill):
        super().__init__(info_skill)
        self.rp = info_skill['rp']

    def get_rp(self):
        return self.rp