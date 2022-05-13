from operator import index
from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print("Olá, esse é o sistema de chatbots da empresa " + self.__empresa)
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são: ")
        for bot in self.__lista_bots:
            print(str(index(bot)) + " - Bot: " + bot.nome + " - Mensagem de apresentação: " + bot.apresentacao())
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        escolha = input("Digite o número do bot desejado:")
        self.__bot = self.__lista_bots[escolha]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        códigoDoComando = input("Digite o comando desejado " + "(" + "ou -1 para fechar o programa e sair" + ")")
        if códigoDoComando == -1:
            self.__bot.despedida()
        else:
            self.__bot.executa_comando(códigoDoComando)
            self.le_envia_comando()
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.boas_vindas()
        self.le_envia_comando()
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
