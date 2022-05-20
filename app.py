#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado
from Bots.BotEstudante import BotEstudante
###construa a lista de bots disponíveis aqui
lista_bots = [BotCansado("Forever Alone", {"1": "Saudação", "2": "Qual seu nome?", "3": "Quero uma dica", "4": "Adeus"}), BotEstudante("Estudante", {"1": "Cumprimentar", "2": "Qual seu nome?", "3": "O que tem de almoço no RU hoje?", "4": "Até mais"})]


sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
