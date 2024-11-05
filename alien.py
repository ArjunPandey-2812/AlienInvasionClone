import pygame
from pygame.sprite import Sprite
from random import choice

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    # Preload the alien images and points
    alien_images = {
        'images/ufo1.bmp': 150,
        'images/ufo2.bmp': 100,
        'images/ufo3.bmp': 200
    }
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Set a random image and points for the alien
        self.image, self.points = self.get_color()
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def get_color(self):
        """Set a random color for the alien and determine its points."""
        alien_color = choice(list(self.alien_images.keys()))
        self.image = pygame.image.load(alien_color)
        return self.image, self.alien_images[alien_color]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    # Optional: Add collision handling method
    def handle_collision(self, bullets):
        """Handle collision with bullets and remove the alien."""
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                bullet.kill()  # Remove the bullet
                self.kill()    # Remove the alien
                break
