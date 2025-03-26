def get_first_element(lst):
    """Returns the first element of the list."""
    return lst[0] if lst else None  # Prevents error if the list is empty

def get_lst():
    print()
    lst_before = []
    while True:
        element = input("Please enter an element of the list or type 'stop' to end: ")
        if element.lower() == "stop":  # Stop if user types 'stop'
            break
        lst_before.append(element)
    
    return lst_before

def main():
    lst = get_lst()
    first_element = get_first_element(lst)
    
    if first_element is not None:
        print("The first element of the list is:", first_element)
    else:
        print("The list is empty.")

if __name__ == '__main__':
    main()
