from Skill_MP import Skill_mp
from Skill_Ulti import Skill_ulti
import json
from math import floor

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
		self.hp_max = info_perso['hp']
		self.mp_max = info_perso['mp']
		self.rp_max = info_perso['rp_max']
		self.hp = info_perso['hp']
		self.mp = info_perso['mp']	
		self.rp = info_perso['rp']
		self.accuracy = info_perso['accuracy']
		self.exp = info_perso['exp']
		self.sprite = info_perso['sprite']

		# stats de base du perso
		self.attack = info_perso['attack']
		self.defense = info_perso['defense']
		self.speed = info_perso['spd']
		self.resistance_fire = info_perso['resistance']['fire']
		self.resistance_water = info_perso['resistance']['water']
		self.resistance_thunder = info_perso['resistance']['thunder']
		self.resistance_earth = info_perso['resistance']['earth']
		self.resistance_wind = info_perso['resistance']['wind']
		self.resistance_light = info_perso['resistance']['light']
		self.resistance_dark = info_perso['resistance']['dark']

		# stat du perso modiafle apres buff / debuff
		self.current_defense = info_perso['defense']
		self.is_current_defense = False
		self.current_attack = info_perso['attack']
		self.current_speed = info_perso['spd']
		self.current_resistance_fire = info_perso['resistance']['fire']
		self.current_resistance_water = info_perso['resistance']['water']
		self.current_resistance_thunder = info_perso['resistance']['thunder']
		self.current_resistance_earth = info_perso['resistance']['earth']
		self.current_resistance_wind = info_perso['resistance']['wind']
		self.current_resistance_light = info_perso['resistance']['light']
		self.current_resistance_dark = info_perso['resistance']['dark']

		self.skill_1 = Skill_mp(info_perso['skills']['skill_1'])
		self.skill_2 = Skill_mp(info_perso['skills']['skill_2'])
		self.skill_3 = Skill_mp(info_perso['skills']['skill_3'])
		self.ultimate = Skill_ulti(info_perso['skills']['ultimate'])

		self.resistance = info_perso['resistance']
		self.resistance_fr = self.init_resistance_fr()

		self.is_buff_str = False
		self.is_buff_res = False
		self.is_buff_spd = False

		self.cpt_buff_str = 0
		self.cpt_buff_res = 0
		self.cpt_buff_spd = 0

	def get_is_current_defense(self) :
		return self.is_current_defense

	def set_is_current_defense(self, is_current_defense) :
		self.is_current_defense = is_current_defense

	def get_cpt_buff_str(self) :
		return self.cpt_buff_str
	def get_cpt_buff_res(self) :
		return self.cpt_buff_res
	def get_cpt_buff_spd(self) :
		return self.cpt_buff_spd

	def set_cpt_buff_str(self, cpt_buff_str) :
		self.cpt_buff_str = cpt_buff_str
	def set_cpt_buff_res(self, cpt_buff_res) :
		self.cpt_buff_res = cpt_buff_res
	def set_cpt_buff_spd(self, cpt_buff_spd) :
		self.cpt_buff_spd = cpt_buff_spd

	def get_is_buff_str(self) :
		return self.is_buff_str
	def get_is_buff_res(self) :
		return self.is_buff_res
	def get_is_buff_spd(self) :
		return self.is_buff_spd

	def set_is_buff_str(self, is_buff_str) :
		self.is_buff_str = is_buff_str
	def set_is_buff_res(self, is_buff_res) :
		self.is_buff_res = is_buff_res
	def set_is_buff_spd(self, is_buff_spd) :
		self.is_buff_spd = is_buff_spd

	def set_name(self, name):
		self.name = name

	def get_rp_max(self):
		return self.rp_max

	def get_rp(self):
		return self.rp

	def set_rp(self, rp):
		if rp >= 100 :
			self.rp = 100
		else :
			self.rp = rp

	def equals_rp(self) :
		if self.rp == self.ultimate.get_rp() :
			# on peut utiliser l'ultime
			return True
		else :
			return False

	def init_resistance_fr(self):
		res_fr = {}
		for k, v in self.resistance.items() :
			if k == "fire" :
				key = "Feu"
			if k == "water" :
				key = "Eau"
			if k == "thunder" :
				key = "Foudre"
			if k == "earth" :
				key = "Terre"
			if k == "wind" :
				key = "Vent"
			if k == "light" :
				key = "Lumière"
			if k == "dark" :
				key = "Ténèbre"
			res_fr.update({key: v})
		
		return res_fr

	def get_resistance_fr(self):
		return self.resistance_fr

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
	
	def get_hp_max(self) :
		return self.hp_max
	
	def get_mp_max(self) :
		return self.mp_max

	def get_attack(self) :
		return self.attack
	
	def get_defense(self) :
		return self.defense
	
	def get_accuracy(self) :
		return self.accuracy
	
	def get_speed(self) :
		return self.speed

	def get_current_attack(self) :
		return self.current_attack

	def get_current_defense(self) :
		return self.current_defense

	def get_current_speed(self) :
		return self.current_speed

	def set_current_attack(self, attack) :
		self.current_attack = attack

	def set_current_defense(self, defense) :
		self.current_defense = defense

	def set_current_speed(self, speed) :
		self.current_speed = speed
	
	def get_exp(self) :
		return self.exp
	
	def get_sprite(self) :
		return self.sprite
	
	def get_resistance_fire(self) :
		return self.resistance_fire
	
	def get_resistance_water(self) :
		return self.resistance_water
	
	def get_resistance_thunder(self) :
		return self.resistance_thunder
	
	def get_resistance_earth(self) :
		return self.resistance_earth
	
	def get_resistance_wind(self) :
		return self.resistance_wind
	
	def get_resistance_light(self) :
		return self.resistance_light
	
	def get_resistance_dark(self) :
		return self.resistance_dark

	def get_current_resistance_fire(self) :
		return self.current_resistance_fire
	
	def get_current_resistance_water(self) :
		return self.current_resistance_water
	
	def get_current_resistance_thunder(self) :
		return self.current_resistance_thunder
	
	def get_current_resistance_earth(self) :
		return self.current_resistance_earth
	
	def get_current_resistance_wind(self) :
		return self.current_resistance_wind
	
	def get_current_resistance_light(self) :
		return self.current_resistance_light
	
	def get_current_resistance_dark(self) :
		return self.current_resistance_dark

	def print_current_resistance(self) :
		print("")
		print(f"Feu : {self.get_current_resistance_fire()}\nEau : {self.get_current_resistance_water()}\nFoudre : {self.get_current_resistance_thunder()}\nTerre : {self.get_current_resistance_earth()}\nVent : {self.get_current_resistance_wind()}\nLumière : {self.get_current_resistance_light()}\nTénèbre : {self.get_current_resistance_dark()}")

	def get_skill_1(self) :
		return self.skill_1
	
	def get_skill_2(self) :
		return self.skill_2
	
	def get_skill_3(self) :
		return self.skill_3
	
	def get_ultimate(self) :
		return self.ultimate

	def set_hp(self, hp) :
		self.hp = hp
		if self.is_dead() :
			self.hp = 0
	
	def set_mp(self, mp) :
		self.mp = mp

	def set_current_resistance(self, resistance) :
		self.current_resistance_fire += resistance
		self.current_resistance_water += resistance
		self.current_resistance_thunder += resistance
		self.current_resistance_earth += resistance
		self.current_resistance_wind += resistance
		self.current_resistance_light += resistance
		self.current_resistance_dark += resistance

	def is_dead(self) :
		if self.hp <= 0 :
			return True
		else :
			return False

p = Character(json_class("heros"))
v = Character(json_class("lancer"))
t = Character(json_class("warrior"))
k = Character(json_class("priest"))
