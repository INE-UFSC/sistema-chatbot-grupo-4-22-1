##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.comandos = {}

    #nao esquecer o decorator
    @property
    def nome(self):
        pass 

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        pass

    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
