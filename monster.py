# Chad Reynolds
# 12/23/13
# Has the Monster class to create and interface with monsters

class Monster:
	"""A virtual monster to take care of."""
	HUNGRY = 5
	BORED = 4
	DIRTY = 5
	SLEEPY = 6
	SAD = 18
	
	DEAD = 200
	OLD = 150
	ADULT = 100
	TEENAGER = 50
	CHILD = 25

	def __init__(self, name):
		# monster attributes
		self.name = name
		self.hunger = 0
		self.boredom = 0
		self.dirtiness = 0
		self.sleepiness = 0
		self._age = 0

	@property
	def mood(self):
		"""Get the current mood and update Visualizer."""
		if self.hunger + self.boredom + self.dirtiness + self.sleepiness >= Monster.SAD:
			return "sad"
		elif self.hunger >= Monster.HUNGRY:
			return  "hungry"
		elif self.boredom >= Monster.BORED:
			return "bored"
		elif self.sleepiness >= Monster.SLEEPY:
			return "sleepy"
		elif self.dirtiness >= Monster.DIRTY:
			return "dirty"
		else:
			return "happy"

	@property
	def age(self):
		"""Gets the current age descriptor and updates Visualizer."""
		if self._age >= Monster.DEAD:
			return "Dead"
		elif self._age >= Monster.OLD:
			return "Old"
		elif self._age >= Monster.ADULT:
			return "Adult"
		elif self._age >= Monster.TEENAGER:
			return "Teenager"
		elif self._age >= Monster.CHILD:
			return "Child"
		else:
			return "Baby"

	def _pass_time(self):
		"""Shows the passage of time on the monster as events occur."""
		self._age += self._age_monster(self.mood)
		self.hunger += 1
		self.boredom += 1
		self.dirtiness += 1
		self.sleepiness += 1

	def _age_monster(self, state):
		"""Determines how much the monster ages based on it's state."""
		if state == "sad":
			return 3
		elif state == "hungry" or state == "bored":
			return 2
		elif state == "sleepy" or state == "dirty":
			return 1
		else:
			return 0

	def feed(self, food = 3):
		"""Feeds the monster an amount of food."""
		self._pass_time()
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0

	def nap(self, rest = 7):
		"""Gives the monster a nap for number of hours."""
		self._pass_time()
		self.sleepiness -= rest
		if self.sleepiness < 0:
			self.sleepiness = 0

	def play(self, fun = 4):
		"""Plays with the monster for a number of hours."""	
		self._pass_time()
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0	

	def clean(self, soap = 5):
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
