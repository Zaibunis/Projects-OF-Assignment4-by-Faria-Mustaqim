def main():
    print("Double Until 100")
    curr_value  = int(input("Enter your Number: "))
    while curr_value < 100:
        curr_value = curr_value*2 # Double the value
        print(curr_value, end=" ")  # Print result on the same line

if __name__ == '__main__':
    main()