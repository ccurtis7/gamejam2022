##### INITIALIZATION

# Import Modules
import pygame

# Initialize PyGame
pygame.init()

# Initialize game window
screen = pygame.display.set_mode((1280, 960))

##### MAIN PROGRAM

# Loop until the window is closed
window_open = True

while window_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Request to close window
            window_open = False

# Close the window
pygame.quit()