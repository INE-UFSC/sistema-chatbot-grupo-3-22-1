from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        self.__lista_bots = list()
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                print(f"Objeto {bot} não é do tipo bot!\n")
            else:
                self.__lista_bots.append(bot)

        self.__bot = None
    
    def boas_vindas(self):
        print("Olá, esse é o sistema de chatbots da empresa " + self.__empresa)
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são: ")
        for bot in self.__lista_bots:
            print(str(self.__lista_bots.index(bot)) + " - Bot: " + bot.nome + ": " + bot.apresentacao())
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        try:
            escolha = input("Digite o número do bot desejado:")
            self.__bot = self.__lista_bots[int(escolha)]
        except:
            print("Número selecionado inválido")
            self.escolhe_bot()
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def boas_vindas_bot(self):
        print(self.__bot.boas_vindas())

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        codigoDoComando = input("Digite o comando desejado " + "(" + "ou -1 para fechar o programa e sair" + "): ")
        print()
        if codigoDoComando == "-1":
            print(self.__bot.despedida())
        else:
            print(" -", self.__bot.executa_comando(codigoDoComando), "\n")
            self.mostra_comandos_bot()
            self.le_envia_comando()
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.boas_vindas_bot()
        self.mostra_comandos_bot()
        self.le_envia_comando()
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
