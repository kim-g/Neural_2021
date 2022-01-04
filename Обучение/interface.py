from tkinter import *

import tkinter as tk
import numpy as np
import sqlite3


class GUI:
    def __init__(self):
        self.button_dict = dict()
        self.window = tk.Tk()
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry('%dx%d+0+0' % (self.w, self.h))

    def callback_function(self, x):#функция возврата информации в
        self.OutVal = x
        self.window.destroy()

    def Show(self, Question, Answers, Amount_of_answers, num_of_question):
        self.button_dict = dict()
        if Question == None:
            return
        row, column =self.window.grid_size()

        lbl = Label(text='\n'+Question+'\n')
        lbl1 = Label(text=f' Ответ номер : {num_of_question}/{Amount_of_answers[0][0]}'
                     , font='defult 19')#виджет номера ответа
        lbl2 = Label(text=f'Осталось : {Amount_of_answers[0][0]-num_of_question}/{Amount_of_answers[0][0]}'
                     , font='defult 19')#виджет количества оставшихся отетов
        lbl3 = Label(bg='Grey', fg='white', font='defult 10', text=f'\n   Credit\n\n\n\n\n', anchor='w')#виджет credit

        lbl.pack()
        for index, dat in enumerate(Answers):
            button = tk.Button(self.window, text=dat, command=lambda dat=dat,
            index=index: self.callback_function(index), width='20', height='2')
            # кнопки номеруются сверху вниз
            button.pack()
            self.button_dict[dat] = button
        lbl1.pack(side=RIGHT)
        lbl2.pack(side=LEFT)
        lbl3.place(relx=0, rely=0.84, width=self.w)

        self.window.mainloop()

        return self.OutVal




class DATA: #собирает и выдаёт нужную информацию той или иной функции
   def __init__(self):
       self.Queston_and_Button_answers = []
       self.con = sqlite3.connect('answers_and_question (1-я копия).db3')
       self.cur = self.con.cursor()
       #переменная построенна по структуре :
       #[[question,[button_answers,button_answers]],[question,[button_answers,button_answers]]]

   def DATA_COLLECT(self):# возвращает значения введённые пользователем
       self.Outvalue = []
       num_of_question = 0

       for x in self.Queston_and_Button_answers:
           num_of_question += 1
           n = GUI()
           a = n.Show(x.Question, x.Button_answers, self.cur.execute('SELECT Count(question_text) FROM question').fetchall(), num_of_question)
           if a == None:#игнорируем вывод None и незаписываем его в self.Outvalue
               continue
           self.Outvalue.append(a)
       self.Outvalue = np.array(self.Outvalue)
       print(self.Outvalue)

   def Load(self):#выгружаем и переводим данные из sql таблицы в понятные программе
       result_table = self.cur.execute('SELECT * FROM question')
       for question in result_table.fetchall():
           answers = self.cur.execute(f'SELECT answer FROM answers_for_buttons WHERE id_of_question ={question[0]}')
           Quest = Sql_decode()
           Quest.Question = question[1]

           for answer in answers.fetchall() :
               Quest.Button_answers.append(answer[0])

           self.Queston_and_Button_answers.append(Quest)



class Sql_decode:
    def __init__(self):
        self.Button_answers = []
        self.Question = ''





m = DATA()
m.Load()
m.DATA_COLLECT()
