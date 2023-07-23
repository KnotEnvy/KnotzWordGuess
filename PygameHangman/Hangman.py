import pygame
import math

class Hangman:
    def __init__(self, surface):
        self.surface = surface
        self.base_x = self.surface.get_width() // 2
        self.base_y = self.surface.get_height() // 3
        self.ice_thickness = 20

    def draw(self, stage):
        # Draw a gradient background
        for i in range(self.surface.get_height()):
            color = max(0, 255 - i // 3)
            pygame.draw.line(self.surface, (color, color, 255), (0, i), (self.surface.get_width(), i))

        # Draw the man
        self.draw_man()

        # Draw the ice
        self.draw_ice()

        # Draw the noose
        self.draw_noose()

        # Melt the ice a little more each time a wrong guess is made
        if stage > 0:
            self.ice_thickness -= 3

    def draw_man(self):
        pygame.draw.circle(self.surface, (255, 255, 255), (self.base_x, self.base_y - 20), 20)  # Head
        pygame.draw.line(self.surface, (255, 255, 255), (self.base_x, self.base_y), (self.base_x, self.base_y + 50))  # Body
        pygame.draw.line(self.surface, (255, 255, 255), (self.base_x, self.base_y + 10), (self.base_x - 20, self.base_y + 20))  # Left arm
        pygame.draw.line(self.surface, (255, 255, 255), (self.base_x, self.base_y + 10), (self.base_x + 20, self.base_y + 20))  # Right arm
        pygame.draw.line(self.surface, (255, 255, 255), (self.base_x, self.base_y + 50), (self.base_x - 10, self.base_y + 70))  # Left leg
        pygame.draw.line(self.surface, (255, 255, 255), (self.base_x, self.base_y + 50), (self.base_x + 10, self.base_y + 70))  # Right leg

    def draw_ice(self):
        pygame.draw.rect(self.surface, (173, 216, 230), (self.base_x - 30, self.base_y + 70, 60, self.ice_thickness))  # Ice

    def draw_noose(self):
        pygame.draw.line(self.surface, (0, 0, 0), (self.base_x, self.base_y - 40), (self.base_x, self.base_y - 60))  # Noose
