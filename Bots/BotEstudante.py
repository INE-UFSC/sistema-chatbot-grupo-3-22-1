from Bot import Bot
from random import choice


class BotEstudante(Bot):
    # executada ao mostrar os bots disponiveis
    def apresentacao(self):
        return "Me salva! Tem CTS hoje"

    def executa_comando(self, cmd):
        if cmd in self.comandos.keys():
            resposta = choice(self.comandos[cmd][1])
            return resposta
        else:
            return "Me desculpa, mas eu entendi o que tu quis dizer tanto quanto entendi a matéria de sistemas"

    # quando bot é escolhido
    def boas_vindas(self):
        return "Opa, só fala rápido que eu tenho que estudar pra cálculo"

    # chama a funcao despedida quando usa comando -1
    def despedida(self):
        return "Finalmente isso acabou, vou poder comer no RU"
