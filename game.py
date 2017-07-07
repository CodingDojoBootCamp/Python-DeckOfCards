from deck import *
from player import *
from card import *


class CardGame(object):
    def __init__(self, name, players=[]):
        self.name = name
        self.players = players
        self.deck = Deck()
