import random
def main(): # Define the main function.
    start_game("hangman.txt") # Call the start_game with the txt file in it.

def start_game(file): # Define a new function for your hangman code with one parameter being your file.
    attempt = 10 # Create a variable that gives a certain amount of chances.
    with open(file) as f: # Make a txt file. # Within that function, use the with " with open() as, variable".
        word_bank = f.read().splitlines() # Make your variable equal to the word that is your desired answer. sort of
        # print(random.choice(word)) just for checking
    word = random.choice(word_bank)
    hint = ["_"] * len(word) # Have an underline(_) for every letter.
    incorrect_letters = []
    while attempt > 0: # Create a while loop that continues while the chances variable > 0.
        print("Current word:", " ".join(hint))

        while True:
            guess = input("Guess a letter: ").lower() # Make a new variable that is equal to the input of the guessed letter. # Add a .strip() to the end of that variable.
            if len(guess) == 1: #a letter # In the while loop create an if statement.
                break
            else:
                print("Invalid guess. Try again")

        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempt -= 1
            print("You already guessed that letter! Attempts left:", str(attempt))
        else:
            attempt -= 1
            print("Wrong guess! Attempts left:", str(attempt))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")

        if "_" not in hint:
            print("Congratulations! You guessed the word:", word)
            break


    if attempt == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", word)


if __name__ == "__main__":
    main() # Call the main function.

    # Test the code and fix any errors.
