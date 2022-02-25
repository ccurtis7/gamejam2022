##### INITIALIZATION

# Import Modules
import pygame
import consts
from os import path

# Initialize PyGame
pygame.init()
clock = pygame.time.Clock()

# Initialize game window
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# Initialize the sound mixer
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)

# Load background music
# Idiots In Space by Gundatsch
# URL: https://opengameart.org/content/idiots-in-space
pygame.mixer.music.load(path.join(consts.snd_dir, 'idiotsinspace_low.ogg'))
pygame.mixer.music.play(-1)

# Import Display Module
import display

# Sprite Classes
import spaceship
import asteroid
import explosion

# Sprite Groups
all_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Add Starting Sprites
player = spaceship.Spaceship()
all_sprites.add(player)

# Game parameters
max_asteroids = 5

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
    if keystate[pygame.K_SPACE]:
        player.fire = True

    ##### UPDATE THE GAME STATE
    # Laser hits asteroid
    collisions = pygame.sprite.groupcollide(asteroids, lasers, True, True)
    for thing in collisions:
        boom = explosion.Explosion(thing.rect.centerx, thing.rect.centery, thing.rect.width, 0.9)
        all_sprites.add(boom)
    
    # Asteroid hits spaceship
    collisions = pygame.sprite.spritecollide(player, asteroids, True, pygame.sprite.collide_circle)
    if collisions:
        boom = explosion.Explosion(player.rect.centerx, player.rect.centery, 2*player.rect.width, 0.98)
        all_sprites.add(boom)
        player.hide()
    if player.dead == True and player.cool_down == 0:
        game_active = False

    all_sprites.update()
    
    # Add new laser if allowed
    if player.fire == True and player.cool_down == 0:
        laser = player.shoot()
        all_sprites.add(laser)
        lasers.add(laser)
    # Reset firing flag
    player.fire = False
    
    # Respawn asteroids
    for _ in range(max_asteroids - len(asteroids)):
        new_asteroid = asteroid.Asteroid()
        all_sprites.add(new_asteroid)
        asteroids.add(new_asteroid)
    
    ##### RENDER THE GRAPHICS
    display.draw_background(screen)
    all_sprites.draw(screen)
    display.draw_information(screen)
    
    # Show the new frame
    pygame.display.flip()

# Close the window
pygame.quit()