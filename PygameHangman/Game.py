import pygame
import traceback
from Screen import Screen
from WordBank import WordBank
from Player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.player = Player()
        self.game_over = False
        self.won = False
        


    def start(self):
        if self.screen.display_start_screen():
            difficulty_level = self.screen.display_difficulty_screen()
            self.word_bank = WordBank(difficulty_level)
            self.new_round()
        else:
            pygame.quit()
            return

    def new_round(self):
        self.game_over = False
        self.won = False
        self.player.reset()
        self.word_bank.new_word()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    guess = event.unicode.lower()
                    self.game_loop(guess)

    def game_loop(self, guess):
        if guess.isalpha():  # Check if the guess is a letter here
            if self.word_bank.is_already_guessed(guess):
                self.screen.display_message("You've already guessed this letter!")
            elif not self.word_bank.check_guess(guess):
                self.player.wrong_guess()
        if self.word_bank.all_guessed():
            self.won = True
            self.game_over = True
        elif self.player.get_wrong_guesses() >= 7:
            self.game_over = True
        if self.game_over:
            self.screen.display_end_screen(self.won, self.word_bank.get_word(), self.player)
            end_ticks = pygame.time.get_ticks()
            while pygame.time.get_ticks() - end_ticks < 2000:  # Wait for 2 seconds while still processing events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit_game()
            if self.screen.ask_restart():
                self.new_round()
            else:
                self.quit_game()

        else:
            self.screen.display_game_screen(self.player, self.word_bank, guess)


    def quit_game(self):
        pygame.quit()
        exit()


if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except Exception as e:
        print(f"Sorry, something went wrong: {e}")
        traceback.print_exc()  # Print the full stack trace
        pygame.quit()