import pygame

class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Initialized the ship and set its starting position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads the ship image and its rect.
        self.image = pygame.image.load('alien_invasion\images\player-ship.png')
        self.rect = self.image.get_rect()

        # Starts each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)