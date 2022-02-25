# Spaceship Module for Shmup

# Import Modules
import pygame
import consts
from os import path

# Load graphics
spaceship_img_1 = pygame.image.load(path.join(consts.img_dir, 'spaceship_1.png')).convert()
spaceship_img_1.set_colorkey(consts.BLACK)

spaceship_img_2 = pygame.image.load(path.join(consts.img_dir, 'spaceship_2.png')).convert()
spaceship_img_2.set_colorkey(consts.BLACK)

class Spaceship(pygame.sprite.Sprite):
    # Sprite Class Initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.image = spaceship_img_1
        self.rect = self.image.get_rect()
        
        self.animation = [spaceship_img_1, spaceship_img_2]
        
        # Define the sprite's location
        self.rect.centerx = consts.GAME_WIDTH / 2
        self.rect.bottom = consts.GAME_HEIGHT - 20
        
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
        if self.rect.right >= consts.GAME_WIDTH:
            self.rect.right = consts.GAME_WIDTH
        
        # Reset Flags
        self.left = False
        self.right = False
    
