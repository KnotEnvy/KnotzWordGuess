import pygame
import random

# Define some constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SpaceShooterGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Space Shooter Mini-Game')
        self.clock = pygame.time.Clock()
        self.is_running = False

        # Player attributes
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT - 50
        self.player_speed = 5

        # Laser attributes
        self.lasers = []

        # Enemy attributes
        self.enemies = []
        self.enemy_spawn_delay = 60  # Number of frames between enemy spawns
        self.enemy_spawn_counter = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Shoot a laser
                    self.lasers.append([self.player_x, self.player_y])

    def update_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed

        # Ensure the player stays within the screen boundaries
        self.player_x = max(0, min(self.player_x, SCREEN_WIDTH))

    def update_lasers(self):
        # Move lasers up the screen
        for laser in self.lasers:
            laser[1] -= 10

        # Remove lasers that are out of the screen
        self.lasers = [laser for laser in self.lasers if laser[1] > 0]

    def update_enemies(self):
        # Spawn a new enemy periodically
        self.enemy_spawn_counter += 1
        if self.enemy_spawn_counter >= self.enemy_spawn_delay:
            self.enemy_spawn_counter = 0
            enemy_x = random.randint(0, SCREEN_WIDTH)
            enemy_y = 0
            self.enemies.append([enemy_x, enemy_y])

        # Move enemies down the screen
        for enemy in self.enemies:
            enemy[1] += 5

        # Remove enemies that are out of the screen
        self.enemies = [enemy for enemy in self.enemies if enemy[1] < SCREEN_HEIGHT]

    def check_collisions(self):
        # Check for collisions between lasers and enemies
        # TODO: Implement collision detection and handle interactions here

    def draw_objects(self):
        # Draw the player's spaceship
        pygame.draw.rect(self.screen, GREEN, (self.player_x - 25, self.player_y - 10, 50, 20))

        # Draw lasers
        for laser in self.lasers:
            pygame.draw.rect(self.screen, RED, (laser[0], laser[1], 3, 10))

        # Draw enemies
        for enemy in self.enemies:
            pygame.draw.circle(self.screen, WHITE, (enemy[0], enemy[1]), 10)

    def run(self):
        while self.is_running:
            self.clock.tick(60)
            self.handle_events()

            self.update_player()
            self.update_lasers()
            self.update_enemies()

            self.check_collisions()

            self.screen.fill(BLACK)
            self.draw_objects()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = SpaceShooterGame()
    game.start()