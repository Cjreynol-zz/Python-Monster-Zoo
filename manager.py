# Chad Reynolds
# 12/23/13
# Manager, gets name, then creates manager window

from tkinter import *
from monster import *

class Name_Window:
	"""An Intro menu to get the name of your monster."""

	def __init__(self, master):
		self.root = Toplevel()
		self.root.title("Create New")

		self.label = Label(self.root, text = "Name your monster: ")
		self.label.pack()
		self.input = Entry(self.root)
		self.input.pack()
		self.button = Button(self.root, text = "Add", command = self.start_manager)
		self.button.pack()		

		self.master = master

	def start_manager(self):
		"""Wrapper for start method to pass on entry text and reference to main window."""
		self.start(self.input.get(), self.root, self.master)

	def start(self, name, window, master):
		"""Starts Manager_Menu."""
		window.destroy()
		Manager(name, master)


class Manager:
	"""Frame of options to manage a monster."""

	def __init__(self, name, master):
		self.root = LabelFrame(master, text = name)
		self.monster = Monster(name)

		########### mood ############################################
		self.mood_label = Label(self.root, text = "Mood:  ")
		self.mood_label.grid(row = 0, column = 0)

		self.mood_state = StringVar()
		self.mood_state.set(self.monster.mood)
		Label(self.root, textvariable = self.mood_state).grid(row = 0, column = 1)

		######### hunger ############################################
		self.hunger_label = Label(self.root, text = "Hunger:  ")
		self.hunger_label.grid(row = 1, column = 0)

		self.hunger_state = StringVar()
		self.update_hunger()
		Label(self.root, textvariable = self.hunger_state).grid(row = 1, column = 1)

		self.hunger_button = Button(self.root, text = "Feed", command = self.feed)
		self.hunger_button.grid(row = 1, column = 2)

		######## sleepiness ############################################
		self.sleep_label = Label(self.root, text = "Sleepiness:  ")
		self.sleep_label.grid(row = 2, column = 0)

		self.sleep_state = StringVar()
		self.update_sleepiness()
		Label(self.root, textvariable = self.sleep_state).grid(row = 2, column = 1)

		self.sleep_button = Button(self.root, text = "Nap", command = self.nap)
		self.sleep_button.grid(row = 2, column = 2)

		######### boredom ############################################
		self.boredom_label = Label(self.root, text = "Boredom:  ")
		self.boredom_label.grid(row = 1, column = 3)

		self.boredom_state = StringVar()
		self.update_boredom()
		Label(self.root, textvariable = self.boredom_state).grid(row = 1, column = 4)

		self.boredom_button = Button(self.root, text = "Play", command = self.play)
		self.boredom_button.grid(row = 1, column = 5)

		######### dirtiness ############################################
		self.dirt_label = Label(self.root, text = "Dirtiness:  ")
		self.dirt_label.grid(row = 2, column = 3)

		self.dirt_state = StringVar()
		self.update_dirtiness()
		Label(self.root, textvariable = self.dirt_state).grid(row = 2, column = 4)

		self.dirt_button = Button(self.root, text = "Clean", command = self.clean)
		self.dirt_button.grid(row = 2, column = 5)
		
		self.root.pack()

	def update_hunger(self):
		"""Updates the hunger label by generating a string from the monster's hunger field."""
		value = self.monster.hunger	
		if value >= 2 * Monster.HUNGRY:
			text = "High"
		elif value >= Monster.HUNGRY:
			text = "Medium"
		else:
			text = "Low"
		self.hunger_state.set(text)

	def feed(self):
		"""Feeds the monster."""
		self.monster.feed()
		self.update_all()

	def update_sleepiness(self):
		"""Updates the sleepiness label by generating a string from the monster's sleepiness field."""
		value = self.monster.sleepiness
		if value >= 2 * Monster.SLEEPY:
			text = "High"
		elif value >= Monster.SLEEPY:
			text = "Medium"
		else:
			text = "Low"
		self.sleep_state.set(text)

	def nap(self):
		"""Puts the monster down for a nap."""
		self.monster.nap()
		self.update_all()

	def update_boredom(self):
		"""Updates the boredom label by generating a string from the monster's boredom field."""
		value = self.monster.boredom
		if value >= 2 * Monster.BORED:
			text = "High"
		elif value >= Monster.BORED:
			text = "Medium"
		else:
			text = "Low"
		self.boredom_state.set(text)

	def play(self):
		"""Entertains the monster."""
		self.monster.play()
		self.update_all()

	def update_dirtiness(self):
		"""Updates the dirtiness label by generating a string from the monster's dirtiness field."""
		value = self.monster.dirtiness
		if value >= 2 * Monster.DIRTY:
			text = "High"
		elif value >= Monster.DIRTY:
			text = "Medium"
		else:
			text = "Low"
		self.dirt_state.set(text)

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
