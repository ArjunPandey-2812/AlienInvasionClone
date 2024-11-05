import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # Load the ship image outside the class to prevent reloading
    ship_image = pygame.image.load('images/ship.bmp')

    def __init__(self, ai_settings, screen):
        """ Initialize the ship and its starting position. """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = Ship.ship_image  # Use the class variable
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value of the ship's center
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the ship's position based on the movement flags. """
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.centery += self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center
        self.rect.centery = self.centery

        # Check boundaries to keep the ship on screen
        self.check_boundaries()

    def check_boundaries(self):
        """ Ensure the ship stays within the screen boundaries. """
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def center_ship(self):
        """ Center the ship at the bottom center of the screen. """
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ Draw the ship at its current position. """
        self.screen.blit(self.image, self.rect)
