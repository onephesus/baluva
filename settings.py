import pygame

class Settings:
    """A class to store all settings for Baluva."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 3000
        self.screen_height = 2250
        self.bg = pygame.image.load("images/desertTileSet/png/BG.png")