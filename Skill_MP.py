from Skill import Skill

class Skill_mp(Skill) :
    def __init__(self, info_skill):
        super().__init__(info_skill)
        self.mp = info_skill['MP']
        self.cd = info_skill['CD']

    def get_mp(self):
        return self.mp

    def get_cd(self):
        return self.cd
