from deck import deck
from player import *
from deck import card


class CardGame(object):
    def __init__(self, name, players=[]):
        self.name = name
        self.players = players
        self.deck = deck.Deck()
