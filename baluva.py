import sys
import pygame
from pygame.locals import *

from settings import Settings
from ninja import Ninja
from tileset import Tileset

class Baluva:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Iinitialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height), RESIZABLE)
        pygame.display.set_caption("Baluva")
        
        self.ninja = Ninja(self)
        self.tileset = Tileset(self)
    
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ninja to the right.
                    self.ninja.rect.x += 1
            
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screeen during each pass through the loop.
        self.tileset.blitme()
        self.ninja.blitme()
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    b = Baluva()
    b.run_game()