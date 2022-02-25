##### INITIALIZATION

# Import Modules
import pygame

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960

BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Initialize PyGame
pygame.init()

# Initialize game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Initialize Rectangles
rect1 = pygame.Rect(50, 100, 200, 300) # Absolute Coordinates
rect2 = pygame.Rect(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                    WINDOW_WIDTH / 4, WINDOW_WIDTH / 5) # Relative Coordinates

##### GAME LOOP
game_active = True

while game_active:
    ##### READ USER INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Request to close window
            game_active = False

    ##### UPDATE THE GAME STATE
    
    
    ##### RENDER THE GRAPHICS
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)
    
    # Show the new frame
    pygame.display.flip()

# Close the window
pygame.quit()