
from random import shuffle
from card import *


class Deck(CardSet):
    def __init__(self):
        super(Deck, self).__init__()
        for suit in range(1, 5):
            for number in range(1, 14):
                self.add(Card(suit, number))

    def shuffle(self):
        shuffle(self.cards)
        return self
