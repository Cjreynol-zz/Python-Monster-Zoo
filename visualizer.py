# Chad Reynolds
# 12/23/13
# Monster Visualizer, shows an image of the monster based on their mood.
# based on the idea that there is a folder in the current directory called monsterimages
# this directory contains the images:  happy, sad, hungry, sleepy, bored, dirty

from tkinter import *

class Visualizer:
	"""Creates a form to visualize the Monster."""

	def __init__(self, mood, name):
		# create window
		self.root = Tk()
		self.root.title(name)
		self.root.resizable(width = False, height = False)

		# load all images
		self.happy = PhotoImage(file = "monsterimages/happy.gif")
		self.sad = PhotoImage(file = "monsterimages/sad.gif")
		self.hungry = PhotoImage(file = "monsterimages/hungry.gif")
		self.sleepy = PhotoImage(file = "monsterimages/sleepy.gif")
		self.bored = PhotoImage(file = "monsterimages/bored.gif")
		self.dirty = PhotoImage(file = "monsterimages/dirty.gif")
	
		# create label and display
		self.image = Label(self.root, image = self.happy)
		self.image.pack()

		#self.root.mainloop()

	def show_happy(self):
		"""Updates display with the happy image."""
		self.image.config(image = self.happy)

	def show_sad(self):
		"""Updates display with the sad image."""
		self.image.config(image = self.sad)

	def hungry(self):
		"""Updates display with the hungry image."""
		self.image.config(image = self.hungry)

	def sleepy(self):
		"""Updates display with the sleepy image."""
		self.image.config(image = self.sleepy)

	def bored(self):
		"""Updates display with the bored image."""
		self.image.config(image = self.bored)

	def dirty(self):
		"""Updates display with the bored image."""
		self.image.config(image = self.dirty)
