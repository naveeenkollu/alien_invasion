
class Settings:
    """Class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialized game settings"""

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 700
        self.bg_color = (31, 29, 54)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (204, 172, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

