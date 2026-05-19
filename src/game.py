from src import deck

# game logic goes here, UI goes somewhere else.

BLACK_JACK = 21
class Game:

    def __init__(self, deck_size):
        self.dealer_hand_value = 0
        self.deck = deck.Deck(deck_size)
        self.deck.shuffle()
        self.dealer_hand = []
        self.player_hand_value = 0
        self.player_hand = []

    #draw 2 cards
    #Remember the dealer has a card they don't know so on deal 1 card is counted other is not.
    def deal_dealer(self):
        self.dealer_hand.clear()
        self.dealer_hand_value = 0
        visable_card = self.deck.deal_card()
        self.dealer_hand.append(visable_card)
        self.dealer_hand_value += self.deck.get_value(self.dealer_hand[0])

        self.dealer_hand.append(self.deck.deal_card())



    def reveal_dealer(self):
        self.dealer_hand_value += self.deck.get_value(self.dealer_hand[1])

    #draw 2 cards
    #should really isolate logic for adding an ace.
    def deal_player(self):
        self.player_hand.clear()

        self.player_hand.append(self.deck.deal_card())
        self.player_hand_value += self.deck.get_value(self.player_hand[0])

        self.player_hand.append(self.deck.deal_card())

    #adding a card to player or dealer can really just be 1 function based on parameters.
    #pull a new card from deck, check if player is bust and main loop should let player make next move
    def hit_player(self):
        newcard = self.deck.deal_card()
        self.player_hand.append(newcard)
        self.player_hand_value = self.deck.count_value(self.player_hand)
        return self.player_hand_value


    def hit_dealer(self):
        newcard = self.deck.deal_card()
        self.dealer_hand.append(newcard)
        self.dealer_hand_value = self.deck.count_value(self.dealer_hand)
        return self.dealer_hand_value


    def check_bust(self, value):
        if value > 21:
            return True
        return False


    def game_loop(self):
        # while game is being, played (i.e. didn't type q)
        # (later ask for deal in)
        # deal player hand
        # ask then for hit or stand (later double and split)
        # simple loop just keep allowing hit until user hits stand.
        # then call dealer_hit_loop, which reveals card and either stops there or hits until 17 or 21
        print("Welcome to the blackjack table")

        quit = False
        while not quit:

            print("What is your bid?")
            bid = input()
            print(f"Your bid is {bid} ")
            self.clear_all()
            self.deal_dealer()
            self.deal_player()
            hand_done = False
            while not hand_done:
                if self.player_hand_value > BLACK_JACK:
                    hand_done = True
                    break
                print("Dealer has ")
                print(self.dealer_hand[0])
                print("You have ")
                print(self.player_hand)
                print("Enter h for Hit, s for Stand, CTRL-C for QUIT")
                usr_input = input()
                if self.handle_input(usr_input) == 0:
                    hand_done = True


            if self.player_hand_value > BLACK_JACK:
                print("You lost!")
            elif self.player_hand_value == BLACK_JACK:
                print("You won!")

    def clear_all(self):
        self.player_hand_value = 0
        self.player_hand = []
        self.dealer_hand =  []
        self.dealer_hand_value = 0

    def handle_input(self, input):
        cln_input = self.clean_input(input)

        if cln_input == "h":
            self.hit_player()
            return 1
        elif cln_input == "s":
            self.dealer_hit_loop()
        return 0

    def dealer_hit_loop(self):
        # call reveal dealer, and loop, while 21 or 17 is not value hit dealer.

        # when 21 or 17 (or over on dealer side) is not hit just compare value of dealer and player, higher wins.
        while self.dealer_hand_value <= 17:
            self.hit_dealer()
            #print(self.dealer_hand_value)
            print("Dealer has ")
            print(self.dealer_hand)
            print("you have ")
            print(self.player_hand)

        if self.dealer_hand_value > BLACK_JACK:
            print("You Won!")

        elif self.player_hand_value > self.dealer_hand_value:
            print("You won!")
        else:
            print("You lost!")

        return 0

    def shuffle_ui(self):
        # shuffle game
        # print("Shuffled the deck \n")
        self.games_between_shuffle = 0

        # cleans input into either a valid input or else returns -1 if it recived an invalid input.

    def clean_input(self, input):
        if isinstance(input, str):
            cleaned_input = input[0]
            cleaned_input = cleaned_input.lower()
            return cleaned_input
        return -1
