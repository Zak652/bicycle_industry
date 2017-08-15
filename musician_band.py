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


class Band(object):
	"""docstring for Band"""
	band_members = []

	def hire(self, member):

		self.band_members.append(member)
		print([_member.name for _member in self.band_members])

	def fire(self, member):
		
		self.band_members.remove(member)
		print('{} has been fired from the {}'.format(member, self))
		print([_member.name for _member in self.band_members])

	def bandmusic(self):
		
		print (Drummer.counttofour(self))

		for member in self.band_members:
			member.solo(5)


zak = Guitarist('Zak40')
moses = Bassist('Moses')
nigel = Drummer('Nigel')
nigel.solo(9)
print(nigel.counttofour())
print(nigel.combust())
coldplay = Band()
coldplay.hire(nigel)
coldplay.hire(zak)
coldplay.hire(moses)
# coldplay.fire(nigel)
coldplay.bandmusic()import random

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


class Band(object):
	"""docstring for Band"""
	band_members = []

	def hire(self, member):

		self.band_members.append(member)
		print([_member.name for _member in self.band_members])

	def fire(self, member):
		
		self.band_members.remove(member)
		print('{} has been fired from the {}'.format(member, self))
		print([_member.name for _member in self.band_members])

	def bandmusic(self):
		
		print (Drummer.counttofour(self))

		for member in self.band_members:
			member.solo(5)


zak = Guitarist('Zak40')
moses = Bassist('Moses')
nigel = Drummer('Nigel')
nigel.solo(9)
print(nigel.counttofour())
print(nigel.combust())
coldplay = Band()
coldplay.hire(nigel)
coldplay.hire(zak)
coldplay.hire(moses)
# coldplay.fire(nigel)
coldplay.bandmusic()