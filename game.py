"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@classmethod
	def make_unarmed(cls, unarmed):
		unarmed.nom = "Unarmed"
		unarmed.power = 20
		unarmed.min_level = 1

		UNARMED_POWER = 20 #??

	@property
	def name(self):
		return self.__name

class Character(Weapon):
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, power, name, max_hp, attack, defense, level, weapon, hp):
		super().__init__(power)
		super().__init__(weapon)
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp = hp

	def compute_damage(self, other_self):
		dmg = ((((2 * self.level / 5 + 2) * self.power * (self.attack / other_self.defense)) / 50) + 2) * ( * random.uniform(0.85, 1.00))
		crit =
		return dmg


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts

	damage = f"{attacker.name} used {attacker.weapon}\n\t{defender.name} took {Character.compute_damage(attacker, defender)} dmg"
	print(damage)
	return damage

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass
