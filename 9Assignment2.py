import random

# Function to read words from a file and store them in a list
def read_words_from_file(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip())
    return words

# Function to choose a random word from the list
def choose_random_word(word_list):
    return random.choice(word_list)

# Function to play the hangman game
def play_hangman(word):
    word = word.upper()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    hidden_word = ['_'] * len(word)

    while attempts > 0:
        print(" ".join(hidden_word))
        guess = input("Guess your letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            attempts -= 1
            print("Incorrect!")
            print(f"You have {attempts} {'chances' if attempts > 1 else 'chance'} left to guess.")

        if ''.join(hidden_word) == word:
            print("Congratulations! You guessed the word:", word)
            break

    if ''.join(hidden_word) != word:
        print("Sorry, you've run out of chances. The word was:", word)

# Main program
if __name__ == "__main__":
    filename = "words.txt"
    word_list = read_words_from_file(filename)
    
    while True:
        chosen_word = choose_random_word(word_list)
        play_hangman(chosen_word)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
