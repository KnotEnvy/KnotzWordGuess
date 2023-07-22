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
        instruction_text = self.font.render('Press Enter to start', True, BLACK)

        title_text_rect = title_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 4))
        subtitle_text_rect = subtitle_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2))
        instruction_text_rect = instruction_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() * 3 // 4))

        self.DISPLAYSURF.blit(title_text, title_text_rect)
        self.DISPLAYSURF.blit(subtitle_text, subtitle_text_rect)
        self.DISPLAYSURF.blit(instruction_text, instruction_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True


    def display_message(self, message):
        self.message = message
        self.message_time = pygame.time.get_ticks()

    def display_game_screen(self, player, word_bank):
        self.DISPLAYSURF.fill((255, 255, 255))
        # Draw hangman
        self.hangman.draw(player.get_wrong_guesses())

        # Adjust font size based on the length of the word
        font_size = min(36, self.DISPLAYSURF.get_width() // len(word_bank.get_display_word()))
        font = pygame.font.Font(None, font_size)

        word_text = font.render(word_bank.get_display_word(), True, (10, 10, 10))
        guess_text = self.font.render("Wrong guesses: " + str(player.get_wrong_guesses()), True, (10, 10, 10))
        self.DISPLAYSURF.blit(word_text, (50, 100))
        self.DISPLAYSURF.blit(guess_text, (50, 150))
        pygame.display.flip()


    def display_end_screen(self, won, word, player):
        self.DISPLAYSURF.fill((255, 255, 255))
        if won:
            end_text = self.font.render("Congratulations, you won!", True, (10, 10, 10))
        else:
            end_text = self.font.render("You did not make it. The word was " + word, True, (10, 10, 10))
        end_text_rect = end_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2))
        self.DISPLAYSURF.blit(end_text, end_text_rect)
        pygame.display.flip()

    def ask_restart(self):
        self.DISPLAYSURF.fill((255, 255, 255))
        restart_text = self.font.render("Would you like to play again? (yes/no)", True, (10, 10, 10))
        restart_text_rect = restart_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2))
        self.DISPLAYSURF.blit(restart_text, restart_text_rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.unicode.lower() in ['y', 'yes']:
                        return True
                    if event.unicode.lower() in ['n', 'no']:
                        return False

