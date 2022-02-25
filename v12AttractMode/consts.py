# Constants for Shmup

# Import Modules
from os import path

# Game window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960

GAME_WIDTH = 720
GAME_HEIGHT = 960

# Game Speed
FPS = 60

# Basic Colors (RGB) - These are the names of colors based on common HTML usage
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

MAROON = (128, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
NAVY = (0, 0, 128)
BLUE = (0, 0, 255)

OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
FUCHSIA = (255, 0, 255)
TEAL = (0, 128, 128)
AQUA = (0, 255, 255)

# Directories
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')