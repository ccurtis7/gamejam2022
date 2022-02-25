# Display Module for Shmup

# Import Modules
import pygame
import consts
from os import path

# Load Background Graphics
background_img = pygame.image.load(path.join(consts.img_dir, 'background.png')).convert()
background = pygame.transform.scale(background_img, (consts.GAME_WIDTH, consts.GAME_HEIGHT))
background_rect = background.get_rect()

def draw_background(screen):
    screen.blit(background, background_rect)