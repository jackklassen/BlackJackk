import unittest

from src.deck import Deck


class DeckTest(unittest.TestCase):
   #make decks

    def setUp(self):
        deck1 = Deck(1)
        deck2 = Deck(2)
        deck3 = Deck(255)

    def test_build_deck(self):
        self.deck1.build_deck()
        self.deck2.build_deck()

    def test_shuffle(self):
        #copy decks, call shuffle on them if they are the same it fails.
        #but also they should all be the same size.
        pass


    def test_get_value(self):
        pass

    def test_deal_card(self):
        #deal card, check its value, then see if deck went down in size.
        pass
