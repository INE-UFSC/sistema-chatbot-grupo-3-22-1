from Bots.Bot import Bot
from random import choice

class BotCansado(Bot):

    # executada ao mostrar os bots disponiveis
    def apresentacao(self):
        return "Bom dia... ou só dia mesmo."
   
    def executa_comando(self, cmd):
        # saudacoes
        if cmd == "1":
            lista_saudacoes = ["O que quer aqui?", "Sai de perto!", "Não enche."]
            return choice(lista_saudacoes)
        
        # nome do bot
        elif cmd == "2":
            return choice(["Acho que é {} ou alguma coisa".format(self.nome), "Já não leu quando me escolheu?!", "{}. O que mais?".format(self.nome)])
        
        # dica
        elif cmd == "3":
            return choice(["Não tome cachaça.", "Melhor uma pedra no seu caminho do que duas nos rins, beba água.", "Mate 2 pedras com um pássaro só."])
        
        # adeus
        elif cmd == "4":
            return choice(["Até que enfim, sai daqui.", "Enfim livre disso!"])

        else:
            return "Como tudo na vida, eu não sei o que dizer..."

    # quando bot é escolhido
    def boas_vindas(self):
        return "\nSério? Eu? Pra que?\n"
    
    # chama a funcao despedida quando usa comando -1
    def despedida(self):
        return "Frase triste tchau, tamo junto, fim da jornada."