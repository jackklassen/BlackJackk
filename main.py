#Basic little Blackjack program to shake the rust of my python skills.

#How does this work? oop? deck is object it holds used and to unused cards.
#I kinda want it to be able to count cards agianst.

from src import deck


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deck = deck.Deck(1)
    deck.build_deck()
    deck.shuffle()
    print_hi(deck.deal_card())


