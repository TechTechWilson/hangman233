import random

word_list = ["apple", "grape", "kiwi", "orange", "date"]
print(word_list)

word = random.choice(word_list)
print(word)

player_guess = input("Guess a letter: ").lower()
if len(player_guess) == 1 and player_guess.isalpha():
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")
