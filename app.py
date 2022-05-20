#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado
from Bots.BotPoliglota import BotPoliglota
from Bots.BotEstudante import BotEstudante

""" Criar cada bot em uma variável prórpia
    Cada um recebe um dicionário de comandos:
    Chave: código para o comando
    Valor: tupla na fora ("Nome do Comando", ("Resposta1", "Resposta2", ...))"""

botCansado = BotCansado("Forever Alone", {"1": ("Saudação", ("O que quer aqui?", "Sai de perto!", "Não enche.")),
                                          "2": ("Qual seu nome?", ("Acho que é Forever Alone ou alguma coisa", "Já não leu quando me escolheu?!", "Forever Alone. O que mais?")),
                                          "3": ("Quero uma dica", ("Não tome cachaça.", "Melhor uma pedra no seu caminho do que duas nos rins, beba água.", "Mate 2 pedras com um pássaro só.")),
                                          "4": ("Adeus", ("Até que enfim, sai daqui.", "Enfim livre disso!")),
                                          })
botEstudante = BotEstudante("Adilson", {"1": ("Saudação", ("Desculpa, não posso, tô atrasado pra aula", "Estudou pra prova hoje?")),
                                        "2": ("Qual seu nome?", ("Me chamo Adilson, só não me pergunta o meu número de matrícula que eu não vou lembrar", "Depois da aula de álgebra, nem eu lembro")),
                                        "3": ("O que tem no RU hoje?", ("Hoje não sei, mas a última vez que teve linguiça, eu mordi e ela me disse oink de tão crua que tava", "Não tenho nem tempo pra almoçar, preciso estudar pra prova", "Dor e desespero")),
                                        "4": ("Adeus", ("Até mais, vou fazer as listas de POO, tem mais umas cinco!", "Mais duas horas de ônibus até a Palhoça"))
                                        })
lista_bots = [botCansado, botEstudante]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
