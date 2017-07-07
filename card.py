# -*- coding: utf-8 -*-
# Check this out for cards display https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
# Create a Suit Class???
SUITS = {1: {'Suit': 'Clubs',
             'Symbol': '♣'},
         2:  {'Suit': 'Diamonds',
              'Symbol': '♦'},
         3:  {'Suit': 'Hearts',
              'Symbol': '♥'},
         4:  {'Suit': 'Spades',
              'Symbol': '♠'}}


class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
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
        return num_result + " of " + SUITS[self.suit]['Suit']

    # Override Operators <, <=, >, >=, ==, != will allow cards
    # to be compared ignoring the suit
    # TODO: check other to ensure it is type card and implement
    # alternate comparison if int or float it would look like:
    # def __le__(self, other):
    #     if isinstance(other, Card):
    #     return self.number <= other.number
    # elif isinstance(other, (int, float)):
    #     return self.number <= other
    # else:
    #     return NotImplemented

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number


class CardSet(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        out = ''
        for c in self.cards:
            out += str(c) + '\r\n'
        return out[:-1]

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
    def count(self):
        return len(self.cards)
