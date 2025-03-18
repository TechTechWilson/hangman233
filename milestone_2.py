import random

word_list = ["apple", "grape", "kiwi", "orange", "date"]
print(word_list)

word = random.choice(word_list)
print(word)

player_guess = input("Guess a single letter: ")
if len(player_guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")