'''
This is a simple card game called War. The game is played between two players, Player and Computer. The deck is shuffled and divided equally between the two players. Each player draws a card from the top of their deck and the player with the higher card wins the round. The winner takes both cards and adds them to the bottom of their deck. If the cards drawn are of equal rank, a war is declared. In a war, each player draws three cards from their deck and the player with the higher fourth card wins all the cards in play. If a player does not have enough cards to continue a war, the other player wins the game. The game continues until one player has all the cards or the player quits the game.
'''

import random

class Card:  # used to create a card object to represent a single card
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_list = ["None", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  # Ace is the highest

    def __init__(self, suit=0, rank=2): 
        self.suit = suit
        self.rank = rank

    def __str__(self): # Print the card
        return f"{self.rank_list[self.rank]} of {self.suit_list[self.suit]}"

    def __eq__(self, other): # Check if two cards are equal
        return self.rank == other.rank

    def __gt__(self, other): 
        return self.rank > other.rank  # Comparison based on the index in rank_list

class Deck:  # used to create a deck of cards
    def __init__(self): # Initialize the deck with 52 cards
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):  # rank 1 is '2' and 13 is 'Ace'
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def rm_card(self): # Remove a card from the deck
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player: # used to create a player object
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wins = 0

class Game:  # Main game class
    def __init__(self, card_count=52):  # Initialize the game
        deck = Deck()
        self.p1 = Player("Player")
        self.p2 = Player("Computer")
        self.deal_cards(deck, card_count)
        self.turn_count = 0

    def deal_cards(self, deck, card_count):  # Deal half the deck to each player
        deck.cards = deck.cards[:card_count]
        self.p1.hand = deck.cards[:len(deck.cards)//2]
        self.p2.hand = deck.cards[len(deck.cards)//2:]

    def wins(self, winner, cards):  # Award the cards to the winner
        print(f"{winner.name} wins this battle!")
        winner.hand.extend(cards)
        self.print_card_count()  # Show card counts after each round

    def war(self, cards_in_play):  # Handle a war
        if len(self.p1.hand) < 4 or len(self.p2.hand) < 4:
            loser = self.p1 if len(self.p1.hand) < 4 else self.p2
            self.conclude_game_due_to_war(loser)
            return loser
        for _ in range(3):
            cards_in_play.extend([self.p1.hand.pop(0), self.p2.hand.pop(0)])
        face_up_p1 = self.p1.hand.pop(0)
        face_up_p2 = self.p2.hand.pop(0)
        cards_in_play.extend([face_up_p1, face_up_p2])
        self.draw(self.p1.name, face_up_p1, self.p2.name, face_up_p2)
        if face_up_p1 == face_up_p2:
            print("WAR again!")
            self.war(cards_in_play)
        elif face_up_p1 > face_up_p2:
            self.wins(self.p1, cards_in_play)
        else:
            self.wins(self.p2, cards_in_play)

    def draw(self, p1n, p1c, p2n, p2c):  # Print the cards drawn
        print(f"\n{p1n} draws {p1c}, {p2n} draws {p2c}")

    def play_game(self):  # Game instructions
        while self.p1.hand and self.p2.hand:
            response = input("\nPress any key to play or 'q' to quit: ")
            if response.lower() == 'q':
                self.end_game()
                return
            p1c = self.p1.hand.pop(0)
            p2c = self.p2.hand.pop(0)
            self.turn_count += 1
            self.draw(self.p1.name, p1c, self.p2.name, p2c)
            if p1c == p2c:
                print("\nWAR!")
                if self.war([p1c, p2c]) is not None:
                    break
            elif p1c > p2c:
                self.wins(self.p1, [p1c, p2c])
            else:
                self.wins(self.p2, [p1c, p2c])

    def print_card_count(self):  # Print the number of cards each player has
        print(f"Player has {len(self.p1.hand)} cards, Computer has {len(self.p2.hand)} cards.")

    def conclude_game_due_to_war(self, loser):  # End the game if a player does not have enough cards to continue a war
        print(f"{loser.name} does not have enough cards to continue the war and loses.")
        self.end_game()

    def end_game(self):  # End the game
        print(f"\nTotal turns played: {self.turn_count}")
        if len(self.p1.hand) > len(self.p2.hand):
            print(f"\n{self.p1.name} wins the game!")
        elif len(self.p1.hand) < len(self.p2.hand):
            print(f"\n{self.p2.name} wins the game!")
        else:
            print(f"\nIt's a tie!")

def main():  # Main function to start the game
    card_count = 52  # Default to 52 cards without user input
    game = Game(card_count)
    game.play_game()


if __name__ == "__main__":
    main()
