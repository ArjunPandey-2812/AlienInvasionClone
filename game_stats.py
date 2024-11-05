import os


class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.game_active = False
        self.game_paused = False
        self.game_ended = False

        self.high_score = self.load_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.level = 1
        self.high_score_achieved = False
        self.score = 0

    def load_high_score(self):
        """Load the high score from a file, or return 0 if the file does not exist."""
        highscore_file = './resources/data/high_score.txt'

        try:
            with open(highscore_file, 'r') as f_object:
                high_score = f_object.read()
                return int(high_score) if high_score else 0
        except FileNotFoundError:
            return 0
 