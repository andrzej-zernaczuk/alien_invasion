class Settings():
    """A class to store all settings for Allien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        #Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        #Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 50
        self.bullet_height = 15
        self.bullet_color = (255, 223, 0)
        self.bullets_allowed = 6

        #Alien settings
        self.alien_speed_factor = 0.8
        self.fleet_drop_speed = 10

        #fleet_direction of 1 represents right, -1 left
        self.fleet_direction = 1