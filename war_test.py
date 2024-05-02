def draw_card(face, suit):
    # Generate a string representation of a card using ASCII art
    return f"+-----+\n" \
           f"|{face:<2}{suit}  |\n" \
           f"|     |\n" \
           f"|  {face:>2}{suit}|\n" \
           f"+-----+"

def print_battlefield(player_card, computer_card, player_count, computer_count, last_winner, last_player_card, last_computer_card):
    # Clear the screen for readability
    print("\033[H\033[J", end="")  # This is the ANSI escape code to clear the screen, works in most terminals
    player_face, player_suit = player_card
    computer_face, computer_suit = computer_card
    last_player_face, last_player_suit = last_player_card
    last_computer_face, last_computer_suit = last_computer_card
    
    player_card_drawn = draw_card(player_face, player_suit)
    computer_card_drawn = draw_card(computer_face, computer_suit)
    
    # Align cards horizontally
    print("Player" + "   " * (len(player_card_drawn.split('\n')[0]) - 6) + "Computer")
    for p_line, c_line in zip(player_card_drawn.split('\n'), computer_card_drawn.split('\n')):
        print(p_line + "   " + c_line)  # Adjust spacing between cards here

    print("\n" + " " * 7 + "VS\n")
    print("+--------------------------------------------------+")
    print("|                     Result:                      |")
    print(f"| Player drew {last_player_face}{last_player_suit}         Computer drew {last_computer_face}{last_computer_suit}          |")
    print(f"| {last_winner} won the battle!                           |")
    print(f"| Player's cards: {player_count}     Computer's cards: {computer_count}      |")
    print("+--------------------------------------------------+")
    print("\nPress any key to play or 'q' to quit:")

# Example usage
player_card = ('10', '♠')
computer_card = ('J', '♥')
player_count = 26
computer_count = 24
last_winner = 'Player'
last_player_card = ('K', '♣')
last_computer_card = ('6', '♠')

print_battlefield(player_card, computer_card, player_count, computer_count, last_winner, last_player_card, last_computer_card)

input()  # Wait for user input
