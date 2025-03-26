def main():
    print("Triangle Perimeter Calculator")
    side_1 = float(input("What is the length of side 1?"))
    side_2 = float(input("What is the length of side 2?"))
    side_3 = float(input("What is the length of side 3?"))
    triangle_perimeter = (side_1+side_2+side_3)
    print(f"The perimeter of the triangle is {triangle_perimeter}")

if __name__ == '__main__':
    main()