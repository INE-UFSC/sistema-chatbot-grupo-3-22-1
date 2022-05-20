from Bots.Bot import Bot
from random import choice

class BotEstudante(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)

    # executada ao mostrar os bots disponiveis
    def apresentacao(self):
        return "Me salva! Tem CTS hoje"
   
    def executa_comando(self, cmd):
        # saudacoes
        if cmd == "1":
            lista_saudacoes = ["Desculpa, não posso, tô atrasado pra aula", "Estudou pra prova hoje?"]
            return choice(lista_saudacoes)
        
        # nome do bot
        elif cmd == "2":
            return choice(["Me chamo {}, só não me pergunta o meu número de matrícula que eu não vou lembrar".format(self.nome), "Depois da aula de álgebra, nem eu lembro"])
        
        # dica
        elif cmd == "3":
            return choice(["Hoje não sei, mas a última vez que teve linguiça, eu mordi e ela me disse oink de tão crua que tava", "Não tenho nem tempo pra almoçar, preciso estudar pra prova", "Dor e desespero"])
        
        # adeus
        elif cmd == "4":
            return choice(["Até mais, vou fazer as listas de POO, tem mais umas cinco!", "Mais duas horas de ônibus até a Palhoça"])

        else:
            return "Me desculpa, mas eu entendi o que tu quis dizer tanto quanto entendi a matéria de sistemas"

    # quando bot é escolhido
    def boas_vindas(self):
        return "Opa, só fala rápido que eu tenho que estudar pra cálculo"
    
    # chama a funcao despedida quando usa comando -1
    def despedida(self):
        return "Finalmente isso acabou, vou poder comer no RU"