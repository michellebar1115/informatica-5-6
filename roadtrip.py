def main():
    # Finite loop
    answer = ""
    followup = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").title().strip()
        if answer == "Yes":
            followup= input("Really? ").title().strip()
        if followup == "Yes":
            break

    print("We are here!")

if __name__ == "__main__":
    main()
