# Chad Reynolds
# 12/27/13
# Create a class to be used by the manager to keep track of the stats of the monster, and display them when it dies.


class Stat_Tracker():
	"""Keeps track of monster stats."""

	def __init__(self):
		self.fed = 0
		self.napped = 0
		self.cleaned = 0
		self.played = 0

		self.happy = 0
		self.sad = 0
		self.hungry = 0
		self.bored = 0
		self.dirty = 0
		self.sleepy = 0

		self.baby = 0
		self.child = 0
		self.teenager = 0
		self.adult = 0
		self.old = 0

	def update_stats(self, action, mood, age):
		"""Determines and updates stats based on the parameters."""
		# action
		if action == "feed":
			self.fed += 1
		elif action == "nap":
			self.napped += 1
		elif action == "clean":
			self.cleaned += 1
		else:
			self.played += 1

		# mood
		if mood == "happy":
			self.happy += 1
		elif mood == "sad":
			self.sad += 1
		elif mood == "hungry":
			self.hungry += 1
		elif mood == "bored":
			self.bored += 1
		elif mood == "dirty":
			self.dirty += 1
		else:
			self.sleepy += 1

		# age
		if age == "Baby":
			self.baby += 1
		elif age == "Child":
			self.child += 1
		elif age == "Teenager":
			self.teenager += 1
		elif age == "Adult":
			self.adult += 1
		else:
			self.old += 1

	def monster_death(self, manager):
		"""Displays a window upon the monster's death to display stats and then remove the monster from the zoo."""
		root = Toplevel()
		root.title("{0} has died :(".format(manager.monster.name))

		total = self.fed + self.napped + self.played + self.bored
		lifespan = Label(root, text = "They lived for {0} actions.\n\n".format(total))
		lifespan.pack()

		actions = Label(root, text = "Fed {0} times.\nCleaned {1} times.\nNapped {2} times.\nPlayed {3} times.\n\n".format(self.fed, self.cleaned, self.napped, self.played)
		actions.pack()

		mood = Label(root, text = "Happy for {0} actions.\nSad for {1} actions.\nHungry for {2} actions.\nBored for {3} actions.\nSleepy for {4} actions.\nDirty for {5} actions.\n\n".format(self.happy, self.sad, self.hungry, self.bored, self.sleepy, self.dirty))
		mood.pack()

		age = Label(root, text = "Baby for {0} actions.\nChild for {1} actions.\nTeenager for {2} actions.\nAdult for {3} actions.\nOld for {4} actions.\n\n".format(self.baby, self.child, self.teenager, self.adult, self.old))
		age.pack()
		
		def say_goodbye():
			"""Closes manager for dead monster and stats window."""
			manager.euthanize()
			root.destroy()

		goodbye = Button(root, text = "Say Goodbye", command = say_goodbye)
		goodbye.pack()
