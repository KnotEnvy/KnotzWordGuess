import pygame
from Screen import Screen
from WordBank import WordBank
from Player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.word_bank = WordBank()
        self.player = Player()
        self.game_over = False
        self.won = False

    def start(self):
        self.screen.display_start_screen()
        while True:  # Wait for the Enter key to start the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.new_round()

    def new_round(self):
        self.game_over = False
        self.won = False
        self.player.reset()
        self.word_bank.new_word()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    guess = event.unicode.lower()
                    if guess.isalpha():
                        self.game_loop(guess)

    def game_loop(self, guess):
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
            pygame.time.wait(2000)
            if self.screen.ask_restart():
                self.new_round()
            else:
                pygame.quit()
                return
        else:
            self.screen.display_game_screen(self.player, self.word_bank)
