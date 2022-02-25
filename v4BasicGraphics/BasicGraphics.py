##### INITIALIZATION

# Import Modules
import pygame
from os import path

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960

GAME_WIDTH = 720
GAME_HEIGHT = 960

BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Directories
img_dir = path.join(path.dirname(__file__), 'img')

# Initialize PyGame
pygame.init()

# Initialize game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Load Graphics
background_img = pygame.image.load(path.join(img_dir, 'background.png')).convert()

spaceship_img = pygame.image.load(path.join(img_dir, 'spaceship.png')).convert()
spaceship_img.set_colorkey(BLACK)

# Set up background image
background = pygame.transform.scale(background_img, (GAME_WIDTH, GAME_HEIGHT))
background_rect = background.get_rect()

# Sprite Classes
class Spaceship(pygame.sprite.Sprite):
    # Sprite Class Initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.image = spaceship_img
        self.rect = self.image.get_rect()
        
        # Define the sprite's location
        self.rect.centerx = GAME_WIDTH / 2
        self.rect.bottom = GAME_HEIGHT - 20
        
# Sprite Groups
all_sprites = pygame.sprite.Group()

# Add Starting Sprites
player = Spaceship()
all_sprites.add(player)

##### GAME LOOP
game_active = True

while game_active:
    ##### READ USER INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Request to close window
            game_active = False

    ##### UPDATE THE GAME STATE
    
    
    ##### RENDER THE GRAPHICS
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    # Show the new frame
    pygame.display.flip()

# Close the window
pygame.quit()