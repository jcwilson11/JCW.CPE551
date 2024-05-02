import random

class Card:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """Suit + Value are integers"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        return self.value < c2.value

    def __gt__(self, c2):
        return self.value > c2.value

    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"
class Deck:
    def __init__(self, card_count=52):
        full_deck = [Card(value, suit) for value in range(2, 15) for suit in range(4)]
        random.shuffle(full_deck)
        self.cards = full_deck[:card_count]  # Adjust deck size based on user input

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
    
d = Deck()
print(d)