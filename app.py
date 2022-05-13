#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotEspelhado import BotEspelhado

# construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotEspelhado("Mirror")]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
