from Bots.Bot import Bot

class BotPiada(Bot):
    def __init__(self,nome):
        self.__nome = nome
        super().comando = {
            "1": ("","")
            "2": ("","")
            "3": ("","")
            "4": ("","")
        }

    @property
    def nome(self):
        pass

    @nome.setter
    def nome(nome):
        pass

    def apresentacao(self):
        return("%s - Mensagem de apresentação: HAHAHAHAH, Meu nome é %s e você é um bananão!")
 
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        pass

    def despedida(self):
        pass