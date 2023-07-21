from Screen import Screen
from WordBank import WordBank
from Player import Player

class Game:
    def __init__(self):
        self.screen = Screen()
        self.word_bank = WordBank()
        self.player = Player()
        self.game_over = False
        self.won = False

    def start(self):
        self.screen.display_start_screen()
        self.new_round()

    def new_round(self):
        self.game_over = False
        self.won = False
        self.player.reset()
        self.word_bank.new_word()
        while not self.game_over:
            self.game_loop()

    def game_loop(self):
        self.screen.display_game_screen(self.player, self.word_bank)
        guess = self.player.guess()
        if not self.word_bank.check_guess(guess):
            self.player.wrong_guess()
        if self.word_bank.all_guessed():
            self.won = True
            self.game_over = True
        elif self.player.get_wrong_guesses() >= 7:
            self.game_over = True
        if self.game_over:
            self.screen.display_end_screen(self.won, self.word_bank.get_word(), self.player)
            if self.screen.ask_restart():
                self.new_round()

