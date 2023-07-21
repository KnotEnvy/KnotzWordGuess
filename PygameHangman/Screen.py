import pygame
from Hangman import Hangman

# Define some constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Screen:
    def __init__(self):
        self.DISPLAYSURF = pygame.display.set_mode((600, 800), pygame.RESIZABLE)
        pygame.display.set_caption('Knotz WordGuess')
        self.font = pygame.font.Font(None, 36)
        self.hangman = Hangman(self.DISPLAYSURF)
        self.message = ""
        self.message_time = 0

    def display_start_screen(self):
        self.DISPLAYSURF.fill(WHITE)
        
        title_text = self.font.render('Knotz WordGuess!', True, BLACK)
        subtitle_text = self.font.render('Guess the word one letter at a time', True, BLACK)
        instruction_text = self.font.render('Press any key to start', True, BLACK)

        # Create Rect objects for the text
        title_text_rect = title_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 4))
        subtitle_text_rect = subtitle_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2))
        instruction_text_rect = instruction_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() * 3 // 4))

        # Blit the text on the screen using the Rect objects
        self.DISPLAYSURF.blit(title_text, title_text_rect)
        self.DISPLAYSURF.blit(subtitle_text, subtitle_text_rect)
        self.DISPLAYSURF.blit(instruction_text, instruction_text_rect)

        pygame.display.flip()

    def display_message(self, message):
        self.message = message
        self.message_time = pygame.time.get_ticks()

    def display_game_screen(self, player, word_bank):
        self.DISPLAYSURF.fill((255, 255, 255))
        # Draw hangman
        self.hangman.draw(player.get_wrong_guesses())
        word_text = self.font.render(word_bank.get_display_word(), True, (10, 10, 10))
        guess_text = self.font.render("Wrong guesses: " + str(player.get_wrong_guesses()), True, (10, 10, 10))
        self.DISPLAYSURF.blit(word_text, (50, 100))
        self.DISPLAYSURF.blit(guess_text, (50, 150))
        pygame.display.flip()

    def display_end_screen(self, won, word, player):
        self.DISPLAYSURF.fill((255, 255, 255))
        if won:
            self.display_message("Congratulations, you won!")
        else:
            self.display_message("Man, you couldn't get that? The word was " + word)

    def ask_restart(self):
        self.DISPLAYSURF.fill((255, 255, 255))
        self.display_message("You must want to play again? (yes/no)")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.unicode.lower() in ['y', 'yes']:
                        return True
                    if event.unicode.lower() in ['n', 'no']:
                        return False
