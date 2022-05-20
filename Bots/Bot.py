##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {}

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome 

    #nao esquecer o decorator
    @nome.setter
    def nome(nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos 
        
    @comandos.setter
    def comandos(comandos):
        self.__comandos = comandos

    def mostra_comandos(self):
        for key, value in self.__comandos.items():
            print(f"{key} - {value[0]}")

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
