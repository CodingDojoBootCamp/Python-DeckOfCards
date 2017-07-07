from card import *
from deck import *
from player import *
from game import *


class War(CardGame):
    def __init__(self, players=[]):
        super(War, self).__init__('War', players)
        self.deck.shuffle()

    def deal(self):
        player_count = len(self.players)
        while self.deck.count > 0:
            self.players[self.deck.count %
                         player_count].add(self.deck.remove())

    def play(self):
        # can we make this support more than two players
        self.deal()
        while(self.players[0].count > 0 and self.players[0].count > 0):
            self.playRound()
            print str(self.players[0]) + ' ## ' + str(self.players[1])
        if self.players[0].count > self.players[1].count:
            print 'WINNER!!! - ' + self.players[0].name
        else:
            print 'WINNER!!! - ' + self.players[1].name

    def playRound(self, pot=[]):
        p1Card = self.players[0].remove()
        p2Card = self.players[1].remove()
        if p1Card == p2Card:
            pot = CardSet()
            pot.cards.extend([p1Card, p2Card])
            if self.players[0].count > 4 and self.players[1].count > 4:
                self.tieBreaker(pot)
            elif self.players[0].count < 4:
                self.players[1].cards.extend(pot.cards)
                while self.players[0].count > 0:
                    self.players[1].add(self.players[0].remove())
            elif self.players[1].count < 4:
                self.players[0].cards.extend(pot.cards)
                while self.players[1].count > 0:
                    self.players[0].add(self.players[1].remove())

        if p1Card > p2Card:
            # TODO make add support adding multiple cards
            self.players[0].add(p1Card).add(p2Card)
        else:
            self.players[1].add(p1Card).add(p2Card)

    def tieBreaker(self, pot):
        print 'WAR!!!!!'
        (pot.add(self.players[0].remove())
            .add(self.players[0].remove())
            .add(self.players[0].remove()))
        (pot.add(self.players[1].remove())
            .add(self.players[1].remove())
            .add(self.players[1].remove()))
        self.playRound(pot)


p1 = Player('Justin')
p2 = Player('Alisha')
g1 = War([p1, p2])

g1.play()
