# Global constants for the game
import pygame
import os

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Tile settings
TILE_SIZE = 32

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Physics
GRAVITY = 0.8
PLAYER_JUMP_FORCE = -16
PLAYER_SPEED = 5
MAX_FALL_SPEED = 12
FRICTION = 0.1

# Game States
STATE_MENU = "MENU"
STATE_PLAYING = "PLAYING"
STATE_PAUSED = "PAUSED"
STATE_GAME_OVER = "GAME_OVER"

# Asset Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

# Image sub-directories
PLAYER_IMG_DIR = os.path.join(IMAGES_DIR, "player")
ENEMY_IMG_DIR = os.path.join(IMAGES_DIR, "enemies")
TILE_IMG_DIR = os.path.join(IMAGES_DIR, "tiles")
BGS_IMG_DIR = os.path.join(IMAGES_DIR, "backgrounds")
UI_IMG_DIR = os.path.join(IMAGES_DIR, "ui")

# Audio sub-directories
SFX_DIR = os.path.join(AUDIO_DIR, "sfx")
MUSIC_DIR = os.path.join(AUDIO_DIR, "music")
