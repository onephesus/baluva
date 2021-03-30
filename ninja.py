import pygame

class Ninja:
    """A class to manage the ninja."""
    
    def __init__(self, b_game):
        """Initialize the ninja and set its starting position."""
        self.screen = b_game.screen
        self.screen_rect = b_game.screen.get_rect()
        self.settings = b_game.settings
        
        # Load the ninja image and get its rect.
        self.image = pygame.image.load('images/Idle__000.png')
        self.rect = self.image.get_rect()
        
        # Start each new ninja at the bottom left of the screen.
        self.rect.bottomleft = self.screen_rect.bottomleft
        
        # Store a decimal value for the ninja's vertical position.
        self.y = float(self.rect.y)
        
        # Movement flag
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ninja's position based on the movement flag."""
        # Update the ninja's y value, not the rect
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ninja_speed
            self.image = pygame.image.load('images/Jump__006.png')
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ninja_speed
            self.image = pygame.image.load('images/Jump__006.png')
        else:
            self.image = pygame.image.load('images/Idle__000.png')
            
        # Update rect object from self.y
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the ninja at its current location."""
        self.screen.blit(self.image, self.rect)