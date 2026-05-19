import random

BLACK_JACK = 21
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9","10", "K", "Q", "J"]
    deck = []
    deck_size = 1



    def __init__(self,deck_size):
        self.deck = []
        self.deck_size = deck_size


    def shuffle(self):
        random.shuffle(self.deck)

        #size = number of decks i.e. 1 = 1 deck, 2 = 2 decks etc
    def build_deck(self):
        #loop to build deck of tuples.
        #4 times for each suite, heart, spade, club, diamond, not needed for blackjack but is for good deck.
        #ace to king
        #both in enum loops, as tuples in deck.
        for i in range(self.deck_size):
            for suit in self.suits:
                for value in self.values:
                    self.deck.append((suit, value))

    #card is a tuple
    #remember A is whatever is better between 1 or 11.
    def get_value(self, card):
        if card[1] == "K" or card[1] == "Q" or card[1] == "J":
            return 10
        elif card[1] == "A":
            return 11
        else:
            return int(card[1])


    def count_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if self.get_value(card) == 11:
                aces += 1
            else:
                value += self.get_value(card)

        while aces > 0:
            if (value + 11) > BLACK_JACK:
                value += 1
            else:
                value += 11
        return value


    def deal_card(self):
        if(len(self.deck) > 0):
            return self.deck.pop()
        else:
            self.build_deck()
            self.shuffle()
            return self.deck.pop()
