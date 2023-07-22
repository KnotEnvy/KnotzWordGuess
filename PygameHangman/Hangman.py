import pygame
import math

class Hangman:
    def __init__(self, surface):
        self.surface = surface
        self.base_x = self.surface.get_width() // 2
        self.base_y = self.surface.get_height() // 3
        self.angle = 0

    def draw(self, stage):
        # Draw a gradient background
        for i in range(self.surface.get_height()):
            color = max(0, 255 - i // 3)
            pygame.draw.line(self.surface, (color, color, 255), (0, i), (self.surface.get_width(), i))

        # Draw the gallows
        pygame.draw.line(self.surface, (139,69,19), (self.base_x - 60, self.base_y + 170), (self.base_x + 60, self.base_y + 170), 10)
        pygame.draw.line(self.surface, (139,69,19), (self.base_x, self.base_y + 170), (self.base_x, self.base_y - 20), 10)
        pygame.draw.line(self.surface, (139,69,19), (self.base_x, self.base_y - 20), (self.base_x + 60, self.base_y - 20), 10)
        pygame.draw.line(self.surface, (139,69,19), (self.base_x + 60, self.base_y - 20), (self.base_x + 60, self.base_y + 20), 10)

        # Draw the noose
        pygame.draw.line(self.surface,(0 ,0 ,0),(self. base_x+60 ,self. base_y+20),(self. base_x+60 ,self. base_y+40))
        pygame.draw.polygon(self.surface,(0 ,0 ,0),[(self. base_x+55 ,self. base_y+40),(self. base_x+65 ,self. base_y+40),(self. base_x+60 ,self. base_y+45)])

        # Update the angle of the hangman character
        self.angle += 0.1

        # Calculate the position of the hangman character based on the angle
        x_offset = int(20 * math.sin(self.angle))
        y_offset = int(20 * math.cos(self.angle))

        # Draw the hangman character
        stages = [
            lambda: self.draw_head(x_offset, y_offset),
            lambda: self.draw_body(x_offset, y_offset),
            lambda: self.draw_left_arm(x_offset, y_offset),
            lambda: self.draw_right_arm(x_offset, y_offset),
            lambda: self.draw_left_leg(x_offset, y_offset),
            lambda: self.draw_right_leg(x_offset, y_offset),
        ]
        for i in range(stage):
            stages[i]()

    def draw_head(self,x_offset,y_offset):
        pygame.draw.circle(self.surface,(255 ,255 ,255),(self. base_x+60+x_offset ,self. base_y+50+y_offset ),20)

    def draw_body(self,x_offset,y_offset):
        pygame.draw.line(self.surface,(255 ,255 ,255),(self. base_x+60+x_offset ,self. base_y+70+y_offset),(self. base_x+60+x_offset ,self. base_y+120+y_offset))

    def draw_left_arm(self,x_offset,y_offset):
        pygame.draw.line(self.surface,(255 ,255 ,255),(self. base_x+60+x_offset ,self. base_y+80+y_offset),(self. base_x+40+x_offset ,self. base_y+100+y_offset))

    def draw_right_arm(self,x_offset,y_offset):
        pygame.draw.line(self.surface,(255 ,255 ,255),(self. base_x+60+x_offset ,self. base_y+80+y_offset),(self. base_x+80+x_offset ,self. base_y+100+y_offset))

    def draw_left_leg(self,x_offset,y_offset):
        pygame.draw.line(self.surface,(255 ,255 ,255),(self. base_x+60+x_offset ,self. base_y+120+y_offset),(self. base_x+40+x_offset ,self. base_y+150+y_offset))

    def draw_right_leg(self,x_offset,y_offset):
        pygame.draw.line(self.surface,(255 ,255 ,255),(self. base_x+60+x_offset ,self. base_y+120+y_offset),(self. base_x+80+x_offset ,self. base_y+150+y_offset))
