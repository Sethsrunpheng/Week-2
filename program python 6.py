import random

def play_game():
    print("Let's play rock, paper, scissors!")
    print("Enter 'r' for rock, 'p' for paper, or 's' for scissors.")
    
    # Get user's choice
    user_choice = input(" Human ").lower()
    while user_choice not in ['r', 'p', 's']:
        user_choice = input("Invalid choice. Please try again: ").lower()

    # Generate computer's choice
    computer_choice = random.choice(['r', 'p', 's'])
    print(f"Computer {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("You lose.")

# Play the game
play_game()
