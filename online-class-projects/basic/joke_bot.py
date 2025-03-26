PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Why do programmers prefer dark mode? Because light attracts bugs! 😆"
SORRY: str = "Sorry, I only tell jokes."

def main():

    user_input = input(PROMPT)  # Ask for user input
    user_input = user_input.strip().lower()  # Now process it
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
