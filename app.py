#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado
from Bots.BotEstudante import BotEstudante
###construa a lista de bots disponíveis aqui
lista_bots = [BotCansado("Forever Alone", {"1": "Saudação", "2": "Qual seu nome?", "3": "Quero uma dica", "4": "Adeus", "5": "Algo"})]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
