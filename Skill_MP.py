from Skill import Skill

class Skill_mp(Skill) :
    def __init__(self, info_skill):
        super().__init__(info_skill)
        self.mp = info_skill['mp']
        self.cd = info_skill['cd']
        self.current_cd = self.cd

    def get_mp(self):
        return self.mp

    def get_cd(self):
        return self.cd

    def get_current_cd(self):
        return self.current_cd
    
    def set_current_cd(self, cd):
        if cd >= self.cd :
            self.current_cd = self.cd
        else :
            self.current_cd = cd

    def equals_cd(self) :
        if self.current_cd == self.cd :
            # on peut utiliser le skill
            return True
        else :
            return False