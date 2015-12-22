# Dual Controller
import random
from view import *
from cards import *
from dualcards import *

class DualController(object):
    DEALER_NAME = "HY-CSE" #클래스 전체가 공유하는 속성.
    def __init__(self,name):
        self.player = DualPlayer(name)
        self.dealer = DualDealer(DualController.DEALER_NAME)
        self.deck = DualDeck()
        self.deck.fresh_deck()

        # self.length = Deck.check_length(self)


    def play(self):
        player = self.player
        dealer = self.dealer
        deck = self.deck
        # length = Deck.check_length(Deck)
        playertemp = []
        dealtemp = []

        ####To be continue HERE####


        deck.deal(player)
        deck.deal(dealer)

        random.shuffle(player.cards)
        random.shuffle(dealer.cards)
        ####플레이모드 설정 - 1 = 상대카드 없애기, 2 = 내 카드 없애기####
        print("Playmod 1 aims to delete all dealer's cards.")
        print("Playmod 2 aims to delete all player's cards.\n")
        playmod = Reader.playmod("Select play mod what you want to play. (1 or 2) : ")
        while (playmod.isdigit() != True) or ((playmod != "1") and (playmod != "2")):
            playmod = input("RESelect play mod what you want to play. (1 or 2) : ")

        ###Playmod 확인####
        if playmod == "1":
            print("You selected Playmod 1. Get rid of all dealer's cards. Good Luck!\n")
        else:
            print("You selected Playmod 2. Get rid of all your cards. Good Luck!\n")

        print(DualController.DEALER_NAME, ":", dealer.cards)
        print(player.name, ":", player.cards)
        while len(dealer.cards) != 0 and len(player.cards) != 0:

            selcard = input ("Select address number of cards to open (1~"+str(len(player.cards))+") :")
            while  (selcard.isdigit() == False) or (int(selcard) > len(player.cards)) or int(selcard) < 1:
                selcard = input ("Select proper address number to open (1~"+str(len(player.cards))+") : ")
            dealselcard = random.randrange(0,len(dealer.cards)+1)
            playertemp.append(player.cards[int(selcard)-1])
            dealtemp.append(dealer.cards[int(dealselcard)-1])

            print()
            print("Delaer's Card was = ", dealtemp[0]) #랜덤으로 뽑은 숫자에 해당하는카드
            print("Your choice was = ", playertemp[0],"\n") #플레이어가 고른 카드


            ###뽑은 카드 크기 비교하여 승패 판정/숫자가 큰 사람이 작은사람의 카드를 가져감/같은 카드의 경우 둘다 제거##
            if int(playertemp[0]) > int(dealtemp[0]):
                print("You get the dealer's card.")
                player.cards.append(dealtemp[0])
                dealer.cards.remove(dealtemp[0])
                random.shuffle(player.cards)
                random.shuffle(dealer.cards)
                playertemp = []
                dealtemp = []

            elif int(playertemp[0]) < int(dealtemp[0]):
                print("You lost the card.")
                dealer.cards.append(playertemp[0])
                player.cards.remove(playertemp[0])
                random.shuffle(player.cards)
                random.shuffle(dealer.cards)
                playertemp = []
                dealtemp = []

            elif int(playertemp[0]) == int(dealtemp[0]):
                print("We select same cards. You and Dealer lost the cards.")
                dealer.cards.remove(dealer.cards[int(dealselcard)-1])
                player.cards.remove(player.cards[int(selcard)-1])
                random.shuffle(player.cards)
                random.shuffle(dealer.cards)
                playertemp = []
                dealtemp = []

            ###뽑은 카드 보여줌###
            print(DualController.DEALER_NAME, ":", len(dealer.cards)," cards left.\n")
            print(player.name, ":", player.cards)


        ####게임종료 출력####
        if playmod == "1":
            if len(dealer.cards) == 0:
                dealer.bust()
                player.win()
            if len(player.cards) == 0:
                dealer.win()
                player.bust()

            if len(player.cards) == 0 and len(dealer.cards) == 0:
                print("We draw.")

        elif playmod == "2":
            if len(dealer.cards) == 0:
                dealer.win()
                player.lose()
            if len(player.cards) == 0:
                player.win()

            if len(player.cards) == 0 and len(dealer.cards) == 0:
                print("We draw.")
        ###보드 초기화###
        player.clear()
        dealer.clear()

def main():
    print('Welcome to Hanyang Casino!')
    name = input("Write your name here : ")


    game = DualController(name)

    while True:
        print("== New Round ==")
        game.play()
        if not Reader.ox("Play more? (o/x) :"):
            break
    print("Have a nice day. Good Luck!!")

main()