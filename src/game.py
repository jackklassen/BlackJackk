from src import deck
#disperate game logic goes here, UI goes somewhere else.
class Game:
    #TODO need a dealer hand, a player hand and basic function in a loop
    #TODO need to better handle ace, check against the current value to see what the next ace should be considred at.
    #can't just declaire deck to be nothing, must either begin by making it or declair it global later with keyword

    def __init__(self, deck_size):
        self.dealer_hand_value = 0
        self.player_hand_value = 0
        self.deck = deck.Deck(deck_size)
        self.deck.shuffle()
        self.dealer_hand = []
        self.dealer_hand_value = 0
        self.player_hand = []
        self.player_hand_value = 0

    #draw 2 cards
    #Remember the dealer has a card they don't know so on deal 1 card is counted other is not.
    def deal_dealer(self):
        self.dealer_hand.clear()
        self.dealer_hand_value = 0
        visable_card = self.deck.deal_card()
        self.dealer_hand.append(visable_card)
        self.dealer_hand_value += self.deck.get_value(self.dealer_hand[0])

        self.dealer_hand.append(self.deck.deal_card())

        if self.dealer_hand_value + self.deck.get_value(self.dealer_hand[1]) >= 21:
            return -1 #for dealer goes bust

    def reveal_dealer(self):
        self.dealer_hand_value += self.deck.get_value(self.dealer_hand[1])

    #draw 2 cards
    #should really isolate logic for adding an ace.
    def deal_player(self):
        self.player_hand_value = 0
        self.player_hand.clear()

        self.player_hand.append(self.deck.deal_card())
        self.player_hand_value += self.deck.get_value(self.player_hand[0])

        self.player_hand.append(self.deck.deal_card())
        if self.deck.get_value(self.player_hand[1]) == 11:
            if self.player_hand_value + 11 > 21:
                self.player_hand_value += 1
            else:
                self.player_hand_value += 11
        else:
            self.player_hand_value += self.deck.get_value(self.player_hand[1])





    #adding a card to player or dealer can really just be 1 function based on parameters.
    #pull a new card from deck, check if player is bust and main loop should let player make next move
    def hit_player(self):
        newcard = self.deck.deal_card()
        self.player_hand.append(newcard)
        self.player_hand_value += self.deck.get_value(newcard)
        return self.player_hand_value

    def hit_dealer(self):
        pass


    def check_bust(self, value):
        if value > 21:
            return True
        return False


