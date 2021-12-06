from tkinter import *

import tkinter as tk
import numpy as np


class GUI:
    def __init__(self):
        self.button_dict = dict()
        self.window = tk.Tk()

    def callback_function(self, x):
        self.OutVal = x
        self.window.destroy()

    def Show(self, Question, Answers):
        self.button_dict = dict()
        lbl = Label(text='\n'+Question+'\n')
        lbl.pack()
        for index, dat in enumerate(Answers):
            button = tk.Button(self.window, text=dat, command=lambda dat=dat,
            index=index: self.callback_function(index), width='20', height='2')
            # кнопки номеруются сверху вниз
            button.pack()
            self.button_dict[dat] = button
        self.window.mainloop()

        return self.OutVal




class DATA: #собирает и выдаёт нужную информацию той или иной функции
   def __init__(self):
       self.Queston_and_Button_answers = [["Вы уверены?", ["Да", "Не знаю", "Нет"]],
                                          ['шашалык ?', ['да', 'нет', 'ответ']]]
       #переменная построенна по структуре :
       #[[question,[button_answers,button_answers]],[question,[button_answers,button_answers]]]

   def DATA_COLLECT(self):# возвращает значения введённые пользователем
       self.Outvalue = []
       for x in self.Queston_and_Button_answers:
           n = GUI()
           self.Outvalue.append(n.Show(x[0], x[1]))
       self.Outvalue = np.array(self.Outvalue)
       print(self.Outvalue)


m = DATA()
m.DATA_COLLECT()# вызываем