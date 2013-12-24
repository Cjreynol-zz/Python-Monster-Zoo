# Chad Reynolds
# 12/23/13
# MonsterZoo, monster.py has the class for creating your monsters

from monstervisualizer import *

class Monster:
	"""A virtual monster to take care of."""
	total = 0
	HUNGRY = 5
	BORED = 4
	DIRTY = 5
	SLEEPY = 6
	SAD = 14

	def __init__(self, name):
		# monster attributes
		self._name = name
		self.hunger = 0
		self.boredom = 0
		self.dirtiness = 0
		self.sleepiness = 0
		self._mood = "happy"
		total += 1

		# the visualizer
		self.visual = Visualizer(self._mood, self.name)

	def __str__(self):
		return "{0} is currently {1}.".format(name, mood)

	@property
	def name(self):
		"""Get the monster's name."""
		return _name

	@name.setter
	def name(self, value):
		"""Set the monster's name."""
		if value == "":
			raise ValueError("Cannot have a monster with an empty name.")
		else:
			_name = value

	@property
	def mood(self):
		"""Get the current mood."""
		if self.hunger + self.boredom + self.dirtiness + self.sleepiness > SAD:
			self._mood = "sad"
			self.visual.show_sad()
		elif self.hunger > HUNGRY:
			self._mood = "hungry"
		elif self.sleepiness > SLEEPY:
			self._mood = "sleepy"
		elif self.boredom > BORED:
			self._mood = "bored"
		elif self.dirtiness > DIRTY:
			self._mood = "dirty"
		else:
			self._mood = "happy"
			self.visual.show_happy()

		return self._mood

	def _pass_time(self):
		"""Shows the passage of time on the monster as events occur."""
		self.hunger += 1
		self.boredom += 1
		self.dirtiness += 1
		self.sleepiness += 1

	def feed_monster(self, food = 3):
		"""Feeds the monster an amount of food."""
		self._pass_time()
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0

	def nap_time(self, rest = 6):
		"""Gives the monster a nap for number of hours."""
		self._pass_time()
		self.sleepiness -= rest
		if self.sleepiness < 0:
			self.sleepiness = 0

	def play_time(self, fun = 3):
		"""Plays with the monster for a number of hours."""	
		self._pass_time()
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0	

	def give_bath(self, soap = 5):
		"""Cleans the monster off."""
		self._pass_time()
		self.dirtiness -= soap
		if self.dirtiness < 0:
			self.dirtiness = 0

	def debug(self, hungry, sleepy, bored, dirt):
		"""Changes stats by given values for testing."""
		self.hunger += hungry
		self.sleepiness += sleepy
		self.boredom += bored
		self.dirtiness += dirt
