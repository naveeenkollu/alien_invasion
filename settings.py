
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
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 12
        self.bullet_color = (204, 172, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



