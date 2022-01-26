import pygame

import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from ship import Ship
from button import Button

def run_game():
    """Initialize game, settings and screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion :)")

    #Create an instance to store game statistics
    stats = GameStats(ai_settings)

    #Make a ship, group of bullets and group of aliens
    ship = Ship(ai_settings, screen, stats)
    bullets = Group()
    aliens = Group()
    
    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        
run_game()