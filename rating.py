def main():

    print("Michy's Pastaria")

    rating = float(input("What do you rate Michy's Pastaria from 0-5? Use decimals. : "))

    if rating > 5:
        print("Choose a number between 0-5")
    elif rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")

if __name__ == "__main__":
    main()

