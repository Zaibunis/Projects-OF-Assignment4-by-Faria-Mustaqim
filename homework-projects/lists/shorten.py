MAX_SIZE = 3  
def trim_list(data):
    """Removes and prints elements until the list length is MAX_SIZE."""
    while len(data) > MAX_SIZE:
        removed_item = data.pop()
        print(removed_item)

def collect_inputs():
    """Collects user inputs into a list until they press Enter to stop."""
    items = []
    value = input("Enter an item (or enter stop): ")
    while value != "stop":
        items.append(value)
        value = input("Enter an item (or enter stop): ")
    return items

def main():
    user_list = collect_inputs()
    trim_list(user_list)

if __name__ == '__main__':
    main()
