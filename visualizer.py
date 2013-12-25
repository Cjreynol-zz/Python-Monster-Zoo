# Chad Reynolds
# 12/23/13
# Monster Visualizer, shows an image of the monster based on their mood.
# based on the idea that there is a folder in the current directory called monsterimages
# this directory contains the images:  happy, sad, hungry, sleepy, bored, dirty

from tkinter import *
import os

class Visualizer:
	"""Image to visualize the mood the Monster."""

	def __init__(self, mood, name):
		# create window
		self.root = Toplevel()
		self.root.title(name)
		self.root.resizable(width = False, height = False)

		# load all images
		if os.path.isdir(name):			
			self.happy = PhotoImage(file = name + "/happy.gif")
			self.sad = PhotoImage(file = name + "/sad.gif")
			self.hungry = PhotoImage(file = name + "/hungry.gif")
			self.sleepy = PhotoImage(file = name + "/sleepy.gif")
			self.bored = PhotoImage(file = name + "/bored.gif")
			self.dirty = PhotoImage(file = name + "/dirty.gif")
		else:
			self.happy = PhotoImage(file = "default/happy.gif")
			self.sad = PhotoImage(file = "default/sad.gif")
			self.hungry = PhotoImage(file = "default/hungry.gif")
			self.sleepy = PhotoImage(file = "default/sleepy.gif")
			self.bored = PhotoImage(file = "default/bored.gif")
			self.dirty = PhotoImage(file = "default/dirty.gif")
	
		# create label and display
		self.image = Label(self.root, image = self.happy)
		self.image.pack()

	def show_happy(self):
		"""Updates display with the happy image."""
		self.image.config(image = self.happy)

	def show_sad(self):
		"""Updates display with the sad image."""
		self.image.config(image = self.sad)

	def show_hungry(self):
		"""Updates display with the hungry image."""
		self.image.config(image = self.hungry)

	def show_sleepy(self):
		"""Updates display with the sleepy image."""
		self.image.config(image = self.sleepy)

	def show_bored(self):
		"""Updates display with the bored image."""
		self.image.config(image = self.bored)

	def show_dirty(self):
		"""Updates display with the bored image."""
		self.image.config(image = self.dirty)
