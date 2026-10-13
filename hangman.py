





# Count how many letters the word has using len.
# Print an underline(_) for every letter.
# Create a variable that gives a certain amount of chances.
# Create a while loop that continues while the chances variable > 0.
# Make a new variable that is equal to the input of the guessed letter.
# Add a .strip() to the end of that variable.
# In the while loop create an if statement.
# Type "else" for incorrect letters.
# In the "else" display inputted incorrect letters with a print.
# In the same else line subtract 1 from the chances variable.

# Test the code and fix any errors.
import random
def main(): # Define the main function.

    start_game("hangman.txt") # Call the start_game with the txt file in it.

def start_game(file): # Define a new function for your hangman code with one parameter being your file.
    with open(file) as word_file: # Make a txt file. # Within that function, use the with " with open() as, variable".
        content = word_file.read().splitlines() # Make your variable equal to the word that is your desired answer. sort of
        print(random.choice(content))

if __name__ == "__main__":
    main() # Call the main function.
