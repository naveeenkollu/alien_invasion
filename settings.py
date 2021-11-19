class Settings:
    """Class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialized game settings"""

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

