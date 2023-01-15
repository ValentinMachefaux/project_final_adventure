class Skill :
    def __init__(self, info_skill):
        self.detail = info_skill['detail']
        self.name = info_skill['name']
        self.image = info_skill['image']
        self.value = info_skill['effect']['value']
        self.skill_type = info_skill['effect']['type']
        self.is_aoe = info_skill['effect']['aoe']
        self.element = info_skill['effect']['element']
        self.is_buff = info_skill['effect']['is_buff']
        self.is_debuff = info_skill['effect']['is_debuff']
        if 'value_boss' in info_skill['effect'] :
            self.skill_value_boss = info_skill['effect']['value_boss']

    def get_name(self):
        return self.name

    def get_detail(self):
        return self.detail

    def get_image(self):
        return self.image

    def get_value(self):
        return self.value

    def get_value_boss(self):
        return self.value_boss

    def get_skill_type(self):
        return self.skill_type

    def get_is_aoe(self):
        return self.is_aoe

    def get_element(self):
        return self.element

    def get_is_buff(self) :
        return self.is_buff

    def get_is_debuff(self) :
        return self.is_debuff
        
    def get_sound_effect(self) :
        return self.sound_effect