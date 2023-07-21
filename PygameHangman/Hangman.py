import pygame

class Hangman:
    def __init__(self, surface):
        self.surface = surface
        self.base_x = self.surface.get_width() // 2
        self.base_y = self.surface.get_height() // 3

    def draw(self, stage):
        stages = [
            self.draw_head,
            self.draw_body,
            self.draw_left_arm,
            self.draw_right_arm,
            self.draw_left_leg,
            self.draw_right_leg,
        ]
        for i in range(stage):
            stages[i]()

    def draw_head(self):
        pygame.draw.circle(self.surface, (0, 0, 0), (self.base_x, self.base_y), 20, 2)

    def draw_body(self):
        pygame.draw.line(self.surface, (0, 0, 0), (self.base_x, self.base_y + 20), (self.base_x, self.base_y + 70), 2)

    def draw_left_arm(self):
        pygame.draw.line(self.surface, (0, 0, 0), (self.base_x, self.base_y + 30), (self.base_x - 20, self.base_y + 50), 2)

    def draw_right_arm(self):
        pygame.draw.line(self.surface, (0, 0, 0), (self.base_x, self.base_y + 30), (self.base_x + 20, self.base_y + 50), 2)

    def draw_left_leg(self):
        pygame.draw.line(self.surface, (0, 0, 0), (self.base_x, self.base_y + 70), (self.base_x - 20, self.base_y + 100), 2)

    def draw_right_leg(self):
        pygame.draw.line(self.surface, (0, 0, 0), (self.base_x, self.base_y + 70), (self.base_x + 20, self.base_y + 100), 2)
