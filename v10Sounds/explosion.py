# Explosion Module for Shmup

# Import Modules
import pygame
import consts
from os import path

# Load Graphics
explosion = pygame.image.load(path.join(consts.img_dir, 'Explosion.png')).convert()
explosion.set_colorkey(consts.BLACK)

# Load Sounds
short_explosion = pygame.mixer.Sound(path.join(consts.snd_dir, 'short_boom.wav'))
long_explosion = pygame.mixer.Sound(path.join(consts.snd_dir, 'long_boom.wav'))

class Explosion(pygame.sprite.Sprite):
    # Sprite class initialization
    def __init__(self, x, y, size, decay_rate):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.image = pygame.transform.scale(explosion, (size, size))
        self.rect = self.image.get_rect()

        # Define the sprite's location
        self.rect.centerx = x
        self.rect.centery = y

        # Define attributes
        self.alpha = 255
        self.decay_rate = decay_rate
        
        if decay_rate < 0.95:
            short_explosion.play()
        else:
            long_explosion.play()

    def update(self):
        # Fade out the image
        self.alpha = int(self.decay_rate * self.alpha)
        self.image.set_alpha(self.alpha)
        
        # Destroy the sprite when transparent
        if self.alpha < 1:
            self.kill()
