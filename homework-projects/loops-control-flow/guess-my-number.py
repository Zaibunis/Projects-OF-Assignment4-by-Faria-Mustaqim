import random

def main():
    """A simple number guessing game."""
    computer_number = random.randint(0, 99)  # Generate a random number between 0 and 99

    print("Guess My Number")
    print("I am thinking of a number between 0 and 99... ")

    guess = int(input("Enter a guess: "))  # Convert input to integer

    while guess != computer_number:
        if guess < computer_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print()

        guess = int(input("Enter a new guess: "))  # Convert input to integer

    print(f"Congrats! The number was {computer_number}")  # Print success message

if __name__ == '__main__':
    main()
