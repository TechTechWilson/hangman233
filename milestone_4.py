import random

word_list = ["apple", "grape", "kiwi", "orange", "date"]
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.guess = None
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for element in self.word]
        self.num_letters = list(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []


    def check_guess(self, guess):
        if guess.lower() in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(guess)] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print( "Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if guess.isalpha() is False or len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

play_hangman = Hangman(word_list)
play_hangman.ask_for_input()