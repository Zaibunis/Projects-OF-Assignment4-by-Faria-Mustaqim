def main():
    print("Leap Year")
    year: int = int(input("Enter a year: "))
    if year % 4:
        if year % 100:
            if year % 400:
                print(year, "That's a leap year.!")
            else:
                print(year, "That's not a leap year.")
        else:
            print(year, "That's not a leap year.")
    else:
        print(year, "That's not a leap year.")

if __name__ == '__main__':
    main()