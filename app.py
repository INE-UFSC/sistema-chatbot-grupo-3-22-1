#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado
<<<<<<< HEAD
from Bots.BotPoliglota import BotPoliglota

=======
from Bots.BotEstudante import BotEstudante
>>>>>>> 5c31395d8a7793d0e912b76c20df787b71164b72
###construa a lista de bots disponíveis aqui
botCansado = BotCansado("Forever Alone", {"1": ("Saudação", ("O que quer aqui?", "Sai de perto!", "Não enche.")), 
                                          "2": ("Qual seu nome?", ("Acho que é Forever Alone ou alguma coisa", "Já não leu quando me escolheu?!", "Forever Alone. O que mais?")), 
                                          "3": ("Quero uma dica", ("Não tome cachaça.", "Melhor uma pedra no seu caminho do que duas nos rins, beba água.", "Mate 2 pedras com um pássaro só.")), 
                                          "4": ("Adeus", ("Até que enfim, sai daqui.", "Enfim livre disso!")),
                                         })
lista_bots = [botCansado]

# botPoliglota = BotPoliglota("")

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
