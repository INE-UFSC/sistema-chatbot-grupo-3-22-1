from Bots.Bot import Bot
from random import choice

class BotCansado(Bot):
    # executada ao mostrar os bots disponiveis
    def apresentacao(self):
        return "Bom dia... ou só dia mesmo."
   
    def executa_comando(self, cmd):
        if cmd in self.comandos.keys():
            resposta = choice(self.comandos[cmd][1])
            return resposta
        else:
            return "Como tudo na vida, eu não sei o que dizer..."

    # quando bot é escolhido
    def boas_vindas(self):
        return "\nSério? Eu? Pra que?\n"
    
    # chama a funcao despedida quando usa comando -1
    def despedida(self):
        return "Frase triste tchau, tamo junto, fim da jornada."