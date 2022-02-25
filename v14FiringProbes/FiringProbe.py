##### INITIALIZATION

# Import Modules
import pygame
import consts
from os import path
import random

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
import probe

# Sprite Groups
all_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
probes = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Score memory
high_score = 0
last_score = 0

##### GAME LOOP
game_active = True
attract_mode = True
game_over = False

while game_active:
    clock.tick(consts.FPS) # Control Game speed
    if attract_mode:
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Request to close window
                game_active = False
            elif event.type == pygame.KEYDOWN: # Start new game
                attract_mode = False
                
                # Clean up existing sprites
                for thing in all_sprites:
                    thing.kill()
                
                # Add Starting Sprites
                player = spaceship.Spaceship()
                all_sprites.add(player)

                # New Game parameters
                max_asteroids = 5
                max_probes = 3
                
                # Add probes
                for i in range(max_probes):
                    new_probe = probe.Probe(player, i)
                    all_sprites.add(new_probe)
                    enemies.add(new_probe)
                    probes.add(new_probe)
        
        # Show attract screen
        display.draw_splash(screen, last_score, high_score)
        pygame.display.flip()
    else: # Game Mode
        ##### READ USER INPUT
        
        # Check events
        for event in pygame.event.get():
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
        # Laser hits enemy
        collisions = pygame.sprite.groupcollide(enemies, lasers, True, True)
        for thing in collisions:
            boom = explosion.Explosion(thing.rect.centerx, thing.rect.centery, thing.rect.width, 0.9)
            all_sprites.add(boom)
            player.score += int(thing.rect.width)
        
        # Enemy hits spaceship
        collisions = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
        for thing in collisions:
            boom = explosion.Explosion(thing.rect.centerx, thing.rect.centery, thing.rect.width, 0.9)
            all_sprites.add(boom)
            player.shield += -0.5 * thing.rect.width
        if player.shield <= 0 and player.dead == False:
            boom = explosion.Explosion(player.rect.centerx, player.rect.centery, 2*player.rect.width, 0.98)
            all_sprites.add(boom)
            player.hide()
        if player.dead == True and player.cool_down == 0:
            if player.lives > 0:
                player.unhide()
            else: # Game over
                attract_mode = True
                last_score = player.score
                high_score = max(high_score, last_score)
    
        all_sprites.update()
        
        # Add new laser if allowed
        if player.dead == False and player.fire == True and player.cool_down == 0:
            laser = player.shoot()
            all_sprites.add(laser)
            lasers.add(laser)
        # Reset firing flag
        player.fire = False
        
        # Respawn asteroids
        for _ in range(max_asteroids - len(asteroids)):
            new_asteroid = asteroid.Asteroid()
            all_sprites.add(new_asteroid)
            enemies.add(new_asteroid)
            asteroids.add(new_asteroid)
        
        # Probes fire energy particles
        for thing in probes:
            if thing.fire == True and player.dead == False:
                ep = probe.EnergyParticle(player, thing)
                all_sprites.add(ep)
                enemies.add(ep)
                thing.fire = False
                thing.cool_down = random.randint(60, max(300 - 10 * player.level, 100))
        
        # Increase level if all the probes are destroyed
        if len(probes) == 0:
            player.level += 1
            max_probes += 1
            max_asteroids += 1
            
            # Add probes
            for i in range(max_probes):
                new_probe = probe.Probe(player, i)
                all_sprites.add(new_probe)
                enemies.add(new_probe)
                probes.add(new_probe)
        
        ##### RENDER THE GRAPHICS
        display.draw_background(screen)
        all_sprites.draw(screen)
        if player.dead == False:
            display.draw_health_bar(screen, player.shield)
        display.draw_information(screen, player)
        
        # Show the new frame
        pygame.display.flip()

# Close the window
pygame.quit()