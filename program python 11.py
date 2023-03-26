import random

options = ["rock", "paper", "scissors"]

while True:
    # Get computer's choice
    computer_choice = random.choice(options)
    
    # Get user's choice
    user_choice = input("Choose rock, paper, or scissors: ")
    while user_choice not in options:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ")
    
    # Determine winner
    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    
    # Ask if user wants to play again
    play_again = input("Play again? (y/n): ")
    while play_again.lower() not in ["y", "n"]:
        play_again = input("Invalid choice. Please enter 'y' or 'n': ")
    if play_again.lower() == "n":
        break

print("Thanks for playing!")

