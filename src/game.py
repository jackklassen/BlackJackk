class Game:
    #TODO need a dealer hand, a player hand and basic function in a loop


    dealer_hand = []
    dealer_hand_value = 0

    player_hand = []
    player_hand_value = 0

    def __init__(self):
        dealer_hand_value = 0
        player_hand_value = 0

    #draw 2 cards
    #Remember the dealer has a card they don't know so on deal 1 card is counted other is not.
    def deal_dealer(self):


    #draw 2 cards
    def deal_player(self):
        pass


    #pull a new card from deck, check if player is bust and main loop should let player make next move
    def hit_player(self):
        pass

    def hit_dealer(self):
        pass

    def check_bust(self, value):
        if value > 21:
            return True
        return False


