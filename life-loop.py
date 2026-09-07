import time
def main():

    print("Good morning!")
    variable = 1
    while variable != 0:

        answer = input("Would you like to sleep one more minute? ").title().strip()

        if answer == "Yes":
            start = 6
            while start > 0:
                print(start)
                time.sleep(1)
                start -= 1

        elif answer == "No":
            print("Good luck with your day!")
            variable -= 1

        else:
            print("Please choose yes or no.")


if __name__ == "__main__":
    main()
