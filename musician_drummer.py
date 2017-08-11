import random

class Musician(object):
	"""docstring sounds Musician"""
	def __init__(self, sounds):
		self.sounds = sounds


	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=" ")
		print()


class Bassist(Musician): # The Musician class is the parent of the Bassist
	def __init__(self):
		# call the __init__ method of the parent class
		super().__init__(["Twang", "Thrum", "Bling"])


class Guitarist(Musician):
	def __init__(self):
		# call the __init__ method of the parent class
		super().__init__(["Bonk", "Bow", "Boom"])


	def tune(self):
		print("Be with you in a moment")
		print("Twoning, sproing, splang")


class Drummer(Musician):
	def __init__(self):
		# call the __init__ method of the parent
		super().__init__(["Boom", "Baac", "Bang"])

	def Counttofour(self):
		for i in range(1, 5):
			print(i, end=" ")
		print()

	def Combust(self):
		print(random.choice(self.sounds)*3)


nigel = Drummer()
nigel.solo(9)
print(nigel.sounds)
print(nigel.Counttofour())
print(nigel.Combust())