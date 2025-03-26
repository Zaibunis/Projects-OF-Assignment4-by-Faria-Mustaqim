def main():
    values = []
    values = []  # Initialize an empty list

    while True:
        user_input = input("Enter a value: ")
        if user_input == "":  # Stop when the user presses Enter without typing anything
            break
        values.append(user_input)  # Add input to the list

    print("\nHere's the list:", values)
   

if __name__ == '__main__':
    main()