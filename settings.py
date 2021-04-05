import pygame

class Settings:
    """A class to store all settings for Baluva."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 3500
        self.screen_height = 2000
        self.bg_color = (230, 230, 230)
        
        # Ninja Settings
        self.ninja_speed = 20

        # Kunai settings
        self.kunai_speed = 1.0
        self.kunai_width = 3
        self.kunai_height = 15
        self.kunai_color = (60, 60, 60)