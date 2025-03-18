import random

word_list = ["apple", "grape", "kiwi", "orange", "date"]

word = random.choice(word_list)

def check_guess(player_guess):
    if player_guess.lower() in word:
        print(f"Good guess! {player_guess.upper()} is in the word.")
    else:
        print(f"Sorry, {player_guess} is not in the word! Try again.")

def ask_for_input():
    while True:
        player_guess = input("Guess a letter: ").lower()
        if len(player_guess) == 1 and player_guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(player_guess)

ask_for_input()
