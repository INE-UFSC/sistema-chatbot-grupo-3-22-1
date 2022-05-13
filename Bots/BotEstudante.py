from Bots.Bot import Bot

class BotEstudante(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "Me salva, tem CTS hoje!"

    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        pass

    def despedida(self):
        pass