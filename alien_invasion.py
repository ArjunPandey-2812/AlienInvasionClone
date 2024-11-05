import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from menu import Menu
from Ship import Ship

def run_game():
    # Initialize game and create a screen object
    pygame.init()

    ai_settings = Settings()
    stats = GameStats(ai_settings)
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    # Initialize game components
    sb = Scoreboard(ai_settings, screen, stats)
    menu = Menu(ai_settings, screen, stats)

    # Create the ship, bullets, and aliens groups
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create a clock to control the game's frame rate
    clock = pygame.time.Clock()

    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)

        if stats.game_active and not stats.game_paused:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, menu, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, menu)

        # Control the game's frame rate
        clock.tick(ai_settings.fps)

# Run the game
run_game()
