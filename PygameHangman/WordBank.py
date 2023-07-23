import csv
import random

class WordBank:
    def __init__(self, difficulty_level):
        self.words = []
        self.word = ""
        self.guesses = []
        self.guessed_letters = []

        # Load the words from the CSV file
        with open('words.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == difficulty_level:
                    self.words = row[1:]

    def reset(self):
        self.guesses = []
        self.guessed_letters = []

    def new_word(self):
        self.word = random.choice(self.words)
        self.guesses = ['_'] * len(self.word)
        self.guessed_letters = []

    def check_guess(self, guess):
        self.guessed_letters.append(guess)
        correct = False
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.guesses[i] = guess
                correct = True
        return correct

    def is_already_guessed(self, guess):
        return guess in self.guessed_letters

    def all_guessed(self):
        return '_' not in self.guesses

    def get_word(self):
        return self.word

    def get_display_word(self):
        return ' '.join(self.guesses)
