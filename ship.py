import pygame

class Ship():
    """A class to store ship."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize the ship and set its starting position."""
        
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        #Load the ship image and get it's rect.
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        
        #Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
       
        self.screen.blit(self.image, self.rect)

    def center_ship(self, stats):
        """Center the ship on the screen and change image."""
        
        self.center = self.screen_rect.centerx

        #Change the ship sprite
        if stats.ships_left == 1:
            self.image = pygame.image.load("images/ship2.png")
        if stats.ships_left == 0:
            self.image = pygame.image.load("images/ship3.png")