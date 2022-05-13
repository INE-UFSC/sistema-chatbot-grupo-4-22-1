from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
        	if bot is Bot:
	        	self.__lista_bots.append(bot)
	        	
        self.__bot = None
    
    def boas_vindas(self):
        return(f"Olá, este é o sistema de chatBots da empresa {self.__empresa}!")
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print(f"Os chatBots disponíveis no momento são: ")
        for bot in range(0, len(self.__lista_bots)-1):
            print(f"str{i} - Bot: {bot.apresentacao()}")
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        return(f"Digite o número do Bot escolhido: ", end="")

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
        print(self.escolhe_bot())
        self.__bot = self.__lista_bots(input())
        
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        for 
        ##ao sair mostrar a mensagem de despedida do bot
