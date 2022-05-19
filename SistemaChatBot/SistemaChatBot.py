from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)

        self.__bot = None
    
    def boas_vindas(self):
        return(f"Olá, este é o sistema de chatBots da empresa {self.__empresa}!")
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print(f"Os chatBots disponíveis no momento são: ")
        for bot in range(0, len(self.__lista_bots)):
            print(f"{bot} - Bot: {self.__lista_bots[bot].apresentacao()}")
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot
        print("Digite o número do Bot escolhido: ", end="")
        self.__bot = self.__lista_bots[int(input())]

    def mostra_comandos_bot(self):
        pass
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        print(self.boas_vindas())
				
        ##mostra o menu ao usuário
        self.mostra_menu()
        
        ##escolha do bot
        self.escolhe_bot()
        
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            for key, value in self.__bot.mostra_comandos().items():
                 print(f"{key} - {value[0]}")
            
            print("Digite o comando desejado (ou -1 p/ fechar o programa): ", end="")
            escolha = input()
            
            if escolha == "-1":
                break
                
            for key, value in self.__bot.mostra_comandos().items():
                if key == escolha:
                     print(value[1])
            
        ##ao sair mostrar a mensagem de despedida do bot
