import traceback
import pygame 
from Game import Game

if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except Exception as e:
        print(f"Sorry, something went wrong: {e}")
        traceback.print_exc()  # Print the full stack trace
        pygame.quit()
