def main():
    print("Double the list of number")
    numbers = [1, 2, 3, 4]
    doubled_numbers = [num * 2 for num in numbers]
    print(f"numbers = {doubled_numbers}")

if __name__ == '__main__':
    main()