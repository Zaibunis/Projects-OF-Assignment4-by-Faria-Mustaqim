
def main():
    fruit = {"apple": 2 , "durian":3, "jackfruit": 2.0, "kiwi": 5.0, "rambutan": 9, "mango": 4.4}
    total_cost = 0
    for fruit, price in fruit.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))  # Get quantity from user
        total_cost += quantity * price  # Update total cost

    print(f"Your total is ${total_cost}")


if __name__ == '__main__':
    main()