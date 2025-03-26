SENTENCE_START = "Once upon a time, in a world full of surprises, I discovered a tiny plant that could fly!"

def main():
    print("Tiny Mad Lib Generator")
    adjective:str = input("Please type an adjective and press enter: ")
    noun:str = input("Please type a noun and press enter: ")
    verb:str = input("Please type a verb and press enter: ")
    print(f"{SENTENCE_START.replace('tiny', adjective).replace('plant', noun).replace('fly', verb)}")

if __name__ == '__main__':
    main()