import random

def generate_random_number():
    """Generate a 4-digit random number with no repeated digits."""
    while True:
        number = ''.join(random.sample('0123456789', 4))
        if number[0] != '0':  # Ensure the first digit is not 0
            return number

def count_cows_and_bulls(secret, guess):
    """Count the number of cows and bulls in the guess."""
    cows = sum(1 for s, g in zip(secret, guess) if s == g)
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_random_number()
    attempts = 0

    while True:
        guess = input("Enter a 4-digit number (with no repeated digits): ")
        
        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
            print("Please enter a valid 4-digit number with no repeated digits.")
            continue
        
        attempts += 1
        cows, bulls = count_cows_and_bulls(secret_number, guess)

        if cows == 4:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        else:
            print(f"{cows} cow{'s' if cows != 1 else ''}, {bulls} bull{'s' if bulls != 1 else ''}")

if __name__ == "__main__":
    main()
