import pygame

class Ninja:
    """A class to manage the ninja."""
    
    def __init__(self, b_game):
        """Initialize the ninja and set its starting position."""
        self.screen = b_game.screen
        self.screen_rect = b_game.screen.get_rect()
        
        # Load the ninja image and get its rect.
        self.image = pygame.image.load('images/Idle__000.png')
        self.rect = self.image.get_rect()
        
        # Start each new ninja at the bottom left of the screen.
        self.rect.bottomleft = self.screen_rect.bottomleft
        
    def blitme(self):
        """Draw the ninja at its current location."""
        self.screen.blit(self.image, self.rect)