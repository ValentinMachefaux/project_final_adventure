class Skill_monster:
    def __init__(self, info_skill):
        self.name = info_skill["name"]
        self.value = info_skill["effect"]["value"]
        self.skill_type = info_skill["effect"]["type"]
        self.element = info_skill["effect"]["element"]

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
    
    def get_skill_type(self):
        return self.skill_type
        
    def get_element(self):
        return self.element