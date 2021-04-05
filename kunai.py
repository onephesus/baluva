import pygame
from pygame.sprite import Sprite

class Kunai(Sprite):
    """A class to manage kunai fired from the ninja"""

    def __init__(self, b_game):
        """Create a kunai object at the ninja's current position"""
        super().__init__()
        self.screen = b_game.screen
        self.settings = b_game.settings
        self.color = self.settings.kunai_color

        # Create a kunai rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.kunai_width,
            self.settings.kunai_height)
        self.rect.midright = b_game.ninja.rect.midright

        # Store the kunai's position as a decimal value
        self.x = float(self.rect.x)


    def update(self):
        """Move the kunai up the screen."""
        # Update the decimal position of the kunai.
        self.x += self.settings.kunai_speed
        # Update the rect position
        self.rect.x = self.x
    

    def draw_kunai(self):
        """Draw the kunai to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)