MINIMUM_HEIGHT = 50

def main():
    print("How tall are you ?")
    user_input:float = float(input("How tall are you? "))
    if user_input > MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':
    main()