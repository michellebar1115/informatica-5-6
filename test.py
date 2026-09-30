def main():

    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number:"))
            not_validated = False
        except ValueError:
            print("You must enter a NUMBER.")

if __name__ == "__main__":
    main()
