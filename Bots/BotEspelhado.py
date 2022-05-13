from Bots.Bot import Bot

class BotEspelhado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        

    #nao esquecer o decorator
    @property
    def nome(self):
        pass

    #nao esquecer o decorator
    @nome.setter
    def nome(nome):
        pass

    def apresentacao(self):
        pass
 
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        pass

    def despedida(self):
        pass