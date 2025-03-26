def main():
    print()
    print("Prints Fibonacci sequence up to a maximum value of 10,000.")
    print()
    MAX_VALUE = 10000  # Set the maximum value for Fibonacci sequence
    a, b = 0, 1  # First two terms

    while a < MAX_VALUE:
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update values for the next iteration 1,0+1

if __name__ == '__main__':
    main()
