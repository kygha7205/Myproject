#Playing Cards for Dual
import random
import cards
from cards import *




class DualCard(Card):

    @property
    def value(self):
        v = DualCard.CARDS.index(self.rank) + 1


class DualDeck(Deck):
    def __init__(self):
        super(DualDeck, self).__init__()
        self.cards = []
    def fresh_deck(self):
        for s in DualCard.CARDS:
            self.cards.append(s)
        random.shuffle(self.cards)


class DualHand(cards.Hand):
    def __init__(self,name):
        super(DualHand,self).__init__()
        self.name = name



class DualPlayer(DualHand):
    def __int__(self,name):
        super(DualPlayer,self).__init__(name)


    def bust(self):    ####카드를 모두 잃었을때.######
        print(self.name,"busts.")
        self.lose()


    def lose(self):
        print(self.name,"loses.")
        print("Dealer : Don't worry. I hope you to win next Game.")

    def win(self):
        print(self.name,"wins.")
        print("Congratulation!!")



class DualDealer(DualHand):
    ######hit??????#######
    def win(self):
        print("Dealer wins.")


    def bust(self):     #####카드를 모두 잃었을때########
        print("Dealer lost all cards.")
        print(self.name,"busts.")


















