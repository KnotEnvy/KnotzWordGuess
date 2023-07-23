import pygame

class Text:
    def __init__(self, text, font_size, position, color, surface):
        self.text = text
        self.font = pygame.font.Font("Fonarto.ttf", font_size)
        self.position = position
        self.color = color
        self.surface = surface
        self.animation_speed = 20
        self.target_text = ""
        self.is_animating = False
        self.animation_offset = 0

    def set_text(self, text):
        if self.text != text:
            self.target_text = text
            self.animation_offset = -self.surface.get_width()
            self.is_animating = True

    def update_animation(self):
        if self.is_animating and self.target_text != "":
            if self.text == self.target_text:
                self.is_animating = False
                self.target_text = ""
            else:
                diff = len(self.target_text) - len(self.text)
                if diff > 0:
                    self.text += self.target_text[len(self.text):len(self.text) + self.animation_speed + 1]
                else:
                    self.text = self.text[:len(self.text) - self.animation_speed]
                self.animation_offset += self.animation_speed

            self.draw()

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.position[0] + self.animation_offset, self.position[1])
        self.surface.blit(text_surface, text_rect)


