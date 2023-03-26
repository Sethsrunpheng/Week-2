import random

while True:
    number = random.randint(1, 10)
    guess = 0

    print("Guess a number between 1 and 10:")

    while guess != number:
        guess = int(input())

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the number.")
            play_again = input("Would you like to play again? (y/n)").lower()
            if play_again == 'y':
                break
            else:
                print("Thanks for playing! Goodbye!")
                exit()
