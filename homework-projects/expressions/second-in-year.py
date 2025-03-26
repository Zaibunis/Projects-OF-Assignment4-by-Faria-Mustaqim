DAYS = 365
HOURS = 24
MINUTES = 60
SECONDS = 60

def main():
    print("Seconds in a Year Calculator")
    total_seconds = DAYS * HOURS* MINUTES* SECONDS
    print(f"There are {total_seconds:.2f} seconds in a year!")

if __name__ == '__main__':
    main()