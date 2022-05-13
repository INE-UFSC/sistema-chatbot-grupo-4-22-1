from codeop import CommandCompiler
from Bots.Bot import Bot


class BotEspelhado(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().comandos = {
            "1": ("Bom Dia", "")
            "2": ("Qual o seu nome?", "")
            "3": ("Quero um conselho", "")
            "4": ("Adeus", "")
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
        return "...odahlepse é olaf ue euq o odut ,odahlepsE toB o uos rorriM é emon uem ,álO" #fazer o nome ser printado utilizando o self.__nome espelhado

    def mostra_comandos(self):
        return self.comandos

    def executa_comando(self, cmd):
        pass

    def boas_vindas(self):
        return "...odnalaf uotse euq o rednetne arap amelborp ahnet oãn euq orepse ,uehlocse em êcov abO"

    def despedida(self):
        return ""
