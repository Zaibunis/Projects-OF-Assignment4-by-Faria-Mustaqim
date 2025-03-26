import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print("Random Numbers") 
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")
    print() 

if __name__ == '__main__':
    main()
