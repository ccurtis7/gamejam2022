##### INITIALIZATION

# Import Modules
import pygame
import consts

# Initialize PyGame
pygame.init()
clock = pygame.time.Clock()

# Initialize game window
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# Import Display Module
import display

# Sprite Classes
import spaceship

# Sprite Groups
all_sprites = pygame.sprite.Group()

# Add Starting Sprites
player = spaceship.Spaceship()
all_sprites.add(player)

##### GAME LOOP
game_active = True

while game_active:
    clock.tick(consts.FPS) # Control Game speed

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
    display.draw_background(screen)
    all_sprites.draw(screen)

    # Show the new frame
    pygame.display.flip()

# Close the window
pygame.quit()
