import numpy as np
import pathlib


class NN:
    def __init__(self):
        self._model = None
        self._path = pathlib.Path(__file__).parent
        print()
    def create(self):
        pass
    def Load(self):#загрузка
        self._model= load_model(self._path.joinpath(__class__.__name__))
    def Save(self):
        self._model.safe(self._path)

m = NN()