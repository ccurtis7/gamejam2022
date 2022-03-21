# Display Module for Shmup

# Import Modules
import pygame
import consts
from os import path

# Load Background Graphics
background_img = pygame.image.load(path.join(consts.img_dir, 'background.png')).convert()
background = pygame.transform.scale(background_img, (consts.GAME_WIDTH, consts.GAME_HEIGHT))
background_rect = background.get_rect()

# Create Rectangles for Blackout
info_rect = pygame.Rect(consts.GAME_WIDTH, 0, consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
full_screen = pygame.Rect(0, 0, consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)

# Define Font
font_name = pygame.font.match_font('arial')

def draw_text(screen, text, size, x, y):
    # Set the font and font size
    font = pygame.font.Font(font_name, size)

    # Create the image and get the rectangle
    text_surface = font.render(text, True, consts.WHITE)
    text_rect = text_surface.get_rect()

    # Position the text
    text_rect.midtop = (x, y)

    # Display the text
    screen.blit(text_surface, text_rect)

def draw_background(screen):
    screen.blit(background, background_rect)

def draw_information(screen, player):
    # Clear the information area
    pygame.draw.rect(screen, consts.BLACK, info_rect)

    # Game Title and Other Information
    draw_text(screen, "Mediocre Space Shooter", 48, consts.GAME_WIDTH + (consts.WINDOW_WIDTH - consts.GAME_WIDTH) / 2, 10)
    draw_text(screen, "Designed and Programmed by Dr. Wong", 24, consts.GAME_WIDTH + (consts.WINDOW_WIDTH - consts.GAME_WIDTH) / 2, 70)
    draw_text(screen, "for Nevada State Game Jam 2022", 24, consts.GAME_WIDTH + (consts.WINDOW_WIDTH - consts.GAME_WIDTH) / 2, 100)

    # In-Game Information Display
    draw_text(screen, 'Score: {}'.format(player.score), 36, consts.GAME_WIDTH + (consts.WINDOW_WIDTH - consts.GAME_WIDTH) / 2, 300)
    draw_text(screen, 'Lives: {}'.format(player.lives), 36, consts.GAME_WIDTH + (consts.WINDOW_WIDTH - consts.GAME_WIDTH) / 2, 350)
    draw_text(screen, 'Level: {}'.format(player.level), 36, consts.GAME_WIDTH + (consts.WINDOW_WIDTH - consts.GAME_WIDTH) / 2, 400)

def draw_health_bar(screen, pct):
    # Avoid negative values
    if pct < 0:
        pct = 0

    # Calculate the parameters for the health bar
    BAR_LENGTH = (consts.GAME_WIDTH / 12) * 10
    BAR_HEIGHT = 10
    x = int(consts.GAME_WIDTH / 12)
    y = consts.GAME_HEIGHT - 15
    fill = (pct / 100) * BAR_LENGTH

    # Select the color of the health bar
    if pct > 70:
        COLOR = consts.GREEN
    elif pct > 40:
        COLOR = consts.YELLOW
    else:
        COLOR = consts.RED

    # Draw the health bar
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, COLOR, fill_rect)
    pygame.draw.rect(screen, consts.WHITE, outline_rect, 2)

def draw_splash(screen, last_score, high_score):
    pygame.draw.rect(screen, consts.BLACK, full_screen)
    draw_text(screen, "Medicore Space Shooter", 96, consts.WINDOW_WIDTH / 2, 10)
    draw_text(screen, "Designed and Programmed by Dr. Wong", 48, consts.WINDOW_WIDTH / 2, 120)
    draw_text(screen, "for Nevada State Game Jam 2022", 48, consts.WINDOW_WIDTH / 2, 170)
    draw_text(screen, "https://github.com/ccurtis7/gamejam2022/", 48, consts.WINDOW_WIDTH / 2, 220)

    draw_text(screen, "Use the arrow keys to move left and right", 36, consts.WINDOW_WIDTH / 2, 300)
    draw_text(screen, "Hold the space bar to shoot", 36, consts.WINDOW_WIDTH / 2, 350)
    draw_text(screen, "Press any key to begin", 36, consts.WINDOW_WIDTH / 2, 400)

    draw_text(screen, "Last score: {}".format(last_score), 36, consts.WINDOW_WIDTH / 2, 500)
    draw_text(screen, "High score: {}".format(high_score), 36, consts.WINDOW_WIDTH / 2, 550)
