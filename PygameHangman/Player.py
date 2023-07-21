class Player:
    def __init__(self):
        self.wrong_guesses = 0

    def guess(self):
        return input("Please enter a letter: ")

    def wrong_guess(self):
        self.wrong_guesses += 1

    def get_wrong_guesses(self):
        return self.wrong_guesses

    def reset(self):
        self.wrong_guesses = 0
