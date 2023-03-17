import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the game window size
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Allowed Characters Example")

# Set the allowed characters (only accept lowercase and uppercase letters)
allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Check if the key is an allowed character
            if event.unicode in allowed_characters:
                print("Pressed character:", event.unicode)

    # Refresh the screen
    pygame.display.flip()
