#Basic little Blackjack program to shake the rust of my python skills.

#How does this work? oop? deck is object it holds used and to unused cards.
#I kinda want it to be able to count cards agianst.


from src.game import Game


def main():
    game = Game(1)
    game.game_loop()

# Using the special variable
# __name__
if __name__=="__main__":
    main()

