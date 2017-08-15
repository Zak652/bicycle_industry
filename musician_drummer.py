import random

class Musician(object):
	"""docstring sounds Musician"""
	def __init__(self, sounds, name):
		self.sounds = sounds
		self.name = name


	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=" ")
		print()


class Bassist(Musician): # The Musician class is the parent of the Bassist
	def __init__(self, name):
		self.name = name
		# call the __init__ method of the parent class
		super().__init__(["Twang", "Thrum", "Bling"], self.name)


class Guitarist(Musician):
	def __init__(self, name):
		self.name = name
		# call the __init__ method of the parent class
		super().__init__(["Bonk", "Bow", "Boom"], self.name)


	def tune(self):
		print("Be with you in a moment")
		print("Twoning, sproing, splang")


class Drummer(Musician):
	def __init__(self, name):
		self.name = name
		# call the __init__ method of the parent
		super().__init__(["Boom", "Baac", "Bang"], self.name)

	def counttofour(self):
		for i in range(1, 5):
			print(i, end=" ")
		print()

	def combust(self):
		print(random.choice(self.sounds)*3)



zak = Guitarist('Zak40')
moses = Bassist('Moses')
nigel = Drummer('Nigel')
nigel.solo(9)
print(nigel.counttofour())
print(nigel.combust())