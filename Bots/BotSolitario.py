from Bots.Bot import Bot

class BotSolitario(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self.comandos['1'] =  ("Bom dia", "Bom dia, eu sou o Sozinho, e gostaria muito de ser seu amigo!")
        self.comandos['2'] = ("Qual o seu nome?", "Ah, desculpa, eu não lembro... faz muito tempo que não me perguntam meu nome... mas pode me chamar de Sozinho!")
        self.comandos['3'] = ("Quero um conselho", "Uhm... eu não sou muito bom com pessoas, mas sempre valorize seus amigos! Você nunca sabe quando eles vão te deixar.")
        self.comandos['4'] = ("Adeus", "Como sempre... todos sempre acabam me abandonando... é tudo minha culpa...")
        
    def apresentacao(self):
        return self.executa_comando('1')
 
    def mostra_comandos(self):
        for key, value in self.comandos.items():
            print (f"{key} - {value[0]}")
    
    def executa_comando(self, cmd):
        return f"{self.comandos[cmd][1]}\n"

    def boas_vindas(self):
        print("\nÉ sério??? Você me escolheu??? Eba! Um amigo!!!\n")

    def despedida(self):
        print("\n", self.executa_comando('4'))
