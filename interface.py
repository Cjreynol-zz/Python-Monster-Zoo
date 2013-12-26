# Chad Reynolds
# 12/24/13
# Creates an interface to hold multiple managers

from tkinter import *
from manager import Name_Window, Manager

class Interface():
	"""Main Window to add and hold multiple monsters."""
	def __init__(self):
		self.root = Tk()
		self.root.title("Monster Zoo")

		self.interface_frame = Frame(self.root)
		self.interface_frame.pack()

		self.button = Button(self.interface_frame, text = "Add Monster", command = self.add_monster)
		self.button.pack(side = LEFT)

		self.monster_total = IntVar()
		self.monster_total.set(0)
		self.total = Label(self.interface_frame, textvariable = self.monster_total)
		self.total.pack(side = RIGHT)

		Label(self.interface_frame, text = "Monster Total:  ").pack(side = RIGHT)		

	def add_monster(self):
		"""Creates a name menu to add a new monster."""
		new = Name_Window(self.root, self.monster_total)	

	def mainloop(self):
		"""Starts the root's mainloop."""
		self.root.mainloop()
