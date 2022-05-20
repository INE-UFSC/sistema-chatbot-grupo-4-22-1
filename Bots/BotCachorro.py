from Bots.Bot import Bot

class BotCachorro(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__nome = nome
        self.comandos['1'] = ("Bom dia!", "Woof Woof")
        self.comandos['2'] = ("Senta", "[Theo sentou]")
        self.comandos['3'] = ("Qual o seu brinquedo favorito?", "Woof Woof")
        self.comandos['4'] = ("Adeus", "Theo sentirá sua falta")

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Woof"
 
    #def mostra_comandos(self):
    #    return self.comandos['a']
    
    def executa_comando(self,cmd):
        if cmd in self.comandos:
            return f"\nVocê --> {self.comandos[cmd][0]}\n{self.__nome} --> {self.comandos[cmd][1]}\n"
        else:
            return "Woof?"

    def boas_vindas(self):
        return self.executa_comando('1')

    def despedida(self):
        return self.executa_comando('4')
