import pygame
from settings import TILE_SIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type, image=None):
        super().__init__()
        self.tile_type = tile_type
        if image:
            self.image = image
        else:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            colors = {
                "GROUND": (100, 100, 100),
                "WALL": (50, 50, 50),
                "PLATFORM": (150, 150, 150),
                "EXIT": (0, 255, 0),
                "GAP": (0, 0, 0)
            }
            self.image.fill(colors.get(tile_type, (255, 0, 255)))
        self.rect = self.image.get_rect(topleft=(x, y))

    def is_solid(self):
        return self.tile_type in ["GROUND", "WALL", "PLATFORM"]

class Tilemap:
    def __init__(self, data, tile_images=None):
        self.data = data
        self.tile_images = tile_images or {}
        self.tiles = []
        self.collidables = pygame.sprite.Group()
        self._build_map()

    def _build_map(self):
        for row_index, row in enumerate(self.data):
            for col_index, tile_type in enumerate(row):
                if tile_type == "GAP" or tile_type == 0:
                    continue

                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                # Handle both string and int tile types
                type_str = str(tile_type)
                if tile_type == 1: type_str = "GROUND"
                elif tile_type == 2: type_str = "WALL"
                elif tile_type == 3: type_str = "PLATFORM"
                elif tile_type == 9: type_str = "EXIT"

                image = self.tile_images.get(type_str)
                tile = Tile(x, y, type_str, image)
                self.tiles.append(tile)

                if tile.is_solid():
                    self.collidables.add(tile)

    def render(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

    def get_collidables(self):
        return self.collidables
