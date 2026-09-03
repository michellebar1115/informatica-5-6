import random

def main():

    coin = ["heads","tails"]
    attempts = 3

    while attempts > 0:
        flip = random.choice(coin)
        guess = input("Heads or Tails? ").strip().lower()

        print("The coin landed on", flip)

        if guess == flip:
            print("Winner!")
            break
        else:
            print("Loser!")
            attempts -= 1
            print("Attempts left:", attempts)


if __name__ == "__main__":
    main()
