from Bots.Bot import Bot

class BotPiada(Bot):
    def __init__(self, nome):
        self.nome = nome
        self.__comandos = {
            "1": ("Bom Dia", "Bom dia! O que for para ser será (mas tomara que seja o que eu quero)"),
            "2": ("Qual o seu nome?", "Meu nome é Roger"),
            "3": ("Conte uma piada", "O que o pato disse para a pata?\nVem Quá!")
        }

    # nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    # nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "- Mensagem de apresentação: HAHAHAHAH, Meu nome é %s e você é um bananão!"
 
    def mostra_comandos(self):
        return self.__comandos
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return "Agora que me escolheu venha rir comigo"

    def despedida(self):
        return "Até a proxima piada"