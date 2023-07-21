import random

class WordBank:
    def __init__(self):
        self.words = ["apple", "banana", "cherry", "date", "elderberry"]
        self.word = ""
        self.guesses = []

    def new_word(self):
        self.word = random.choice(self.words)
        self.guesses = ['_'] * len(self.word)

    def check_guess(self, guess):
        correct = False
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.guesses[i] = guess
                correct = True
        return correct

    def all_guessed(self):
        return '_' not in self.guesses

    def get_word(self):
        return self.word

    def get_display_word(self):
        return ' '.join(self.guesses)
