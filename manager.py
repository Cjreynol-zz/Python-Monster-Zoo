# Chad Reynolds
# 12/23/13
# Manager, gets name, then creates manager window

from tkinter import *
from monster import *

class Name_Menu:
	"""An Intro menu to get the name of your monster."""

	def __init__(self):
		self.root = Tk()
		self.root.title("Monster Zoo")

		self.label = Label(self.root, text = "Name your monster: ")
		self.label.pack()

		self.input = Entry(self.root)
		self.input.pack()

		self.button = Button(self.root, text = "Start", command = self.start_manager)
		self.button.pack()
		
		self.root.mainloop()

	def start_manager(self):
		"""Wrapper for start method that starts the manager with the name variable passed in."""
		self.start(self.input.get(), self.root)

	def start(self, name, window):
		"""Starts Manager_Menu."""
		window.destroy()
		Manager_Menu(name)


class Manager_Menu:
	"""Provides options to manage a monster."""

	def __init__(self, name):
		self.root = Tk()
		self.root.title(name + " Manager")
		
		self.monster = Monster(name)

		# mood
		self.mood_label = Label(self.root, text = "Mood:  ")
		self.mood_label.grid(row = 0, column = 0)
		self.mood_state = StringVar()
		self.mood_state.set(self.monster.mood)
		Label(self.root, textvariable = self.mood_state).grid(row = 0, column = 1)

		# hunger
		self._hunger = self.monster.hunger
		self.hunger_label = Label(self.root, text = "Hunger:  ")
		self.hunger_label.grid(row = 1, column = 0)
		self.hunger_state = StringVar()
		self.hunger_state.set(self.hunger)
		Label(self.root, textvariable = self.hunger_state).grid(row = 1, column = 1)
		self.hunger_button = Button(self.root, text = "Feed", command = self.feed)
		self.hunger_button.grid(row = 1, column = 2)

		# sleepiness
		self._sleepiness = self.monster.sleepiness
		self.sleep_label = Label(self.root, text = "Sleepiness:  ")
		self.sleep_label.grid(row = 2, column = 0)
		self.sleep_state = StringVar()
		self.sleep_state.set(self.sleepiness)
		Label(self.root, textvariable = self.sleep_state).grid(row = 2, column = 1)
		self.sleep_button = Button(self.root, text = "Nap", command = self.nap)
		self.sleep_button.grid(row = 2, column = 2)

		# boredom
		self._boredom = self.monster.boredom
		self.boredom_label = Label(self.root, text = "Boredom:  ")
		self.boredom_label.grid(row = 1, column = 3)
		self.boredom_state = StringVar()
		self.boredom_state.set(self.boredom)
		Label(self.root, textvariable = self.boredom_state).grid(row = 1, column = 4)
		self.boredom_button = Button(self.root, text = "Play", command = self.play)
		self.boredom_button.grid(row = 1, column = 5)

		# dirtiness
		self._dirtiness = self.monster.dirtiness
		self.dirt_label = Label(self.root, text = "Dirtiness:  ")
		self.dirt_label.grid(row = 2, column = 3)
		self.dirt_state = StringVar()
		self.dirt_state.set(self.dirtiness)
		Label(self.root, textvariable = self.dirt_state).grid(row = 2, column = 4)
		self.dirt_button = Button(self.root, text = "Clean", command = self.clean)
		self.dirt_button.grid(row = 2, column = 5)
		
		self.root.mainloop()

	@property
	def hunger(self):
		"""Gets a string descriptor for the monster's hunger."""
		if self._hunger >= 2 * Monster.HUNGRY:
			return "High"
		elif self._hunger >= Monster.HUNGRY:
			return "Medium"
		else:
			return "Low"

	@hunger.setter
	def hunger(self, value):
		"""Sets the value for the hunger property."""
		self._hunger = value

	def update_hunger(self):
		"""Updates the hunger label through the hunger property."""
		self.hunger = self.monster.hunger
		self.hunger_state.set(self.hunger)

	def feed(self):
		"""Feeds the monster."""
		self.monster.feed()
		self.update_all()

	@property
	def sleepiness(self):
		"""Gets a string descriptor for the monster's sleepiness."""
		if self._sleepiness >= 2 * Monster.SLEEPY:
			return "High"
		elif self._sleepiness >= Monster.SLEEPY:
			return "Medium"
		else:
			return "Low"

	@sleepiness.setter
	def sleepiness(self, value):
		"""Sets the value for the sleepiness property."""
		self._sleepiness = value

	def update_sleepiness(self):
		"""Updates the sleepiness label through the sleepiness property."""
		self.sleepiness = self.monster.sleepiness
		self.sleep_state.set(self.sleepiness)

	def nap(self):
		"""Puts the monster down for a nap."""
		self.monster.nap()
		self.update_all()

	@property
	def boredom(self):
		"""Gets a string descriptor for the mosnter's boredom."""
		if self._boredom >= 2 * Monster.BORED:
			return "High"
		elif self._boredom >= Monster.BORED:
			return "Medium"
		else:
			return "Low"

	@boredom.setter
	def boredom(self, value):
		"""Sets the value for the boredom property."""
		self._boredom = value

	def update_boredom(self):
		"""Updates the boredom label through the boredom property."""
		self.boredom = self.monster.boredom
		self.boredom_state.set(self.boredom)

	def play(self):
		"""Entertains the monster."""
		self.monster.play()
		self.update_all()

	@property
	def dirtiness(self):
		"""Gets a string descriptor for the monster's dirtiness."""
		if self._dirtiness >= 2 * Monster.DIRTY:
			return "High"
		elif self._dirtiness >= Monster.DIRTY:
			return "Medium"
		else:
			return "Low"

	@dirtiness.setter
	def dirtiness(self, value):
		"""Sets the value for the dirtiness property."""
		self._dirtiness = value

	def update_dirtiness(self):
		"""Updates the dirtiness label through the dirtiness property."""
		self.dirtiness = self.monster.dirtiness
		self.dirt_state.set(self.dirtiness)

	def clean(self):
		"""Cleans the monster."""
		self.monster.clean()	
		self.update_all()

	def update_mood(self):
		"""Updates the mood state label."""
		self.mood_state.set(self.monster.mood)

	def update_all(self):
		"""Calls all the update methods for the state labels."""
		self.update_hunger()
		self.update_sleepiness()
		self.update_boredom()
		self.update_dirtiness()	
		self.update_mood()
