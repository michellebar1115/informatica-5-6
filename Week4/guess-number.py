import random
def main():


    name = input("Hello, what is your name? ").title()
    difficulty = input("Choose a difficulty, Easy, Medium, or Hard: ").title().strip()
    attempts = 6


    if difficulty == "Easy":
        print(f"Well, {name}, I am thinking of a number between 1 and 20.")
        while attempts > 0:
            number = random.randint(1,20)
            guess = int(input("Take a guess. "))


            if guess == number:
                print("Winner")
                break
            elif guess > number:
                attempts -= 1
                print("Too high.")
                print("Attempts left:",attempts)
            else:
                attempts -= 1
                print("Too low.")
                print("Attempts left:",attempts)


    elif difficulty == "Medium":
        print(f"Well, {name}, I am thinking of a number between 1 and 50.")
        while attempts > 0:
            number = random.randint(1,50)
            guess = int(input("Take a guess. "))


            if guess == number:
                print("Winner")
                break
            elif guess > number:
                attempts -= 1
                print("Too high.")
                print("Attempts left:",attempts)
            else:
                attempts -= 1
                print("Too low.")
                print("Attempts left:",attempts)


    elif difficulty == "Hard":
        print(f"Well, {name}, I am thinking of a number between 1 and 100.")
        while attempts > 0:
            number = random.randint(1,100)
            guess = int(input("Take a guess. "))


            if guess == number:
                print("Winner")
                break
            elif guess > number:
                attempts -= 1
                print("Too high.")
                print("Attempts left:",attempts)
            else:
                attempts -= 1
                print("Too low.")
                print("Attempts left:",attempts)


    else:
        print("Please choose one of the three options.")


if __name__ == "__main__":
    main()
