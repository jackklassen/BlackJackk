import unittest

from src.deck import Deck


class DeckTest(unittest.TestCase):
   #make decks

    def setUp(self):
        self.deck1 = Deck(1)
        self.deck2 = Deck(2)
        self.deck3 = Deck(255)

    def test_build_deck(self):
        assert(len(self.deck1.deck) == 0)
        assert (len(self.deck2.deck) == 0)
        assert (len(self.deck3.deck) == 0)
        self.deck1.build_deck()
        self.deck2.build_deck()
        self.deck3.build_deck()
        assert (len(self.deck1.deck) == 52)
        assert (len(self.deck2.deck) == (52 * 2))
        assert (len(self.deck3.deck) == (52 * 255))


    def test_shuffle(self):
        #copy decks, call shuffle on them if they are the same it fails.
        #but also they should all be the same size.
        self.deck1.build_deck()
        deck_copy = list(self.deck1.deck)
        assert(deck_copy == self.deck1.deck)
        self.deck1.shuffle()
        assert(deck_copy != self.deck1.deck)



    def test_get_value(self):
        test_card_A = ["Hearts", "A"]
        test_card_2 = ["Hearts", "2"]
        test_card_K = ["Hearts", "K"]
        test_card_10 = ["Hearts", "10"]
        assert(self.deck1.get_value(test_card_A) == 11)
        assert(self.deck1.get_value(test_card_2) == 2)
        assert(self.deck1.get_value(test_card_K) == 10)
        assert(self.deck1.get_value(test_card_10) == 10)

    def test_deal_card(self):
        self.deck1.build_deck()
        pre_size = len(self.deck1.deck)
        self.deck1.deal_card()
        assert((pre_size - 1) == len(self.deck1.deck))
