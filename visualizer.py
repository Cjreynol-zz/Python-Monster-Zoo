# Chad Reynolds
# 12/23/13
# Monster Visualizer, shows an image of the monster based on their mood.
# based on the idea that there is a folder in the current directory called monsterimages
# this directory contains the images:  happy, sad, hungry, sleepy, bored, dirty

from tkinter import *
import os

class Visualizer:
	"""Image to visualize the mood the Monster."""

	def __init__(self, name, root):
		self.happy = PhotoImage(file = "moods/happy.gif")
		self.sad = PhotoImage(file = "moods/sad.gif")
		self.hungry = PhotoImage(file = "moods/hungry.gif")
		self.sleepy = PhotoImage(file = "moods/sleepy.gif")
		self.bored = PhotoImage(file = "moods/bored.gif")
		self.dirty = PhotoImage(file = "moods/dirty.gif")
	
		self.mood_image = Label(root, image = self.happy)

		if os.path.isdir(name):
			self.dead = PhotoImage(file = name + "/dead.gif")
			self.old = PhotoImage(file = name + "/old.gif")
			self.adult = PhotoImage(file = name + "/adult.gif")
			self.teenager = PhotoImage(file = name + "/teenager.gif")
			self.child = PhotoImage(file = name + "/child.gif")
			self.baby = PhotoImage(file = name + "/baby.gif")
		else:
			self.dead = PhotoImage(file = "default/dead.gif")
			self.old = PhotoImage(file = "default/old.gif")
			self.adult = PhotoImage(file = "default/adult.gif")
			self.teenager = PhotoImage(file = "default/teenager.gif")
			self.child = PhotoImage(file = "default/child.gif")
			self.baby = PhotoImage(file = "default/baby.gif")

		self.monster_image = Label(root, image = self.baby)
	
	def update_mood(self, state):
		"""Changes the mood image based on the passed in mood."""
		if state == "sad":
			self.mood_image.config(image = self.sad)
		elif state == "hungry":
			self.mood_image.config(image = self.hungry)
		elif state == "sleepy":
			self.mood_image.config(image = self.sleepy)
		elif state == "bored":
			self.mood_image.config(image = self.bored)
		elif state == "dirty":
			self.mood_image.config(image = self.dirty)
		else:
			self.mood_image.config(image = self.happy)
	
	def update_age(self, state):
		"""Changes the monster image based on the passed in age."""
		if state == "Dead":	
			self.monster_image.config(image = self.dead)
		elif state == "Old":
			self.monster_image.config(image = self.old)
		elif state == "Adult":	
			self.monster_image.config(image = self.adult)
		elif state == "Teenager":
			self.monster_image.config(image = self.teenager)
		elif state == "Child":
			self.monster_image.config(image = self.child)
		else:
			self.monster_image.config(image = self.baby)

