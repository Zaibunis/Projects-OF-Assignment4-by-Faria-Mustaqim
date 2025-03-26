def main():
    print("Lists")
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruit_list))# Print the length of the list.
    fruit_list.append('mango')# Add 'mango' at the end of the list. 
    # Print the updated list.
    for fruit in fruit_list:
     print(fruit)
    print(fruit_list)
     
if __name__ == "__main__":
    main()

def access_element(lst, index):
    """Returns the element at the specified index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Error: Index out of range."

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with a new value if valid."""
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Modified: {old_value} → {new_value}\nUpdated list: {lst}"
    else:
        return "Error: Index out of range."

def slice_list(lst, start, end):
    """Returns a sliced portion of the list while handling out-of-range cases."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return f"Sliced list: {lst[start:end]}"
    else:
        return "Error: Invalid slice indices."

def main():
    # Initialize the list
    my_list = ["apple", "banana", "cherry", "kiwi", "blackberry"]

    while True:
        print("\nINDEX GAME: Choose an operation")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter an index: "))
            print(access_element(my_list, index))

        elif choice == "2":
            index = int(input("Enter an index: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
