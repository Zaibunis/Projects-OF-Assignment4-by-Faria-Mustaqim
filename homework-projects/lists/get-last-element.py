def get_last_element(lst):
    """Prints the last element of the list."""
    print(f"The last element of the list is: {lst[-1]}")  
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
    get_last_element(lst)  

if __name__ == '__main__':
    main()
