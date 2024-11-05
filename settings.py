import pygame

class Settings():
    """A class to store all settings for 'Alien Invasion'."""

    MAX_SPEED = 15  # Maximum speed for ships and aliens
    FALLBACK_BG_COLOR = (170, 255, 225)  # Fallback color for the background

    def __init__(self):
        """Initialize game's static settings."""
        # Screen settings
        self.fps = 60
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = Settings.FALLBACK_BG_COLOR

        # Load and scale background image
        try:
            self.bg_image = pygame.image.load('images/bg2.png')
            self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
        except pygame.error as e:
            print(f"Unable to load background image: {e}")
            self.bg_image = None  # Set to None or a fallback color if needed

        # Sound settings
        self.high_volume = 1
        self.med_volume = 0.5
        self.low_volume = 0.25
        
        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 6

        # Alien settings
        self.fleet_drop_speed = 5

        # Speed scaling factors
        self.alien_speed_scale = 1.1
        self.ship_speed_scale = 1.05
        self.alien_score_multiplier = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize game's dynamic settings."""
        self.ship_speed_factor = 3.10
        self.bullet_speed_factor = 7.55
        self.alien_speed_factor = 3.4
        self.fleet_direction = 1  # Direction of the alien fleet

    def increase_speed(self):
        """Increment levels speed and scoring."""
        self.ship_speed_factor *= self.ship_speed_scale
        self.bullet_speed_factor *= self.ship_speed_scale
        self.alien_speed_factor *= self.alien_speed_scale
        self.alien_score_multiplier *= 1.5

        # Cap the maximum speeds to prevent excessive values
        self.ship_speed_factor = min(self.ship_speed_factor, Settings.MAX_SPEED)
        self.bullet_speed_factor = min(self.bullet_speed_factor, Settings.MAX_SPEED)
        self.alien_speed_factor = min(self.alien_speed_factor, Settings.MAX_SPEED)
