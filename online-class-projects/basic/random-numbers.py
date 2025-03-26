import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(" ".join(map(str, numbers)))  # Print numbers space-separated

if __name__ == '__main__':
    main()
