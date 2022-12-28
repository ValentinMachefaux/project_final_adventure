class Skill :
    def __init__(self, info_skill):
        self.detail = info_skill['Detail']
        self.name = info_skill['Name']
        self.image = info_skill['Image']
        self.value = info_skill['Effect']['Value']
        self.skill_type = info_skill['Effect']['Type']
        self.is_aoe = info_skill['Effect']['AoE']
        self.element = info_skill['Effect']['Element']

    def get_info(self) :
        return self.info

    def get_name(self):
        return self.name

    def get_detail(self):
        return self.detail

    def get_image(self):
        return self.image

    def get_value(self):
        return self.value

    def get_skill_type(self):
        return self.skill_type

    def get_is_aoe(self):
        return self.is_aoe

    def get_element(self):
        return self.element