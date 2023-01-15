from math import floor
import random
from Character import *
from Monster import *
from Inventory import *
from Item import *

class Fight:
	def __init__(self, c, m, i):
		self.list_chars = c
		self.list_mobs = m
		self.list_order_turn = self.set_turn()
		self.inventory = i
		self.nb_chars_dead = 0
		self.nb_mobs_dead = 0

		# compétence héros
		self.is_intimidation = False
		self.cpt_intimidation = 0

		# heros
		self.is_piercing_thrust = False # coup perçant
		
		# valentin
		self.is_parry = False # riposte
		
		# thari
		self.is_spear_thrower = False # lance-pique

	def get_inventory(self) :
		return self.inventory

	def get_size_list_mobs(self):
		return len(self.list_mobs)

	def get_size_list_chars(self):
		return len(self.list_chars)

	def presentation(self):
		print("[UN COMBAT EST LANCÉ]\n")
		for i in range(self.get_size_list_chars()) :
			if i == self.get_size_list_chars() - 1:
				print(self.list_chars[i].get_name(), end=" ")
			else :
				print(self.list_chars[i].get_name(), end=", ")

		# si le personnage est tout seul, phrase au singulier
		if self.get_size_list_chars() == 1 :
			print("rencontre un groupe de monstres !\n")
		# sinon au pluriel
		else :
			print("rencontrent un groupe de monstre !\n")

		print("Le groupe de monstres est composé de : ", end="")
		for i in range(self.get_size_list_mobs()) :
			if i == self.get_size_list_mobs() - 1:
				print(self.list_mobs[i].get_name(), end=".")
			else :
				print(self.list_mobs[i].get_name(), end=", ")
		print("\n")

	def choice_defend(self, c) :
		"""
		Personnage qui se défend
		Augmente la défense de 20% pendant le tour
		"""
		c.set_is_current_defense(True)
		c.set_current_defense(c.get_defense() * 1.2)

	def is_mob_loots(self, monster):
		n = random.random()
		if  n < monster.get_loot1().get_rate() :
			return True
		else :
			return False

	def get_loot(self, monster) :
		if self.is_mob_loots(monster) :
			print(f"{monster.get_name()} a fait tombé quelque chose lors de sa mort.")
			self.inventory.update_item(monster.get_loot1(), monster.get_loot1().get_quantity())
			print(f"Vous ramassez {monster.get_loot1().get_quantity()} x [{monster.get_loot1().get_name()}].\n")
		else :
			print(f"{monster.get_name()} n'a rien fait tombé lors de sa mort.")


	def quick_sort(self, L):
		"""
		Fonction qui permet de trier la liste selon la vitesse des joueurs / monstres
		:param l : une liste de monstres et joueurs
		:return la liste triée dans l'ordre décroissant
		"""
		if len(L) <= 1:
			return L

		pivot_value = L[-1]

		pivot = []
		G = []
		D = []
		
		# parmi les monstres et les personnages
		for i in L:
			if i.get_current_speed() < pivot_value.get_current_speed():
				D.append(i)
			elif i.get_current_speed() > pivot_value.get_current_speed():
				G.append(i)
			else:
				pivot.append(i)

		return self.quick_sort(G) + pivot + self.quick_sort(D)

	def set_turn(self) :
		list_all = []
		for i in self.list_mobs :
			list_all.append(i)
		for i in self.list_chars :
			list_all.append(i)

		return self.quick_sort(list_all)

	def sort_list(self, l) :
		return self.quick_sort(l)

	def is_all_chars_is_dead(self) : 
		self.nb_chars_dead = 0
		for i in self.list_chars :
			if i.is_dead() : 
				self.nb_chars_dead += 1
		if self.nb_chars_dead == self.get_size_list_chars() :
			return True
		else :
			return False

	def is_all_mobs_is_dead(self) :
		self.nb_mobs_dead = 0
		for i in self.list_mobs :
			if i.is_dead() : 
				self.nb_mobs_dead += 1
		if self.nb_mobs_dead == self.get_size_list_mobs() :
			return True
		else :
			return False

	def fight(self):
		turn = 0
		is_exit = False
		choice = 0
		self.presentation()
		# while not self.is_all_chars_is_dead() or not self.is_all_mobs_is_dead() or not is_exit:
		while not is_exit:
			turn += 1
			print(f"\t[TOUR N° {turn}]\n")
			self.list_order_turn = self.set_turn()
			for i in self.list_order_turn :

				if self.is_all_chars_is_dead() or self.is_all_mobs_is_dead() :
					break

				elif isinstance(i, Character) :
					print(f"\t[TOUR DE : {i.get_name().upper()}]\n")
					print(f"HP : {i.get_hp()}")
					print(f"MP : {i.get_mp()}")
					print(f"RP : {i.get_rp()}")
					print("")
					if i.is_dead() :
						print(f"{i.get_name()} est mort, son tour passe.\n")
						pass
					else :
						choice = self.action(i)
						# print("CHOIX", choice)
						if choice != None :
							# print("SORTIR")
							is_exit = True
							break

						print("")

				else :
					print(f"\t[TOUR DE : {i.get_name().upper()}]\n")
					if i.is_dead() :
						print(f"{i.get_name()} est mort, son tour passe.\n")
						pass
					else :
						self.monster_attack(i)
						print("")


			print(f"[FIN DU TOUR N°{turn}]\n")

			if self.is_all_chars_is_dead() :
				print("Tous les personnages de votre équipe sont morts.\n")
				break
			elif self.is_all_mobs_is_dead() :
				print("Tous les monstres sont morts.\n")
				break

			else :
				# on incremente les cd de chaque skill de chaque personnage
				for i in list_char :
					i.skill_1.set_current_cd(i.skill_1.get_current_cd() + 1)
					i.skill_2.set_current_cd(i.skill_2.get_current_cd() + 1)
					i.skill_3.set_current_cd(i.skill_3.get_current_cd() + 1)

					if i.get_is_current_defense() :
						i.set_is_current_defense(False)
						i.set_current_defense(i.get_defense())
						print(f"{i.get_name()} retrouve sa défense de base.")

					# on verifie si il ont des buff de potions
					if i.get_is_buff_str() :
						# si ca fait 3 tours
						if i.get_cpt_buff_str() > 2 :
							i.set_is_buff_str(False)
							i.set_cpt_buff_str(0)
							i.set_current_attack(i.get_attack())
							print(f"L'effet de [Potion de force] prend fin.\n{i.get_name()} retrouve son attaque de base.")
						else :
							print("nombre de tour", i.get_cpt_buff_str())
							print(f"L'effet [Potion de force] sur {i.get_name()} prendra fin dans {3 - i.get_cpt_buff_str()} tour.")
							i.set_cpt_buff_str(i.get_cpt_buff_str() + 1)
					if i.get_is_buff_res() :
						# si ca fait 3 tours
						if i.get_cpt_buff_res() > 2 :
							i.set_is_buff_res(False)
							i.set_cpt_buff_res(0)
							i.set_current_resistance(-5)
							print(f"L'effet de [Potion de résistance] prend fin.\n{i.get_name()} retrouve ses résistances de base.")
							i.print_current_resistance()
						else :
							print(f"L'effet [Potion de résistance] sur {i.get_name()} prendra fin dans {3 - i.get_cpt_buff_res()} tour.")
							i.set_cpt_buff_res(i.get_cpt_buff_res() + 1)

					if i.get_is_buff_spd() :
						self.list_order_turn = self.sort_list(self.list_order_turn)
						# si ca fait 3 tours
						if i.get_cpt_buff_spd() > 2 :
							i.set_is_buff_spd(False)
							i.set_cpt_buff_spd(0)
							i.set_current_speed(i.get_speed())
							# on remet la liste de tour dans l'ordre après le debuff de vitesse
							# self.list_order_turn = self.set_turn()
							self.list_order_turn = self.sort_list(self.list_order_turn)

							print(f"L'effet de [Potion de vitesse] prend fin.\n{i.get_name()} retrouve sa vitesse de base.")
						else :
							print(f"L'effet [Potion de vitesse] sur {i.get_name()} prendra fin dans {3 - i.get_cpt_buff_spd()} tour.")
							i.set_cpt_buff_spd(i.get_cpt_buff_spd() + 1)


				# verif si il y a des buff/debuff
				# retablir l'attaque des mobs
				if self.is_intimidation :
					self.cpt_intimidation += 1
					if self.cpt_intimidation == 2 :
						print("L'effet [Intimidation] prend fin.\nLes monstres retrouvent leur attaque de base.")
						for i in list_mobs :
							i.set_current_attack(i.get_attack())
						# réinitialisation des variables
						self.cpt_intimidation = 0
						self.is_intimidation = False

			# if turn >= 2 or is_exit:
			if is_exit:
				break
			print("")

		print("[FIN DU COMBAT]\n")
		if self.is_all_chars_is_dead() :
			print("Vous avez perdu le combat.")
		elif self.is_all_mobs_is_dead() :
			print("Félicitations ! Vous avez remporter le combat !\n")
			for i in self.list_mobs :
				self.get_loot(i)
		else :
			print("Vous vous êtes enfuis du combat.")

	def menu_action(self) :
		print("\t[ACTION]\n")
		print("[1] Attaquer\t\t[2] Défendre\n[3] Inventaire\t\t[4] Fuir")

	def action(self, c) :
		self.menu_action()
		print("")
		choice = int(input("Quelle action voulez-vous faire ? "))

		while choice != 1 and choice != 2 and choice != 3 and choice != 4 :
			print("Choisissez parmi les options suivantes : ")
			self.menu_action()
			print("")
			choice = int(input("Quelle action voulez-vous faire ? "))

		print("")
		if choice == 1 :
			print("Vous avez choisi 'Attaquer'.")
			self.choose_skill(c)
		elif choice == 2 :
			print("Vous avez choisi 'Défendre'.")
			self.choose_defend(c)
		elif choice == 3 :
			print("Vous avez choisi 'Inventaire'.")
			print("")
			self.choice_inventory(c)
		elif choice == 4 :
			print("Vous avez choisi 'Fuir'.")
			print("")
			return -1
			# exit1

	def menu_inventory(self, c):
		self.inventory.print_inventory()
		print("")

	def menu_detail_inventory(self, choice) :
		self.inventory.menu_detail_inventory(choice)
		print("")

	def choice_item(self, c, choice) :
		self.menu_detail_inventory(choice)
		
		choice_menu_item = int(input("Que souhaitez-vous faire ? "))

		while choice_menu_item != 1 and choice_menu_item != 2 and choice_menu_item != 3 :
			print("")
			print("Choissisez une valeur parmi celle proposée !\n")
			self.menu_detail_inventory(choice)
			choice_menu_item = int(input("Que souhaitez-vous faire ? "))
			print("")
		
		self.choosen_item(c, choice, choice_menu_item)

	def choosen_item(self, c, choice, choice_menu_item) :
		if choice_menu_item == 1 :
			for index, (key, value) in enumerate(self.inventory.get_inventory().items()):
				if choice == index :
					# si la quantité de potion > 0
					if key.is_potion() :
						print("")
						# choisir quelle personnage utiliser la potion
						char_to_use_potion = self.choice_char()
						# si il fait retour
						if char_to_use_potion == self.get_size_list_chars() :
							self.choice_item(c, choice)
						else :
							for index, i in enumerate(self.list_chars) :
								if index == char_to_use_potion :
									if isinstance(key, Potion_de_buff) :
										if key.use_potion(i) :
											self.inventory.update_item(key, -1)
											if key.get_type_buff() == 'str' :
												i.set_is_buff_str(True)
											if key.get_type_buff() == 'resistance' :
												i.set_is_buff_res(True)
											if key.get_type_buff() == 'spd' :
												i.set_is_buff_spd(True)
										else :
											self.choosen_item(c, choice, choice_menu_item)

									elif isinstance(key, Potion) :
										if key.use_potion(i) :
											self.inventory.update_item(key, -1)
					# si la quantité de potion = 0
					else :
						print("")
						print(f"Vous n'avez pas de [{key.get_name()}] disponible.")
						self.choice_item(c, choice)
		elif choice_menu_item == 2 :
			self.inventory.get_description(choice)
			self.choice_item(c, choice)
		elif choice_menu_item == 3 :
			print("")
			self.choice_inventory(c)

	def choice_inventory(self, c) :
		self.menu_inventory(c)

		choice = int(input("Quel objet souhaitez-vous utiliser ? "))

		while choice < 0 or choice > self.inventory.get_len_inventory() :
			print("")
			print("Choissisez une valeur parmi celle proposée !\n")
			self.menu_inventory(c)
			choice = int(input("Quel objet souhaitez-vous utiliser ? "))
			print("")

		if choice == 0 :
			self.choice_item(c, choice)
		if choice == 1 :
			self.choice_item(c, choice)
		elif choice == 2 :
			self.choice_item(c, choice)
		elif choice == 3 :
			self.choice_item(c, choice)
		elif choice == 4 :
			self.choice_item(c, choice)
		elif choice == 5 :
			self.choice_item(c, choice)
		elif choice == 6 :
			print("")
			self.action(c)

	def choice_mobs(self):
		print("\t[Liste des monstres]\n")
		for index, i in enumerate(self.list_mobs) :
			print(f"[{index}] {i.get_name()}")
		print(f"[{self.get_size_list_mobs()}] Retour")
		print("")
		choice = int(input("Quel mob voulez vous attaquer ? "))

		while choice < 0 or choice > self.get_size_list_mobs() :
			print("Choissisez une valeur parmi celle proposée !\n")
			print("\t[Liste des monstres]\n")

			for index, i in enumerate(self.list_mobs) :
				print(f"[{index}] {i.get_name()}")
			print(f"[{self.get_size_list_mobs()}] Retour")
			print("")
			choice = int(input("Quel mob voulez vous attaquer ? "))

		return choice

	def choice_char(self):
		print("\t[LISTE DES PERSONNAGES]\n")
		for index, i in enumerate(self.list_chars) :
			print(f"[{index}] {i.get_name()}")
		print(f"[{self.get_size_list_chars()}] Retour")
		print("")
		choice = int(input("Sur quel personnage ? "))

		while choice < 0 or choice > self.get_size_list_chars() :
			print("Choissisez une valeur parmi celle proposée !\n")
			print("\t[LISTE DES PERSONNAGES]\n")

			for index, i in enumerate(self.list_chars) :
				print(f"[{index}] {i.get_name()}")
			print(f"[{self.get_size_list_chars()}] Retour")
			print("")
			choice = int(input("Sur quel personnage ? "))

		return choice

	def monster_attack(self, m):
		mob_target = random.choice(self.list_chars)

		# tant que la cible du mob est un personnage mort
		# il choisit jusqu'a avoir un personne en vie
		while mob_target.is_dead() :
			mob_target = random.choice(self.list_chars)

		list_mob_attacks = [m.get_current_attack(), m.skill_1]
		mob_attack = random.choice(list_mob_attacks)

		# si le mob utilise l'attaque de base
		if mob_attack == m.get_current_attack() :			
			damage = m.get_current_attack() - mob_target.get_current_defense()
			mob_attack_name = 'Attaque de base'
		# si le mob utilise sa compétence
		else :
			damage = m.get_current_attack() * m.skill_1.get_value() - mob_target.get_current_defense()
			mob_attack_name = mob_attack.get_name()

			for k, v in mob_target.get_resistance_fr().items() :
				if m.skill_1.get_element() == k :
					dmg_res = damage * v/100
					damage =  damage - dmg_res
		
		damage = round(damage)

		if damage < 1 :
			damage = 1

		if self.is_parry :
			for i in self.list_chars :
				if i.get_name() == "Valentin" :
					print(f"{m.get_name()} attaque {mob_target.get_name()} avec '{mob_attack_name}'.")
					print(f"{i.get_name()} a 'Rispote' d'actif. Il absorbe l'attaque !")
					m.set_hp(m.get_hp() - damage)
					print(f"{m.get_name()} subit {damage} dégats.")
					if m.is_dead() :
						print(f"\n{m.get_name()} est mort !")
			self.is_parry = False

		else :
			mob_target.set_hp(mob_target.get_hp() - damage)
			print(f"{m.get_name()} attaque {mob_target.get_name()} avec [{mob_attack_name}].\n")
			print(f"{mob_target.get_name()} subit {damage} dégats.\n{mob_target.get_name()} a {mob_target.get_hp()} HP restant.")
			if mob_target.is_dead() :
				print("")
				print(f"\n{mob_target.get_name()} est mort !")

	def attack_basic(self, c, skill) :
		"""
		Attaque de base du personnage
		"""
		print("")
		choice = self.choice_mobs()

		if choice == self.get_size_list_mobs() :
			print("Vous avez choisi 'Retour'.")
			print("")
			self.check_skill(c, skill)
		else : 
			for index, i in enumerate(self.list_mobs) :
				if choice == index :
					damage = c.attack - i.get_defense()

					if "Physique" in i.get_resistance():
						damage *= 0.9
						damage = round(damage)
					elif "Physique" in i.get_weakness():
						damage *= 1.1
						damage = round(damage)
					if damage < 1 :
						damage = 1
					i.set_hp(i.get_hp() - damage)

					print("")
					print(f"{c.get_name()} attaque {i.get_name()} avec [Attaque de base].")
					print("")
					print(f"{i.get_name()} subit {damage} dégats.")
					if i.is_dead() :
						print("")
						print(f"{i.get_name()} est mort !")

	def menu_skills(self, c) :
		print("\t[COMPÉTENCE]\n")
		print(f"[1] Attaque de base\n[2] {c.skill_1.get_name()}\n"
		f"[3] {c.skill_2.get_name()}\n[4] {c.skill_3.get_name()}\n"
		f"[5] {c.ultimate.get_name()}\n[6] Retour\n")

	def choose_skill(self, c) :
		print("")
		self.menu_skills(c)
		choice = int(input("Quel choix voulez-vous faire ? "))
		while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 :
			print("Choisissez parmi les compétences suivantes :")
			self.menu_skills(c)
			choice = int(input("Quel choix voulez-vous faire ? "))

		print("")
		if choice == 1 :
			print("Vous avez choisi [Attaque de base].")
			print("")
			self.check_skill(c, c.get_current_attack())
		elif choice == 2 :
			self.check_skill(c, c.skill_1)
		elif choice == 3 :
			self.check_skill(c, c.skill_2)
		elif choice == 4 :
			self.check_skill(c, c.skill_3)
		elif choice == 5 :
			self.check_skill(c, c.ultimate)
		elif choice == 6 :
			print("Vous avez choisi [Retour].")
			print("")
			return self.action(c)

	def menu_check_skill(self) :
		print("\t[SOUS-MENU COMPÉTENCE]\n")
		print("[1] Valider\n[2] Description de la compétence\n[3] Retour")


	def choose_defend(self, c) :
		print("")
		choice = self.choose_check_skill()

		if choice == 1 :
			self.choice_defend(c)
		elif choice == 2 :
			print("\n\t[Défense]\n")
			print("Permet au personnage d'augmenter sa défense de 20% pendant le tour en cours.")
			self.choose_defend(c)
		elif choice == 3 :
			print("")
			print("Vous avez choisi 'Retour'.")
			print("")
			self.action(c)

	def choose_check_skill(self) :
		self.menu_check_skill()
		print("")
		choice = int(input("Quel choix voulez-vous faire ? "))

		while choice != 1 and choice != 2 and choice != 3 :
			print("Choisissez parmi les options suivantes : ")
			print("")
			self.menu_check_skill()
			choice = int(input("Quel choix voulez-vous faire ? "))
		
		return choice

	def check_skill(self, c, skill):

		choice = self.choose_check_skill()

		if choice == 1 :
			if isinstance(skill, Skill_mp) or isinstance(skill, Skill_ulti):
				print("")
				self.use_skill(c, skill)
			else :
				self.attack_basic(c, skill)	
		elif choice == 2 :
			print("")
			print("Vous avez choisi 'Description de la compétence'.\n")
			self.description_skill(c, skill)
		elif choice == 3 :
			print("Vous avez choisi 'Retour'.")
			self.choose_skill(c)

	def description_skill(self, c, skill) :
		if isinstance(skill, Skill_mp) or isinstance(skill, Skill_ulti):
			if isinstance(skill, Skill_mp) :
				print(f"\t[{skill.get_name()}]\n\nDescription : {skill.get_detail()}\nMP : {skill.get_mp()}\nCD : {skill.get_cd()}")
			elif isinstance(skill, Skill_ulti) :
				print(f"\t[{skill.get_name()}]\n\nDescription : {skill.get_detail()}\nRP : {skill.get_rp()}")
		else :
			print(f"\t[Attaque de base]\n\nAttaque : {c.get_current_attack()}\nMP : 0\nCD : 0\n")
		print("")
		self.check_skill(c, skill)


	def use_skill(self, c , skill) :
		"""
		Utilisation de la compétance
		:param skill : compétance choisi par le joueur
		:param mob : liste de monstres
		"""
		if isinstance(skill, Skill_mp) :
			if (c.get_mp() >= skill.get_mp()) and (skill.get_cd() == skill.get_current_cd()) :
				c.set_mp(c.get_mp() - skill.get_mp())
				
				if skill.get_skill_type() == "Attaque" :
					if	skill.get_is_aoe() :
						print(f"{c.get_name()} utilise la compétence AoE [{skill.get_name()}].\n")
						for i in self.list_mobs :
							damage = c.get_current_attack() * skill.get_value() - i.get_defense()
							if skill.get_element() in i.get_resistance():
								damage *= 0.9
								damage = round(damage)
							elif skill.get_element() in i.get_weakness():
								damage *= 1.1
								damage = round(damage)
							if damage < 1 :
								damage = 1
							i.set_hp(i.get_hp() - damage)
							print(f"{c.get_name()} attaque {i.get_name()}.")
							print(f"{i.get_name()} subit {damage} dégats.")
							if i.is_dead() :
								print(f"\n{i.get_name()} est mort !")
							print("")
						
					else :
						choice = self.choice_mobs()
						print("")
						print(f"{c.get_name()} utilise la compétence [{skill.get_name()}].")
						for index, i in enumerate(self.list_mobs) :
							if choice == index :
								if skill.get_is_debuff() :
									if skill.get_name() == "Coup perçant" :
										self.is_piercing_thrust = True
										def_decrease = 0
										damage = 0
										if i.get_is_boss() :
											# ignore 5% de la défense du boss
											def_decrease = i.get_defense() * 0.95
											def_decrease = round(def_decrease)
											damage = c.get_current_attack() * skill.get_value_boss() - def_decrease
											if skill.get_element() in i.get_resistance():
												damage *= 0.9
												print(f"{i.get_name()} a une résistance [{skill.get_element()}] !!")

											elif skill.get_element() in i.get_weakness():
												damage *= 1.1
												print(f"{i.get_name()} a une faiblesse [{skill.get_element()}] !!")

										else :
											# ignore 20% de la défense du mob
											def_decrease = i.get_defense() * 0.80
											def_decrease = round(def_decrease)
											damage = c.get_current_attack() * skill.get_value() - def_decrease
											if skill.get_element() in i.get_resistance():
												damage *= 0.9
												print(f"{i.get_name()} a une résistance [{skill.get_element()}] !!")
											elif skill.get_element() in i.get_weakness():
												damage *= 1.1
												print(f"{i.get_name()} a une faiblesse [{skill.get_element()}] !!")

										damage = round(damage)
										
										print(f"{c.get_name()} perce la défense de {i.get_name()}.\n{i.get_name()} perd {def_decrease} DEF !!")
										i.set_hp(i.get_hp() - damage)
										print(f"{i.get_name()} perd {damage} HP lors de cette attaque.")
										
										
										self.is_piercing_thrust = False
										print("")
								else :
									print("")
									if skill.get_name() == "Lance-pique" :
										self.is_piercing_thrust = True

									# attaque normal
									damage = c.get_current_attack() * skill.get_value() - i.get_defense()

									if skill.get_element() in i.get_resistance():
										damage *= 0.9
										damage = round(damage)
									elif skill.get_element() in i.get_weakness():
										damage *= 1.1
										damage = round(damage)
									if damage < 1 :
										damage = 1

									if self.is_piercing_thrust :
										nb_attack = random.randint(1, 4)
										
										print(f"{c.get_name()} attaque {i.get_name()} {nb_attack} fois.")
										for j in range(nb_attack) :
											i.set_hp(i.get_hp() - damage)
											print(f"{i.get_name()} subit {damage} dégats.")
										self.is_piercing_thrust = False
									else :
										i.set_hp(i.get_hp() - damage)
										print(f"{c.get_name()} attaque {i.get_name()}.")
										print(f"{i.get_name()} subit {damage} dégats.")
									
									if i.is_dead() :
											print(f"\n{i.get_name()} est mort !")

				elif skill.get_skill_type() == "Soin" :
					c.set_mp(c.get_mp() - skill.get_mp())
					print(f"{c.get_name()} utilise la compétence [{skill.get_name()}].\n")
					
					if skill.get_is_aoe() :
						pass
					else :
						char_to_heal = self.choice_char()

						for index, i in enumerate(self.list_chars) :
							if char_to_heal == index :
								heal = i.get_hp_max() * skill.get_value()
								heal = floor(heal)
								
								if (i.get_hp() + heal > i.get_hp_max()) :
									i.set_hp(i.get_hp_max())
								else :
									i.set_hp(i.get_hp() + heal)
								print(f"{c.get_name()} soigne {i.get_name()} de {heal} HP.\n{i.get_name()} a {i.get_hp()} HP.")


				elif skill.get_skill_type() == "Offensif" :
					print(f"{c.get_name()} utilise la compétence [{skill.get_name()}].\n")
					if	skill.get_is_aoe() :
						if skill.get_is_debuff() :
							if skill.get_name() == "Intimidation" :
								self.is_intimidation = True
								for i in self.list_mobs :
									if i.get_is_boss() :
										new_attack = i.get_current_attack() * skill.get_value_boss()
									else :
										new_attack = i.get_current_attack() * skill.get_value()
									new_attack = round(new_attack)
									print(f"{i.get_name()} perd {i.get_current_attack() - new_attack} ATK.")
									i.set_current_attack(new_attack)
									print(f"{i.get_name()} a désormais {i.get_current_attack()} ATK.")
									print("")

					else :
						pass
					
				elif skill.get_skill_type() == "Défensif" :
					print(f"{c.get_name()} utilise la compétence [{skill.get_name()}].\n")
					if	skill.get_is_aoe() :
						pass
					else :
						if skill.get_name() == "Riposte" :
							self.is_parry = True
							print(f"{c.get_name()} a la compétence 'Rispote' d'actif." )

				# fin du tour, on ajoute des RP
				random_rp = random.randint(5, 15)
				# random_rp = random.randint(100, 100)
				c.set_rp(c.get_rp() + random_rp)
				skill.set_current_cd(-1)

			# cas si pas assez de MP
			elif skill.get_mp() >= c.get_mp():
				print(f"Votre compétence coûte {skill.get_mp()} MP.\nVous avez actuellement {c.get_mp()} MP.\nVous n'avez pas les MP nécessaires.")
				self.choose_skill(c)

			# cas si le CD actuel du skill n'est égale au CD du skill
			elif skill.get_cd() != skill.get_current_cd() :
				print(f"Le CD n'est pas terminé\n {skill.get_current_cd()} / {skill.get_cd()}")
				self.choose_skill(c)

		# si c'est l'ulti
		else :
			if (c.get_rp() >= skill.get_rp()):
				c.set_rp(c.get_rp() - skill.get_rp())
				if skill.get_skill_type() == "Attaque" :
					if skill.get_is_aoe() :
						pass
					else :
						choice = self.choice_mobs()
						print("")
						for index, i in enumerate(self.list_mobs) :
							if choice == index :
								damage = c.attack * skill.get_value() - i.get_defense()

								if skill.get_element() in i.get_resistance():
									damage *= 0.9
								elif skill.get_element() in i.get_weakness():
									damage *= 1.1
								if damage < 1 :
									damage = 1
								damage = round(damage)
								i.set_hp(i.get_hp() - damage)

								print(f"{c.get_name()} attaque {i.get_name()} avec [{skill.get_name()}].")
								print(f"{i.get_name()} subit {damage} dégats.")
								if i.is_dead() :
									print(f"\n{i.get_name()} est mort !")


			else :
				print(f"Votre compétence coûte {skill.get_rp()} RP.\nVous avez actuellement {c.get_rp()} RP.\nVous n'avez pas les RP nécessaires.")
				self.choose_skill(c)


# test
h = Character(json_class('heros'))
v = Character(json_class('lancer'))
t = Character(json_class('warrior'))
slime_v = Monster(json_monster('1'))
slime_r = Monster(json_monster('2'))

i = Inventory()
i.init_inventory()

list_char = []
list_mobs = []

list_mobs.append(slime_v)
list_mobs.append(slime_r)
list_char.append(t)
# list_char.append(h)
# list_char.append(v)

f = Fight(list_char, list_mobs, i)
f.fight()

# pour mettre a jour l'inventaire après le combat
i = f.get_inventory()