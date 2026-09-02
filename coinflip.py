import random

def main():

    coin = random ["heads","tails"]
    attempts = 3

    guess = input("heads or tails?").strip()


    if coin == guess:
        print("Winner!")
    else:
        print("Loser!")


if __name__ == "__main__":
    main()
