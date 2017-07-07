from random import shuffle


class CardSet(object):
    def __init__(self):
        self.cards = []

    def remove(self):
        return self.cards.pop()

    def add(self, card):
        self.cards.append(card)
        return self

    def displayCards(self):
        for c in self.cards:
            print c
        return self

    @property
    def total(self):
        return len(self.cards)


class Deck(CardSet):
    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for number in range(1, 14):
                self.cards.append(Card(suit, number))

    def shuffle(self):
        shuffle(self.cards)


class Player(CardSet):
    def __init__(self, cards=[]):
        self.cards = cards


class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        suit_result = ""
        if self.suit == 1:
            suit_result += "Spades"
        elif self.suit == 2:
            suit_result += "Hearts"
        elif self.suit == 3:
            suit_result += "Diamonds"
        elif self.suit == 4:
            suit_result += "Clubs"
        num_result = ""
        if self.number == 1:
            num_result += "Ace"
        elif self.number == 11:
            num_result += "Jack"
        elif self.number == 12:
            num_result += "Queen"
        elif self.number == 13:
            num_result += "King"
        else:
            num_result += str(self.number)
        return num_result + " of " + suit_result


d = Deck()
print len(d.cards)

c = Card(4, 6)
print c
