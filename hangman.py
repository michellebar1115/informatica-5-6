

















import random
def main(): # Define the main function.

    start_game("hangman.txt") # Call the start_game with the txt file in it.

def start_game(file): # Define a new function for your hangman code with one parameter being your file.
    with open(file) as word_file: # Make a txt file. # Within that function, use the with " with open() as, variable".
        content = word_file.read().splitlines() # Make your variable equal to the word that is your desired answer. sort of
        # print(random.choice(content)) just for checking
        answ = random.choice(content)
    count = len(answ) # Count how many letters the word has using len.
    answer = ["_"]* count # Have an underline(_) for every letter.
    print(" ".join(answer)) # Print it.

    chances = 10 # Create a variable that gives a certain amount of chances.
    while chances >= 1: # Create a while loop that continues while the chances variable > 0.
        guess = input("Guess a letter: ").strip() # Make a new variable that is equal to the input of the guessed letter. # Add a .strip() to the end of that variable.
        if len(guess) == 1: #a letter # In the while loop create an if statement.
            break

        else:
            print("Invalid guess")

        for i in answ:
            if guess == i:

            else: # Type "else" for incorrect letters.
                chances -= 1 # In the same else line subtract 1 from the chances variable.
                print(guess) # In the "else" display inputted incorrect letters with a print.




if __name__ == "__main__":
    main() # Call the main function.

    # Test the code and fix any errors.
