from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
            else:
                print("ERRO: algum Bot não é Bot!")

        self.__bot = None
    
    def boas_vindas(self):
        print(f"Olá, este é o sistema de chatBots da empresa {self.__empresa}!")

    def mostra_menu(self):
        print(f"Os chatBots disponíveis no momento são:\n")
        for index, bot in enumerate(self.__lista_bots):
            print(f"{index} - {bot.nome}: {bot.apresentacao()}")
    
    def escolhe_bot(self):
        while True:
            escolha = input("Digite o número do Bot escolhido: ")
            
            try:
                escolha = int(escolha)
            except ValueError:
                print("\nDigite somente números!\n")
            else:
                if escolha >= len(self.__lista_bots) or escolha < 0:
		                print("Escolha inválida! Tente novamente!")
                else:
		                self.__bot = self.__lista_bots[int(escolha)]
		                break

    def le_envia_comando(self):
        escolha = input("Digite o comando desejado (ou -1 p/ fechar o programa): ")
        
        if escolha == "-1":
            return False
        
        if escolha in self.__bot.comandos.keys():
            print("\n", self.__bot.comandos[escolha][1], "\n")
        else:
            print("\nEscolha inválida! Tente novamente!\n")

    def escolher_comando(self):
        while True:
            self.__bot.mostra_comandos()
            if self.le_envia_comando() == False:
                break

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        self.escolher_comando()
        self.__bot.despedida()
