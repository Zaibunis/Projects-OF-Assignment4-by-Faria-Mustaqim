def main():
    counts = {}  # Dictionary to store number counts

    while True:
        num = input("Enter a number: ")  # User input
        if num == "":  
            break
        num = int(num)  # Convert input to integer

        # Update count in dictionary
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Print results
    for number, count in counts.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
