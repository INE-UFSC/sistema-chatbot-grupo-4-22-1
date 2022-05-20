#encoding: utf-8
from Bots.BotPiada import BotPiada
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotSolitario import BotSolitario
from Bots.BotEspelhado import BotEspelhado
from Bots.BotCachorro import BotCachorro

# construa a lista de bots disponíveis aqui
lista_bots = [BotSolitario("Sozinho"), BotCachorro("Theo")]#, BotEspelhado("Mirror"), BotPiada("Roger")]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
