import numpy as np
import pathlib
from tensorflow import keras
from keras import *
from keras.layers import *
import matplotlib.pyplot as plt

class NN:
    def __init__(self):
        self._model = None
        self._path = pathlib.Path(__file__).parent
        print()
    def create(self):
        pass
    def Load(self):#загрузка
        self._model = keras.load_model(self._path.joinpath("Data"+self.__class__.__name__+'.h5'))
    def Save(self):
        self._model = keras.save("Data"+self.__class__.__name__+'.h5')# нетрож .save
        #сохраняет все:
        #    Значения весов
        #    Конфигурацию модели (архитектуру)
        #    Конфигурацию оптимизатора


#классы нейронок
class NN1(NN):
    def craete(self, training_sample, answer, test):
        model = Sequential(Dense(45, activation='relu'),
                           Dense(90, activation='relu'),
                           Dense(180, activation='relu'),
                           Dense(45, activation='relu'),
                           Dense(3, activation='relu'),
                           Dense(1, activation='relu'))
        model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0, 1))
        history = model.fit(x=training_sample, y=answer, epochs=100)
        plt.plot(history.history['loss'])
        plt.grid(True)
        plt.show()
        print(model.get_weights(), '\n', model.summary())
        print(model.evaluate(test, answer))

class NN2(NN):
    def craete(self, training_sample, answer, test):
        model = Sequential(Dense(45, activation='relu'),
                           Dense(22, activation='relu'),
                           Dense(11, activation='relu'),
                           Dense(5, activation='relu'),
                           Dense(3, activation='relu'),
                           Dense(1, activation='relu'))
        model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0, 1))
        history = model.fit(x=training_sample, y=answer, epochs=100)
        plt.plot(history.history['loss'])
        plt.grid(True)
        plt.show()
        print(model.get_weights(), '\n', model.summary())
        print(model.evaluate(test, answer))

class NN3(NN):
    def craete(self, training_sample, answer, test):
        model = Sequential(Dense(45, activation='relu'),
                           Dense(22, activation='relu'),
                           Dense(10, activation='relu'),
                           Dense(45, activation='relu'),
                           Dense(180, activation='relu'),
                           Dense(22, activation='relu'),
                           Dense(5, activation='relu'),
                           Dense(1, activation='relu'))
        model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0, 1))
        history = model.fit(x=training_sample, y=answer, epochs=100)
        plt.plot(history.history['loss'])
        plt.grid(True)
        plt.show()
        print(model.get_weights(), '\n', model.summary())
        print(model.evaluate(test, answer))

class NN4(NN):
    def craete(self, training_sample, answer, test):
        model = Sequential(Dense(45, activation='relu'),
                           Dense(90, activation='relu'),
                           Dense(45, activation='relu'),
                           Dense(180, activation='relu'),
                           Dense(45, activation='relu'),
                           Dense(1, activation='relu'))
        model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0, 1))
        history = model.fit(x=training_sample, y=answer, epochs=100)
        plt.plot(history.history['loss'])
        plt.grid(True)
        plt.show()
        print(model.get_weights(), '\n', model.summary())
        print(model.evaluate(test, answer))

class NN5(NN):
    def craete(self, training_sample, answer, test):
        model = Sequential(Dense(45, activation='relu'),
                           Dense(90, activation='relu'),
                           Dense(45, activation='relu'),
                           Dense(90, activation='relu'),
                           Dense(3, activation='relu'),
                           Dense(1, activation='relu'))
        model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0, 1))
        history = model.fit(x=training_sample, y=answer, epochs=100)
        plt.plot(history.history['loss'])
        plt.grid(True)
        plt.show()
        print(model.get_weights(), '\n', model.summary())
        print(model.evaluate(test, answer))
