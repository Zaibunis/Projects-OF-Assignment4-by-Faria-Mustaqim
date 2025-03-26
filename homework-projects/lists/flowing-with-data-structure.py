def add_three_copies(list, data):
    list += [data] * 3  
def main():
    print(" Simple Demonstration of Mutability in Python")
    message:str = input("Enter a message to copy: ")
    List_before = []
    print(f"List Before: {List_before}")
    add_three_copies(List_before, message )
    print(f"List After: {List_before}")

if __name__ == '__main__':
    main()