from codeop import CommandCompiler
from Bots.Bot import Bot


class BotEspelhado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {
            "1": ("Bom Dia", "aiD moB"),
            "2": ("Qual o seu nome?", "rorriM é emon ueM"),
            "3": ("Quero um conselho", "ohlepse on rahlo oa airros erpmeS")
        }

    def apresentacao(self):
        return "...odahlepse é olaf ue euq o odut ,odahlepsE toB o uos rorriM é emon uem ,álO"

    def mostra_comandos(self):
        return self.__comandos

    def executa_comando(self, cmd):
        return self.__comandos[cmd]

    def boas_vindas(self):
        return "...odnalaf uotse euq o rednetne arap amelborp ahnet oãn euq orepse ,uehlocse em êcov abO"

    def despedida(self):
        return "...amixórp a éta ,raduja et redop mob otium ioF"
