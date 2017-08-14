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

	def counttofour(self):
		for i in range(1, 5):
			print(i, end=" ")
		print()

	def combust(self):
		print(random.choice(self.sounds)*3)


class Band(object):
	"""docstring for Band"""
	band_members = []

	def __init__(self):
		# self.name = name
		# call the __init__ method of the parent
		Drummer()

	def hire(self):
		member = Drummer

		Band.band_members.append(member)
		print(self.band_members)


	# def fire(self):
	# 	Band.band_members.pop(Musician)
	# 	print(Band.band_members)
		


	# def bandplay(self):
	# 	Drummer.counttofour()
	# 	Drummer.solo()
	# 	Bassist.solo()
	# 	Guitarist.solo()



# type(Band.hire)
# print(Band.hire)
zak = Drummer()
nigel = Drummer()
nigel.solo(9)
print(nigel.counttofour())
print(nigel.combust())
Coldplay = Band()
print(Band())
# nigel = Coldplay.hire()
# zak = Coldplay.hire()