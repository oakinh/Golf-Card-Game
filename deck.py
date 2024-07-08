from card import Card
from grid import Grid
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # 0 = King
        # 11 = Jack
        # 12 = Queen
        self.create_cards()

    def create_cards(self):
        for suit in self.suits:
            for value in self.values:
                new_card = Card(value, suit)
                self.cards.append(new_card)

    def deal_cards(self, players):
        for player in players:
            player.grid = Grid()
            for i in range(0, player.grid.num_rows):
                row = []
                for i in range(0, player.grid.num_cols):
                    card_to_deal = random.choice(self.cards)
                    row.append(card_to_deal)
                    self.cards.remove(card_to_deal)
                player.grid.cards.append(row)

