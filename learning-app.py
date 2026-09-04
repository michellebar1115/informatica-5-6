import random
def main():

    print("Welcome to MADMATH.")

    streak = 0
    star = "⭐"
    operation = input("Which operation would you like to do? Addition, Subtraction, or Multiplication: ").strip().title()

    if operation == "Addition":

        while streak != 3:
            number1 = random.randint(10,99)
            number2 = random.randint(10,99)
            addition = number1 + number2

            print(f"What is {number1} + {number2}?")
            guess = int(input("Your answer: "))

            if addition == guess:
                streak += 1
                print("Correct!")
                if streak == 1:
                    print("Streak:", star)
                elif streak == 2:
                    print("Streak:", star,star)
                else:
                    print("Streak:", star,star,star)
            else:
                streak = 0
                print("Incorrect")
                print("The answer was:",addition)

    if operation == "Subtraction":

        while streak != 3:
            number1 = random.randint(10,99)
            number2 = random.randint(10,99)
            subtraction = number1 - number2

            print(f"What is {number1} - {number2}?")
            guess = int(input("Your answer: "))

            if subtraction == guess:
                streak += 1
                print("Correct!")
                if streak == 1:
                    print("Streak:", star)
                elif streak == 2:
                    print("Streak:", star,star)
                else:
                    print("Streak:", star,star,star)
            else:
                streak = 0
                print("Incorrect")
                print("The answer was:",subtraction)
                
    if operation == "Multiplication":

        while streak != 3:
            number1 = random.randint(10,99)
            number2 = random.randint(10,99)
            multiplication = number1 * number2

            print(f"What is {number1} - {number2}?")
            guess = int(input("Your answer: "))

            if multiplication == guess:
                streak += 1
                print("Correct!")
                if streak == 1:
                    print("Streak:", star)
                elif streak == 2:
                    print("Streak:", star,star)
                else:
                    print("Streak:", star,star,star)
            else:
                streak = 0
                print("Incorrect")
                print("The answer was:",multiplication)
    else:
        print("Please provide one of the 3 operation options.")




if __name__ == "__main__":
    main()

