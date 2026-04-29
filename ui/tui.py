class TUI:
    MAX_GAMES_BETWEEN_SHUFFLE = 2 # when games between shuffle hits this constant shuffle and tell the user it happened.
    def __init__(self):
        self.games_between_shuffle = 0
        pass

    def intro(self):
        #intro text, type number of decks default 1
        print("Welcome to the blackjack table, how many decks do you want to play with? default is 1")

        number_of_decks = int(input())
        if isinstance(number_of_decks,int):
            self.game = self.game.Game(number_of_decks)
        else:
            self.game = self.game.Game(1)
        self.game_loop()

    def game_loop(self):
        #while game is being, played (i.e. didn't type q)
        #(later ask for deal in)
        #deal player hand
        #ask then for hit or stand (later double and split)
        #simple loop just keep allowing hit until user hits stand.
        #then call dealer_hit_loop, which reveals card and eithr stops there or hits until 17 or 21
        pass

    def handle_input(self,input):
        pass

    def dealer_hit_loop(self):
        #call reveal dealer, and loop, while 21 or 17 is not value hit dealer.
        pass

    def shuffle_ui(self):
        #shuffle game
        #print("Shuffled the deck \n")
        self.games_between_shuffle = 0


    #cleans input into either a valid input or else returns -1 if it recived an invalid input.
    def clean_input(self,input):
        if isinstance(input,str):
            cleaned_input = input[0]
            cleaned_input = cleaned_input.lower()
            return cleaned_input
        return -1