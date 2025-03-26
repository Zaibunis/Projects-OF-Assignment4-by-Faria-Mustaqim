import random  # Import the random module for dice rolling

def roll_dice():
    """Rolls two dice and prints their values and total."""
    die1 = random.randint(1, 6)  # Roll first die (1 to 6)
    die2 = random.randint(1, 6)  # Roll second die (1 to 6)
    total = die1 + die2  # Calculate the total
    print(f"You rolled: {die1} and {die2} (Total: {total})")

def main():
    print("Rolling two dice... 🎲🎲")
    roll_dice()  # Call the function to roll dice

if __name__ == "__main__":
    main()
