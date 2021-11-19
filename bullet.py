import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        """Created bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Created a bullet rect at (0, 0) and set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width)
        self.settings.bullet_height()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Storing bullet position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Moves the bullet up to the screen"""
        # Updates decimal position of bullet.
        self.y = self.settings.bullet_speed

        # Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

