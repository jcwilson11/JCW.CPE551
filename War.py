'''
This is a simple card game called War. The game is played between two players, Player and Computer. The deck is shuffled and divided equally between the two players. Each player draws a card from the top of their deck and the player with the higher card wins the round. The winner takes both cards and adds them to the bottom of their deck. If the cards drawn are of equal rank, a war is declared. In a war, each player draws three cards from their deck and the player with the higher fourth card wins all the cards in play. If a player does not have enough cards to continue a war, the other player wins the game. The game continues until one player has all the cards or the player quits the game.
'''

import random

class Card:  # used to create a card object to represent a single card
    suit_list = ["♣", "♦", "♥", "♠"] # Unique Feature: Unicode symbols for suits instead of full names, this allows for better alignment in the card drawing function using ASCII art
    rank_list = ["None", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # Ace is the highest

    def __init__(self, suit=0, rank=2): 
        self.suit = suit
        self.rank = rank

    def __str__(self): # Print the card as a string
        return f"{self.rank_list[self.rank]}{self.suit_list[self.suit]}"

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

def draw_card(face, suit):
    # Unique Feature: Print the suite in red or black color for better visibility
    red = "\033[31m"
    black = "\033[37m"
    reset = "\033[0m"
    suit_color = red if suit in ['♥', '♦'] else black
    
    # Generate a string representation of a card using ASCII art
    if face == "10":  # Special case for '10' since it's two characters
        return f"+-----+\n" \
               f"|{face}{suit_color}{suit}{reset}  |\n" \
               f"|     |\n" \
               f"|  {face}{suit_color}{suit}{reset}|\n" \
               f"+-----+"
    else:  # For all other card ranks
        return f"+-----+\n" \
               f"|{face}{suit_color}{suit}{reset}   |\n" \
               f"|     |\n" \
               f"|   {face}{suit_color}{suit}{reset}|\n" \
               f"+-----+"
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

    def draw(self, p1n, p1c, p2n, p2c):  # Unique Feaure: Print the cards drawn using ASCII
        p1_face, p1_suit = p1c.rank_list[p1c.rank], p1c.suit_list[p1c.suit]
        p2_face, p2_suit = p2c.rank_list[p2c.rank], p2c.suit_list[p2c.suit]
        p1_card_drawn = draw_card(p1_face, p1_suit)
        p2_card_drawn = draw_card(p2_face, p2_suit)
        print(f"\n{p1n} draws     {p2n} draws:")
        p1_lines = p1_card_drawn.split('\n')
        p2_lines = p2_card_drawn.split('\n')
        
        # Display the cards side by side with adjusted spacing
        for p1_line, p2_line in zip(p1_lines, p2_lines): # Align cards horizontally; zip the lines of the two cards together
            print(f"{p1_line}{10 * ' '}{p2_line}") # Adjust spacing between cards here

    def play_game(self):  # Game instructions
        while self.p1.hand and self.p2.hand: # Continue playing until one player runs out of cards
            response = input("\nPress any key to play or 'q' to quit: ")
            if response.lower() == 'q':
                self.end_game()
                return
            # Draw a card from each player's deck
            p1c = self.p1.hand.pop(0) 
            p2c = self.p2.hand.pop(0)
            self.turn_count += 1 #  Unique Feature: Keep track of the number of turns played
            self.draw(self.p1.name, p1c, self.p2.name, p2c) # Print the cards drawn using ASCII
            if p1c == p2c: 
                print("\nWAR!") # If the cards drawn are equal, a war is declared
                if self.war([p1c, p2c]) is not None:
                    break
            # Award the cards to the player with the higher card
            elif p1c > p2c: 
                self.wins(self.p1, [p1c, p2c])
            else: 
                self.wins(self.p2, [p1c, p2c])

            # Check if either player has run out of cards
            if len(self.p1.hand) == 0 or len(self.p2.hand) == 0:
                self.end_game()
                return

    def print_card_count(self):  # Print the number of cards each player has
        print(f"Player has {len(self.p1.hand)} cards, Computer has {len(self.p2.hand)} cards.") # rint the number of cards each player has

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
    card_count = 52  
    game = Game(card_count)
    print("Welcome to War!")
    print("The game is played between two players, Player and Computer. Each player draws a card from the top of their deck and the player with the higher card wins the round. If the cards drawn are of equal rank, a war is declared. Three cards are placed face down, and the fourth one is placed face up. The player with the higher card takes all the cards. The game continues until one player has all the cards or the player quits the game.")
    game.play_game()

if __name__ == "__main__": # Run the game
    main()
