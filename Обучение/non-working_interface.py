from tkinter import *

import tkinter as tk
import numpy as np


class App:
	def __init__(self):
		self.data2 = ["Иногда чувствую", "Никогда не чувствую"]
		self.button_dict = dict()
		OutVal = ""
		self.window = tk.Tk()

	def callback_function(self, x): 
		#print('Pressed:', x)
		self.OutVal = x
		self.window.destroy()

	def Show(self, Question, Answers):
		self.button_dict = dict()
		for index, dat in enumerate(Answers):
			button = tk.Button(self.window, text=dat, command=lambda dat=dat: self.callback_function(dat), width='20', height='2')
			button.pack()
			self.button_dict[dat] = button
			
		self.window.mainloop()

		print (self.OutVal)
		return self.OutVal



m = App()
m.Show("Вы уверены?", ["Да","Не знаю","Нет"])
