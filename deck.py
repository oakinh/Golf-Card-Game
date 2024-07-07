import Card from card

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # 0 = King
        # 11 = Jack
        # 12 = Queen
