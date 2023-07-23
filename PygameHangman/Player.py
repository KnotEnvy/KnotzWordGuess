class Player:
    def __init__(self):
        self.wrong_guesses = 0

    def guess(self):
        while True:
            guess = input("Please enter a letter: ")
            if guess.isalpha() and len(guess) == 1:
                return guess.lower()
            else:
                print("Invalid input. Please enter a single letter.")

    def wrong_guess(self):
        self.wrong_guesses += 1

    def get_wrong_guesses(self):
        return self.wrong_guesses

    def reset(self):
        self.wrong_guesses = 0
