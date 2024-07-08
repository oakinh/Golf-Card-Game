import unittest
from deck import Deck
from player import Player

class Tests(unittest.TestCase):
    def test_create_cards(self):
        deck = Deck()

        # Using a set for deduplication purposes
        deck_stringified = set()
        for card in deck.cards:
            deck_stringified.add(f"{card.value} {card.suit}")

        self.assertEqual(
            len(deck.cards),
            52
        )
        self.assertEqual(
            len(deck_stringified),
            52
        )


    def test_cards_dealt(self):
        deck = Deck()
        players = [Player(), Player(), Player(), Player()]
        deck.deal_cards(players)

        player_1_grid = players[0].grid
        player_1_cards = players[0].grid.cards
        for row in player_1_cards:
            for card in row:
                print(card.value, card.suit)

        correct_num_cards_in_deck = 52 - (len(players) * 9)

        self.assertEqual(
            player_1_grid.num_rows,
            len(player_1_cards)
        )
        self.assertEqual(
            player_1_grid.num_cols,
            len(player_1_cards[0])
        )
        self.assertEqual(
            len(deck.cards),
            correct_num_cards_in_deck
        )
        

    def test_cards_dealt_last_player(self):
        deck = Deck()
        players = [Player(), Player(), Player(), Player()]
        deck.deal_cards(players)

        last_player_grid = players[-1].grid
        last_player_cards = players[-1].grid.cards
        # for row in player_1_cards:
        #     for card in row:
                # print(card.value, card.suit)

        correct_num_cards_in_deck = 52 - (len(players) * 9)

        self.assertEqual(
            last_player_grid.num_rows,
            len(last_player_cards)
        )
        self.assertEqual(
            last_player_grid.num_cols,
            len(last_player_cards[-1])
        )
        self.assertEqual(
            len(deck.cards),
            correct_num_cards_in_deck
        )

    def test_cards_dealt_for_duplicates(self):
        deck = Deck()
        players = [Player(), Player(), Player(), Player()]
        deck.deal_cards(players)

        player_1_cards = players[0].grid.cards

        deck_stringified = set()
        for i in range(0, len(players)):
            for row in players[i].grid.cards:
                for card in row:
                    deck_stringified.add(f"{card.value} {card.suit}")

        correct_num_cards_in_grids = len(players) * 9
        
        self.assertEqual(
            correct_num_cards_in_grids,
            len(deck_stringified)
        )


if __name__ == "__main__":
    unittest.main()