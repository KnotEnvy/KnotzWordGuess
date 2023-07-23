import pygame

class MissedLettersDisplay:
    def __init__(self, surface, position, color, font_size):
        self.surface = surface
        self.position = position
        self.color = color
        self.font_size = font_size
        self.missed_letters = []

    def update_missed_letters(self, missed_letters):
        self.missed_letters = missed_letters

    def draw(self):
        circle_radius = self.font_size // 2
        spacing = 10

        for i, letter in enumerate(self.missed_letters):
            x = self.position[0] + (i * (2 * circle_radius + spacing))
            y = self.position[1]

            pygame.draw.circle(self.surface, self.color, (x + circle_radius, y + circle_radius), circle_radius)
            text = pygame.font.Font(None, self.font_size).render(letter.upper(), True, (255, 255, 255))
            text_rect = text.get_rect(center=(x + circle_radius, y + circle_radius))
            self.surface.blit(text, text_rect)
