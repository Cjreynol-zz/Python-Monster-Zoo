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

	def show_happy(self):
		"""Updates display with the happy image."""
		self.mood_image.config(image = self.happy)

	def show_sad(self):
		"""Updates display with the sad image."""
		self.mood_image.config(image = self.sad)

	def show_hungry(self):
		"""Updates display with the hungry image."""
		self.mood_image.config(image = self.hungry)

	def show_sleepy(self):
		"""Updates display with the sleepy image."""
		self.mood_image.config(image = self.sleepy)

	def show_bored(self):
		"""Updates display with the bored image."""
		self.mood_image.config(image = self.bored)

	def show_dirty(self):
		"""Updates display with the bored image."""
		self.mood_image.config(image = self.dirty)

	def show_dead(self):
		"""Updates display with dead image."""
		self.monster_image.config(image = self.dead)

	def show_old(self):
		"""Updates display with old image."""
		self.monster_image.config(image = self.old)

	def show_adult(self):
		"""Updates display with adult image."""
		self.monster_image.config(image = self.adult)
	
	def show_teenager(self):
		"""Updates display with the teenager image."""
		self.monster_image.config(image = self.teenager)

	def show_child(self):
		"""Updates display with the child image."""
		self.monster_image.config(image = self.child)

	def show_baby(self):
		"""Updates display with the baby image."""
		self.monster_image.config(image = self.baby)
