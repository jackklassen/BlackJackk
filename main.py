#Basic little Blackjack program to shake the rust of my python skills.

from src.game import Game


def main():
    game = Game(1)
    game.game_loop()

# Using the special variable
# __name__
if __name__=="__main__":
    main()

