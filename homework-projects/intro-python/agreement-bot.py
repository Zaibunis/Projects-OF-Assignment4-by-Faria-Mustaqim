
#agreement-bot

def main():
    print("Favorite Animal Matcher")
    animal1 : str = input("What's your favorite animal? ")
    animal2 : str = input(f"My favorite animal is also \033[1m{animal1}\033[0m!")
    animal2 : str = str(animal2)

if __name__ == '__main__':
    main()
