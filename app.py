#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotSolitario import BotSolitario
from Bots.BotEspelhado import BotEspelhado

# construa a lista de bots disponíveis aqui
lista_bots = [BotSolitario("Sozinho"), BotEspelhado("Mirror")]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
