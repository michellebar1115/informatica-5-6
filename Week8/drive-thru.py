def main():

    def welcome():
        menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
        print("Welcome to idek!")
        print("Here's your menu:")
        for i in range(len(menu)):
            print(f"{i+1}. {menu[i]}")

    welcome()

    def get_item(item):
        item = item.strip().title()

        if item == "Cheeseburger":
            print("🍔")
        elif item == "Fries":
            print("🍟")
        elif item == "Soda":
            print("🥤")
        elif item == "Ice Cream":
            print("🍦")
        elif item == "Cookie":
            print("🍪")
        else:
            print("Please choose one of the items on the menu.")

    user_choice = input("Which item would you like? ")

    get_item(user_choice)


if __name__ == "__main__":
    main()
