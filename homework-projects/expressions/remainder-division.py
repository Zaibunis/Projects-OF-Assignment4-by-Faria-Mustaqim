def main():
    print("Division and Remainder Calculator")
    integer_1:float = float(input("Please enter an integer to be divided: "))
    integer_2:float = float(input("Please enter an integer to divide by: "))
    quotient: int = integer_1 // integer_2
    remainder: int = integer_1 % integer_2
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()