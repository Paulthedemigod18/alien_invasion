import sys
import pygame
from settings import Settings

class BlueSkyGame:
    """Class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        # Initialize game settings
        self.settings = Settings()

        # Create the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky Game")

    def run_game(self):
        """Start the main game loop."""
        while True:
            # Handle events such as quitting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen with the background color
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Create an instance of the game and run it
    blue_sky_game = BlueSkyGame()
    blue_sky_game.run_game()
