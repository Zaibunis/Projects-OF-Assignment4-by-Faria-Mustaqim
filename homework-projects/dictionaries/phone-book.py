def main():
    phonebook = {}
    while True:
        name = input("Enter name: " )
        if name == "":
            break
        number = input("Enter phone number: ")
        phonebook[name] = number

        print("\nPhonebook:")      
        for name , number in phonebook.items():
            print(f"{name}: {number}")

if __name__ == '__main__':
    main()