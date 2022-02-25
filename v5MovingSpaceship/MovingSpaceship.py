##### INITIALIZATION

# Import Modules
import pygame
from os import path

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960

GAME_WIDTH = 720
GAME_HEIGHT = 960

FPS = 60

BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Directories
img_dir = path.join(path.dirname(__file__), 'img')

# Initialize PyGame
pygame.init()
clock = pygame.time.Clock()

# Initialize game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Load Graphics
background_img = pygame.image.load(path.join(img_dir, 'background.png')).convert()

spaceship_img_1 = pygame.image.load(path.join(img_dir, 'spaceship_1.png')).convert()
spaceship_img_1.set_colorkey(BLACK)

spaceship_img_2 = pygame.image.load(path.join(img_dir, 'spaceship_2.png')).convert()
spaceship_img_2.set_colorkey(BLACK)

# Set up background image
background = pygame.transform.scale(background_img, (GAME_WIDTH, GAME_HEIGHT))
background_rect = background.get_rect()

# Sprite Classes
class Spaceship(pygame.sprite.Sprite):
    # Sprite Class Initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.image = spaceship_img_1
        self.rect = self.image.get_rect()
        
        self.animation = [spaceship_img_1, spaceship_img_2]
        
        # Define the sprite's location
        self.rect.centerx = GAME_WIDTH / 2
        self.rect.bottom = GAME_HEIGHT - 20
        
        # Define attributes
        self.speed = 5
        self.animation_frame = 0
        self.frame_count = 0
        
        # Set flags
        self.left = False
        self.right = False
    
    def update(self):
        # Update frame_count
        self.frame_count += 1
        
        # Animate the spaceship
        if self.frame_count % 30 == 0:
            self.animation_frame = (self.animation_frame + 1) % len(self.animation)
            self.image = self.animation[self.animation_frame]
        
        # Adjust player position
        if self.left == True:
            self.rect.x += -self.speed
        if self.right == True:
            self.rect.x += self.speed
        
        # Check for wall collisions
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= GAME_WIDTH:
            self.rect.right = GAME_WIDTH
        
        # Reset Flags
        self.left = False
        self.right = False

# Sprite Groups
all_sprites = pygame.sprite.Group()

# Add Starting Sprites
player = Spaceship()
all_sprites.add(player)

##### GAME LOOP
game_active = True

while game_active:
    clock.tick(FPS) # Control Game speed
    
    ##### READ USER INPUT
    
    # Check events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT: # Request to close window
            game_active = False
    
    # Check which keys are down
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        player.left = True
    if keystate[pygame.K_RIGHT]:
        player.right = True


    ##### UPDATE THE GAME STATE
    all_sprites.update()
    
    ##### RENDER THE GRAPHICS
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    # Show the new frame
    pygame.display.flip()

# Close the window
pygame.quit()