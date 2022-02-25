# Asteroid Module for Shmup

# Import Modules
import pygame
import consts
import random
from os import path
from math import sqrt

# Load Graphics
probe_img_1 = pygame.image.load(path.join(consts.img_dir, 'probe_1.png')).convert()
probe_img_1.set_colorkey(consts.BLACK)

probe_img_2 = pygame.image.load(path.join(consts.img_dir, 'probe_2.png')).convert()
probe_img_2.set_colorkey(consts.BLACK)

energy_particle_img = pygame.image.load(path.join(consts.img_dir, 'energy.png')).convert()
energy_particle_img.set_colorkey(consts.BLACK)

class Probe(pygame.sprite.Sprite):
    # Sprite class initialization
    def __init__(self, player, probe_num):
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the graphics
        self.image = probe_img_1
        self.rect = self.image.get_rect()
        
        self.animation = [probe_img_1, probe_img_2]
        
        # Load Sprite Movement Pattern
        num_patterns = 3
        pattern = (player.level - 1) % num_patterns
        if pattern == 0:
            self.path = [[50, 50], [consts.GAME_WIDTH - 50, 50], [consts.GAME_WIDTH - 50, 100], [50, 100], [50, 150], [consts.GAME_WIDTH - 50, 150], [consts.GAME_WIDTH - 50, 200], [50, 200], [50, 150], [consts.GAME_WIDTH - 50, 150], [consts.GAME_WIDTH - 50, 100], [50, 100]]
            self.start = [-50 - 100 * probe_num, 50]
        elif pattern == 1:
            self.path = [[-50, 50], [consts.GAME_WIDTH + 50, 250], [consts.GAME_WIDTH + 50, 50], [-50, 250]]
            self.start = [-50 - 100 * probe_num, 50]
        elif pattern == 2:
            self.path = [ [random.randint(50, consts.GAME_WIDTH - 50), random.randint(50, 300)] for _ in range(20)]
            self.start = [random.randint(50,consts.GAME_WIDTH), -50]

        # Define the sprite's location
        self.rect.centerx = self.start[0]
        self.rect.centery = self.start[1]
        
        # Define graphical attributes
        self.animation_frame = 0
        self.frame_count = 0
        
        # Define movement parameters
        self.speed = min(5 + player.level, 25)

        self.lastpoint = -1
        self.movementframe = 0
        self.movefrom = self.start
        self.moveto = self.path[0]
        self.movementsteps = self.calculate_steps(self.movefrom, self.moveto, self.speed)
        
        # Define firing attributes
        if player.level > num_patterns:
            self.cool_down = random.randint(60, max(300 - 10 * player.level, 100))
        else:
            self.cool_down = -1
        self.fire = False

    def update(self):
        # Update parameters
        self.frame_count += 1
        self.movementframe += 1
        self.cool_down += -1

        # Update animation
        if self.frame_count % 10 == 0:
            self.animation_frame = (self.animation_frame + 1) % len(self.animation)
            self.image = self.animation[self.animation_frame]

        # Calculate the new position
        self.rect.centerx, self.rect.centery = self.calculate_position(self.movefrom, self.moveto, self.movementframe, self.movementsteps)
        
        # Calculate the next movement after the current movement is complete
        if self.movementframe == self.movementsteps:
            self.lastpoint = (self.lastpoint + 1) % len(self.path)
            self.movefrom = self.path[self.lastpoint]
            self.moveto = self.path[(self.lastpoint + 1) % len(self.path)]
            self.movementsteps = self.calculate_steps(self.movefrom, self.moveto, self.speed)
            self.movementframe = 0
        
        if self.cool_down == 0:
            self.fire = True
        
    def calculate_steps(self, start, stop, speed):
        return(int((sqrt((stop[0] - start[0])**2 + (stop[1] - start[1])**2))/speed) + 1)
    
    def calculate_position(self, start, stop, step, max_steps):
        x = start[0] + (stop[0] - start[0]) * step/max_steps
        y = start[1] + (stop[1] - start[1]) * step/max_steps
        return (x, y)

class EnergyParticle(pygame.sprite.Sprite):    
    # Sprite class initialization
    def __init__(self, player, probe):
        pygame.sprite.Sprite.__init__(self)

        # Set up the graphics
        self.image = energy_particle_img
        self.rect = self.image.get_rect()

        # Calculate the targeting
        self.startx = probe.rect.centerx
        self.starty = probe.rect.centery
        self.targetx = player.rect.centerx
        self.targety = player.rect.centery

        # Define the sprite's location
        self.rect.centerx = probe.rect.centerx
        self.rect.centery = probe.rect.centery
        
        # Define parameters
        self.speedy = random.randint(3, min(5 + player.level, 25))
        self.frame_count = 0

    def update(self):
        # Update parameters
        self.frame_count += 1
        
        # Calculate new position
        self.rect.centerx = self.startx + (self.targetx - self.startx) * self.frame_count * self.speedy / (self.targety - self.starty)
        self.rect.centery = self.starty + self.frame_count * self.speedy
        
        if self.rect.top > consts.GAME_HEIGHT + 50:
            self.kill()
