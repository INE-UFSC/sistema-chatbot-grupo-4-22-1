from Bots.Bot import Bot

class BotSolitario(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.comandos({
            "1": ("Bom dia", "Bom dia, amigo!!!"),
            "2": ("Qual o seu nome?", "Ah, desculpa, eu não lembro... faz muito tempo que não me perguntam meu nome... mas pode me chamar de Sozinho!"),
            "3": ("Quero um conselho", "Uhm... eu não sou muito bom com pessoas, mas sempre valorize seus amigos! Você nunca sabe quando eles vão te deixar.") })
        
        

    def apresentacao(self):
        return "Ah- Oi... eu sou o Sozinho, e gostaria muito de ser seu amigo"
 
    def mostra_comandos(self):
        return self.__comandos
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return "É sério??? Você me escolheu??? Eba! Um amigo!!!"

    def despedida(self):
        return "Como sempre... todos sempre acabam me abandonando... é tudo minha culpa..."
