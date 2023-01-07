from Skill_MP import Skill_mp
from Skill_Ulti import Skill_ulti


import json

def json_class(class_name):
	with open('resources\\json_datas\\characters.json', "r", encoding='utf-8') as f:
		data = json.load(f)
	get_character = data['characters']
	get_hero = get_character[0]
	return get_hero[class_name]

class Character():

	def __init__(self, info_perso):
		self.name = info_perso['name']
		self.classe = info_perso['class']
		self.level = info_perso['level']
		self.hp = info_perso['hp']
		self.mp = info_perso['mp']
		self.attack = info_perso['atk']
		self.defense = info_perso['def']
		self.accuracy = info_perso['accuracy']
		self.speed = info_perso['spd']
		self.exp = info_perso['exp']
		self.sprite = info_perso['sprite']
		self.resitance_fire = info_perso['resistance']['fire']
		self.resitance_water = info_perso['resistance']['water']
		self.resitance_thunder = info_perso['resistance']['thunder']
		self.resitance_earth = info_perso['resistance']['earth']
		self.resitance_wind = info_perso['resistance']['wind']
		self.resitance_light = info_perso['resistance']['light']
		self.resitance_dark = info_perso['resistance']['dark']
		self.skill_1 = Skill_mp(info_perso['skills']['skill_1'])
		self.skill_2 = Skill_mp(info_perso['skills']['skill_2'])
		self.skill_3 = Skill_mp(info_perso['skills']['skill_3'])
		self.ultimate = Skill_ulti(info_perso['skills']['ultimate'])

	def get_name(self) :
		return self.name
	
	def get_classe(self) :
		return self.classe
	
	def get_level(self) :
		return self.level
	
	def get_hp(self) :
		return self.hp
	
	def get_mp(self) :
		return self.mp
	
	def get_attack(self) :
		return self.attack
	
	def get_defense(self) :
		return self.defense
	
	def get_accuracy(self) :
		return self.accuracy
	
	def get_speed(self) :
		return self.speed
	
	def get_exp(self) :
		return self.exp
	
	def get_sprite(self) :
		return self.sprite
	
	def get_resitance_fire(self) :
		return self.resitance_fire
	
	def get_resitance_water(self) :
		return self.resitance_water
	
	def get_resitance_thunder(self) :
		return self.resitance_thunder
	
	def get_resitance_earth(self) :
		return self.resitance_earth
	
	def get_resitance_wind(self) :
		return self.resitance_wind
	
	def get_resitance_light(self) :
		return self.resitance_light
	
	def get_resitance_dark(self) :
		return self.resitance_dark
	
	def get_skill_1(self) :
		return self.skill_1
	
	def get_skill_2(self) :
		return self.skill_2
	
	def get_skill_3(self) :
		return self.skill_3
	
	def get_ultimate(self) :
		return self.ultimate