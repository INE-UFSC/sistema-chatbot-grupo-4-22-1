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
        while True:
            print("Digite o número do Bot escolhido: ", end="")
            escolha = int(input())
            
            if escolha > len(self.__lista_bots) or escolha < 0:
		            print("Escolha inválida! Tente novamente")
            else:
		            self.__bot = self.__lista_bots[int(escolha)]
		            break
		      	

    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        for key, value in self.__bot.mostra_comandos().items():
                 print(f"{key} - {value[0]}")

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        print("Digite o comando desejado (ou -1 p/ fechar o programa): ", end="")
        escolha = input()
        
        if escolha == "-1":
            return False
            
        for key, value in self.__bot.mostra_comandos().items():
            if key == escolha:
                 print("\n", value[1], "\n")

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        print(self.boas_vindas())
				
        ##mostra o menu ao usuário
        self.mostra_menu()
        
        ##escolha do bot
        self.escolhe_bot()
        
        ##mostra mensagens de boas-vindas do bot escolhido
        print("\n", self.__bot.boas_vindas(), "\n")
        
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            self.mostra_comandos_bot()
            if self.le_envia_comando() == False:
                break
        ##ao sair mostrar a mensagem de despedida do bot
        print("\n", self.__bot.despedida())
