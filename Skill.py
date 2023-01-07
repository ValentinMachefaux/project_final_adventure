class Skill :
    def __init__(self, info_skill):
        self.detail = info_skill['detail']
        self.name = info_skill['name']
        self.image = info_skill['image']
        self.value = info_skill['effect']['value']
        self.skill_type = info_skill['effect']['type']
        self.is_aoe = info_skill['effect']['aoe']
        self.element = info_skill['effect']['element']

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