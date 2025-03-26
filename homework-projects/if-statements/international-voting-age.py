def main():
    print("International Voting Age")
    age = int(input("How old are you? "))  # No need to specify `:int`

    if age >= 16:
        print("You are eligible to vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You are eligible to vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print("You are eligible to vote in Mayengua where the voting age is 48.")

    if age < 25:
        print("You are not eligible to vote in Stanlau where the voting age is 25.")

    if age < 48:
        print("You are not eligible to vote in Mayengua where the voting age is 48.")

if __name__ == '__main__':
    main()
