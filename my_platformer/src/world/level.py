import pygame
import json
import os
from settings import TILE_SIZE, TILE_IMG_DIR
from src.world.tilemap import Tilemap

class Level:
    def __init__(self, level_path):
        self.level_path = level_path
        self.tile_images = {}
        self.all_sprites = pygame.sprite.Group()

        self.load_level()

    def load_level(self):
        # 1. Load Level JSON
        with open(self.level_path, 'r') as f:
            level_data = json.load(f)

        grid = level_data['grid']

        # 2. Load and slice tileset
        # Using "Tileset Inside.png" as the primary set
        tileset_path = os.path.join(TILE_IMG_DIR, "Tileset Inside.png")
        tileset = pygame.image.load(tileset_path).convert_alpha()

        # Simple slicing logic: assume tiles are in a row
        # Mapping: 1=GROUND, 2=WALL, 3=PLATFORM, 9=EXIT
        mapping = {
            "GROUND": (0, 32),
            "WALL": (32, 32),
            "PLATFORM": (64, 32),
            "EXIT": (96, 32),
        }

        for type_str, coords in mapping.items():
            rect = pygame.Rect(coords[0], coords[1], TILE_SIZE, TILE_SIZE)
            self.tile_images[type_str] = tileset.subsurface(rect)

        # 3. Instantiate Tilemap
        self.tilemap = Tilemap(grid, self.tile_images)

        # Set up sprite groups
        self.collidables = self.tilemap.get_collidables()
        for tile in self.tilemap.tiles:
            self.all_sprites.add(tile)

        # 4. Player spawn: (1, 7) in tiles -> pixels
        # col 1, row 7
        self.player_spawn = (1 * TILE_SIZE, 7 * TILE_SIZE)

        # 5. Find Exit position
        self.exit_pos = None
        for row_idx, row in enumerate(grid):
            for col_idx, tile_val in enumerate(row):
                if tile_val == 9:
                    self.exit_pos = (col_idx * TILE_SIZE, row_idx * TILE_SIZE)
                    break
            if self.exit_pos:
                break
