from card import CardSet


class Player(CardSet):
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name

    def __str__(self):
        return self.name + ' - ' + str(self.count)

    def displayCards(self):
        print self.name + '\r\n====================\r\n' + super(Player, self).__str__()
