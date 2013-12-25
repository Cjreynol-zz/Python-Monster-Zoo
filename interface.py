# Chad Reynolds
# 12/24/13
# Creates an interface to hold multiple managers

from manager import *

class Interface():
	"""Main Window to add and hold multiple monsters."""
	def __init__(self):
		self.root = Tk()
		self.root.title("Monster Zoo")

		self.button = Button(self.root, text = "Add Monster", command = self.add_monster)
		self.button.pack()

	def add_monster(self):
		"""Creates a name menu to add a new monster."""
		new = Name_Window(self.root)	

	def mainloop(self):
		"""Starts the root's mainloop."""
		self.root.mainloop()
