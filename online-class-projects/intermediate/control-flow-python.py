import random

NUM_ROUNDS = 5  # Total rounds

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0  #  Initialize score inside the function

    for round_num in range(1, NUM_ROUNDS + 1):  #  Loop for multiple rounds
        print(f"Round {round_num}")

        num = int(input("Enter your number: "))
        print(f"Your number is {num}")

        computer_num = random.randint(1, 100)  #  Generate computer's number

        user_input = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        if (user_input == "higher" and num < computer_num) or (user_input == "lower" and num > computer_num):
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1  #  Increase score on correct guess
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now: {your_score}")  #  Show score after each round
        print()

    print("Game Over!")
    print(f"Your final score: {your_score}")  #  Show final score

    if your_score == NUM_ROUNDS:
        print("Outstanding! You guessed perfectly in every round! 🎉")
    elif your_score > NUM_ROUNDS // 2:
        print("Great effort! You did really well! 😊")
    else:
        print("Don't worry! Keep practicing, and you'll get better! 👍")


if __name__ == "__main__":
    main()
