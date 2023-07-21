import pygame 
from Game import Game

if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except Exception as e:
        print(f"Sorry, something went wrong: {e}")
        pygame.quit()
