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

#-----#
# To make longer animations, repeat the pattern above to load all the animations.
# You will also need to change the self.animation line in the Probe class below.
# To control the speed of the animation, you'll need to edit the update() method.
#
# For example...
# spaceship_img_3 = pygame.image.load(path.join(consts.img_dir, 'spaceship_3.png')).convert()
# spaceship_img_3.set_colorkey(consts.BLACK)
#-----#

# Load Sounds
#-----#
# To change the laser sound, place your sound file in the snd directory
# and change the name of the file in the command below.
shoot_sound = pygame.mixer.Sound(path.join(consts.snd_dir, 'laser.wav'))
#-----#

class Spaceship(pygame.sprite.Sprite):
    # Sprite Class Initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.image = spaceship_img_1
        self.rect = self.image.get_rect()
        
        #-----#
        # If you added extra animation frames, you'll need to make this list longer.
        self.animation = [spaceship_img_1, spaceship_img_2]
        #-----#
        
        # Define the sprite's location
        self.rect.centerx = consts.GAME_WIDTH / 2
        self.rect.bottom = consts.GAME_HEIGHT - 20
        
        # Define attributes
        self.speed = 5
        self.animation_frame = 0
        self.frame_count = 0
        self.cool_down = 0
        self.radius = self.rect.width * 0.4
        
        # Set flags
        self.left = False
        self.right = False
        self.fire = False
        self.dead = False

        # Game information
        self.score = 0
        self.lives = 3
        self.level = 1
        self.shield = 100
    
    def update(self):
        # Update frame_count
        self.frame_count += 1
        
        # Update cool_down
        if self.cool_down > 0:
            self.cool_down += -1
        
        # Animate the spaceship
        #-----#
        # The number after the % sign controls how many frames will pass before going to the next
        # image in the animation. The game runs at 60 frames per second.
        if self.frame_count % 30 == 0: #-----#
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
    
    def shoot(self):
        laser = Laser(self)
        self.cool_down = 12
        shoot_sound.play()
        return(laser)
    
    def hide(self):
        self.dead = True
        self.rect.y = -200
        self.cool_down = 200
        self.lives += -1

    def unhide(self):
        self.dead = False
        self.rect.centerx = consts.GAME_WIDTH / 2
        self.rect.bottom = consts.GAME_HEIGHT - 20
        self.shield = 100
    

class Laser(pygame.sprite.Sprite):
    # Sprite Class Initialization
    def __init__(self, spaceship):
        pygame.sprite.Sprite.__init__(self)

        # Set up the graphics
        self.image = pygame.Surface((6,25))
        self.image.fill(consts.YELLOW)
        self.rect = self.image.get_rect()
        
        # Define the sprite's location
        self.rect.bottom = spaceship.rect.top
        self.rect.centerx = spaceship.rect.centerx
        
        # Define parameters
        self.speed = -15

    def update(self):
        # Update the position of the laser
        self.rect.y += self.speed
        
        # Destroy the laser when it goes off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
        

        