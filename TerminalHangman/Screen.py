class Screen:
    def display_start_screen(self):
        print("Welcome to Hangman!")
        input("Press Enter to start...")

    HANGMAN_PICS = ['''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
         ===''']
    
    
    
    
    def display_game_screen(self, player, word_bank):
        print(self.HANGMAN_PICS[player.get_wrong_guesses()])
        print("Current word: " + word_bank.get_display_word())
        print("Wrong guesses: " + str(player.get_wrong_guesses()))

    def display_end_screen(self, won, word, player):
        if won:
            print("Congratulations, you won!")
        else:
            print("Sorry, you lost. The word was " + word)
        print("Wrong guesses: " + str(player.get_wrong_guesses()))

    def ask_restart(self):
        response = input("Do you want to play again? (yes/no)").lower()
        positive_responses = ["yes", "y", "yeah", "sure"]
        negative_responses = ["no", "n", "nah", "nope"]
        while response not in positive_responses and response not in negative_responses:
            print("What are you doing?!")
            response = input("Do you want to play again? (yes/no)").lower()
        return response in positive_responses

