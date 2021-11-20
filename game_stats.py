class GameStats:
    """Tracks statistics for Alien Invasion."""

    def __init__(self, ai_game):
            self.settings = ai_game.settings
            self.reset_stats()

            # Start Alien Inavsion in an active state.
            self.game_active = True

    def reset_stats(self):
        """Initializing the stats that can change during the game."""
        self.ships_left = self.settings.ship_limit