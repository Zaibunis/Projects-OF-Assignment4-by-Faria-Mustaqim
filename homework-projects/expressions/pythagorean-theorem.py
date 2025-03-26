import math

def main():
    print("Pythagorean Theorem")
    length:float = float(input("Enter the length of AB: "))
    length2:float = float(input("Enter the length of AC: "))
    hypotenuse:float = math.sqrt(length ** 2 + length2 ** 2)
    print(f"The length of BC (the hypotenuse) is: {hypotenuse:.2f}")

if __name__ == '__main__':
    main()