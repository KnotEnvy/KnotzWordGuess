import pygame
from Hangman import Hangman
from Text import Text  # New class for animated text
from MissedLettersDisplay import MissedLettersDisplay

# Define some constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 139)
ORANGE = (255, 165, 0)

class Screen:
    def __init__(self):
        pygame.font.init()
        self.DISPLAYSURF = pygame.display.set_mode((600, 800), pygame.RESIZABLE)
        pygame.display.set_caption('Knotz WordGuess')
        self.font = pygame.font.Font(None, 36)
        self.hangman = Hangman(self.DISPLAYSURF)
        
        self.message = Text("", 36, (50, 50), (10, 10, 10), self.DISPLAYSURF)
        self.missed_letters_display = MissedLettersDisplay(self.DISPLAYSURF, (50, 200), (255, 0, 0), 40)
    def display_start_screen(self):
        # Draw a gradient sky
        for i in range(self.DISPLAYSURF.get_height() // 2):
            color = max(0, 255 - i // 3)
            pygame.draw.line(self.DISPLAYSURF, (color, color, 255), (0, i), (self.DISPLAYSURF.get_width(), i))

        # Draw a gradient icy ground
        for i in range(self.DISPLAYSURF.get_height() // 2, self.DISPLAYSURF.get_height()):
            color = max(0, 255 - (self.DISPLAYSURF.get_height() - i) // 3)
            pygame.draw.line(self.DISPLAYSURF, (color, color, 255), (0, i), (self.DISPLAYSURF.get_width(), i))

        # Draw snow-capped mountains
        pygame.draw.polygon(self.DISPLAYSURF, (255, 255, 255), [(0, self.DISPLAYSURF.get_height() // 2),
                                                                 (self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 4),
                                                                 (self.DISPLAYSURF.get_width(), self.DISPLAYSURF.get_height() // 2)])

        # Draw icicles hanging from the top of the screen
        for i in range(0, self.DISPLAYSURF.get_width(), 30):
            pygame.draw.polygon(self.DISPLAYSURF, (255, 255, 255), [(i, 0), (i + 15, 30), (i + 30, 0)])


        title_font = pygame.font.Font("Fonarto.ttf", 48)
        subtitle_font = pygame.font.Font("Fonarto.ttf", 36)
        instruction_font = pygame.font.Font("Fonarto.ttf", 24)

        title_text = title_font.render('Knotz WordGuess!', True, DARK_BLUE)
        subtitle_text = subtitle_font.render('Guess the word one letter at a time', True, BLACK)
        instruction_text = instruction_font.render('Press Enter to start', True, ORANGE)

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

    def display_difficulty_screen(self):
        # Draw a gradient background
        for i in range(self.DISPLAYSURF.get_height()):
            color = max(0, 255 - i // 3)
            pygame.draw.line(self.DISPLAYSURF, (color, color, 255), (0, i), (self.DISPLAYSURF.get_width(), i))

        title_font = pygame.font.Font("Fonarto.ttf", 48)
        option_font = pygame.font.Font("Fonarto.ttf", 30)

        title_text = title_font.render('Select Level', True, DARK_BLUE)
        easy_text = option_font.render('1. Easy', True, BLACK)
        medium_text = option_font.render('2. Medium', True, BLACK)
        hard_text = option_font.render('3. Hard', True, BLACK)
        expert_text = option_font.render('4. Biggest Words Ever', True, BLACK)
        animal_text = option_font.render('5. Animals', True, BLACK)
        color_text = option_font.render('6. Colors', True, BLACK)
        country_text = option_font.render('7. Countries', True, BLACK)
        state_text = option_font.render('8. States', True, BLACK)

        title_text_rect = title_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 4-50))
        easy_text_rect = easy_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2 - 100))
        medium_text_rect = medium_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2-50))
        hard_text_rect = hard_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2))
        expert_text_rect = expert_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2 + 50))
        animal_text_rect = animal_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2 + 100))
        color_text_rect = color_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2 + 150))
        country_text_rect = country_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2 + 200))
        state_text_rect = state_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2 + 250))

        self.DISPLAYSURF.blit(title_text, title_text_rect)
        self.DISPLAYSURF.blit(easy_text, easy_text_rect)
        self.DISPLAYSURF.blit(medium_text, medium_text_rect)
        self.DISPLAYSURF.blit(hard_text, hard_text_rect)
        self.DISPLAYSURF.blit(expert_text, expert_text_rect)
        self.DISPLAYSURF.blit(animal_text, animal_text_rect)
        self.DISPLAYSURF.blit(color_text, color_text_rect)
        self.DISPLAYSURF.blit(country_text, country_text_rect)
        self.DISPLAYSURF.blit(state_text, state_text_rect)

        pygame.display.flip()

        # Variable to keep track of the user's choice
        selected_difficulty = None

        while selected_difficulty is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_difficulty = 'easy'
                    elif event.key == pygame.K_2:
                        selected_difficulty = 'medium'
                    elif event.key == pygame.K_3:
                        selected_difficulty = 'hard'
                    elif event.key == pygame.K_4:
                        selected_difficulty = 'expert'
                    elif event.key == pygame.K_5:
                        selected_difficulty = 'animals'
                    elif event.key == pygame.K_6:
                        selected_difficulty = 'colors'
                    elif event.key == pygame.K_7:
                        selected_difficulty = 'countries'
                    elif event.key == pygame.K_8:
                        selected_difficulty = 'states'

        return selected_difficulty

    def display_message(self, message):
        self.message.set_text(message)  # Use the new Text class to set the message

    def display_game_screen(self, player, word_bank, guess):
        # Fill the screen with white
        self.DISPLAYSURF.fill((255, 255, 255))

        # Draw the hangman based on the player's wrong guesses
        self.hangman.draw(player.get_wrong_guesses())

        # Adjust the font size based on the length of the word
        font_size = min(36, self.DISPLAYSURF.get_width() // len(word_bank.get_display_word()))
        font = pygame.font.Font("Fonarto.ttf", font_size)

        # Render the word and guess texts
        word_text = Text(word_bank.get_display_word(), font_size, (50, 100), (10, 10, 10), self.DISPLAYSURF)
        guess_text = font.render(f"Your guess: {guess}", True, (10, 10, 10))

        # Update text animation and draw the updated text
        word_text.update_animation()
        word_text.draw()

        # Display the word and guess texts
        self.DISPLAYSURF.blit(guess_text, (50, 150))

        # Update and draw the missed letters display
        missed_letters = ", ".join(word_bank.guessed_letters)
        missed_text = font.render("Missed letters: " + missed_letters, True, (255, 0, 0))
        missed_text_rect = missed_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() - 50))
        self.DISPLAYSURF.blit(missed_text, missed_text_rect)

        # Update the display
        pygame.display.flip()

    def display_end_screen(self, won, word, player):
        self.DISPLAYSURF.fill((255, 255, 255))
        if won:
            end_text = self.font.render("Congratulations, you won!", True, DARK_BLUE)
        else:
            end_text = self.font.render("You did not make it. The word was " + word, True, BLACK)
        end_text_rect = end_text.get_rect(center=(self.DISPLAYSURF.get_width() // 2, self.DISPLAYSURF.get_height() // 2))
        self.DISPLAYSURF.blit(end_text, end_text_rect)
        pygame.display.flip()

    def ask_restart(self):
        self.DISPLAYSURF.fill((255, 255, 255))
        restart_text = self.font.render("Would you like to play again? (yes/no)", True, ORANGE)
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
