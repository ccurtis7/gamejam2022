# Asteroid Module for Shmup

# Import Modules
import pygame
import consts
import random
from os import path

# Load Graphics
asteroid_images = []
asteroid_list = ['asteroid_big.png', 'asteroid_small.png']
for img in asteroid_list:
    asteroid = pygame.image.load(path.join(consts.img_dir, img)).convert()
    asteroid.set_colorkey(consts.BLACK)
    asteroid_images.append(asteroid)

class Asteroid(pygame.sprite.Sprite):
    # Sprite class initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.asteroid = random.choice(asteroid_images)
        
        self.image = self.asteroid
        self.rect = self.image.get_rect()

        # Define the sprite's location
        self.rect.bottom = -20
        self.rect.centerx = random.randint(0, consts.GAME_WIDTH)

        # Define attributes
        self.angle = 0
        self.spinspeed = (-1)^random.randint(1,2) * random.randint(1,5)
        self.speedx = random.randint(-10,10)
        self.speedy = random.randint(10,15)
        self.radius = self.rect.width * 0.4

    def update(self):
        # Determine the new position
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Set the new rotation
        self.angle += self.spinspeed
        
        # Update and recenter the image
        new_image = pygame.transform.rotate(self.asteroid, self.angle)
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center

        # Kill the asteroid if it's too far off screen
        if True in (self.rect.top > consts.GAME_HEIGHT + 50, self.rect.right < -20, self.rect.left > consts.GAME_WIDTH + 20):
            self.kill()