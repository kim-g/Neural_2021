from tkinter import *

import tkinter as tk
import numpy as np


class App:
   def __init__(self):
      self.num_of_question = 0
      self.window = tk.Tk()
      self.btn1 = Button(width='20', height='2')
      self.btn2 = Button(width='20', height='2')
      self.btn1.pack()
      self.btn2.pack()
      self.window.mainloop()



m = App()
