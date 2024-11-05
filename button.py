import pygame.font

class Button():
    """A class to create a button for the game interface."""

    def __init__(self, ai_settings, screen, stats, msg=''):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (90, 200, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # Customize the font if needed

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.rect.center[1]

        # Initialize button message
        self.msg = msg
        self.prep_msg(stats)

    def prep_text(self, stats):
        """Prepare the text for the menu button based on the state of the game."""
        if not stats.game_active and not stats.game_paused and not stats.game_ended:
            self.msg = 'Play!'
        elif stats.game_active and stats.game_paused:
            self.msg = 'Resume'
        elif stats.game_ended:
            self.msg = 'Try Again!'

    def prep_msg(self, stats):
        """Turn msg into a rendered image and center text on the button."""
        self.prep_text(stats)  # Update the message based on game state
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, stats):
        """Draw the button with its current message."""
        self.prep_msg(stats)  # Refresh the message each time the button is drawn
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def clicked(self, mouse_pos):
        """Return True if the button is clicked."""
        return self.rect.collidepoint(mouse_pos)

    def update_button_state(self, active=True):
        """Enable or disable the button."""
        self.active = active
        self.button_color = (90, 200, 30) if active else (200, 30, 30)  # Example color change when inactive
