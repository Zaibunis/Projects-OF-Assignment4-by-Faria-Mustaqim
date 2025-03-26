def main():
    print("Feet to Inches Converter")
    feet:float = input("Enter the number of feet: ")
    inches:float = feet*12 #There are 12 inches per foot.
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == '__main__':
    main()