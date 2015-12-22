# Dual cards

class Card(object):
    CARDS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    def __init__(self, rank, face_up=True):
        if rank in Card.CARDS:
            self.rank = rank
        else:
            print("Error: Not a right Rank or jokers")



class Hand(object):
    def __init__(self):
        self.cards = []


    def clear(self):
        self.cards = []

    def add(self, card):
        for _ in range(len(card)):
            self.cards.append(card[_])

    def give(self, card, hand):
        # self.cards.remove(card)
        hand.add(card)




class Deck(Hand):
    def __init__(self):
        super(Hand, self).__init__()

    def fresh_deck(self):
        cards = []
        return cards

    def deal(self, hand):
        if len(self.cards) < 0:
            d = self.fresh_deck()
            self.cards += d
        # for _ in range(how_many):
        self.give(self.cards, hand)