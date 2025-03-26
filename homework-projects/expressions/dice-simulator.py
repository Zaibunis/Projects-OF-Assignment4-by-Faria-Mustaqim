import random  # Import random module for dice rolling

def roll_dice():
    """Rolls two dice and prints their total."""
    die1 = random.randint(1, 6)  # Roll first die
    die2 = random.randint(1, 6)  # Roll second die
    print(f"Rolled: {die1} and {die2} (Total: {die1 + die2})")

def main():
    die1 = 10  # This variable is separate from the one inside roll_dice()
    print(f"die1 in main() starts as: {die1}")

    # Roll dice three times
    for _ in range(3):
        roll_dice()

    print(f"die1 in main() is still: {die1}")  # Shows variable scope

if __name__ == "__main__":
    main()
