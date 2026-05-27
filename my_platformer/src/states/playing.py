import pygame
from src.states.base_state import BaseState
from src.entities.player import Player
from src.systems.input_handler import InputHandler
from src.systems.physics import PhysicsSystem
from src.world.level import Level
from settings import SCREEN_HEIGHT

class PlayingState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.level = Level("levels/level_01.json")
        self.player = Player(*self.level.player_spawn)
        self.input_handler = InputHandler()
        self.physics_system = PhysicsSystem()

    def handle_event(self, event):
        # State-specific event handling (e.g., pause game)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Will implement pause state later
                pass

    def update(self, dt):
        self.input_handler.update()
        self.player.handle_input(self.input_handler)
        self.player.update(dt, self.physics_system)

        # Resolve collisions with solid tiles
        self.physics_system.resolve_collisions(self.player, self.level.collidables)

        # Check for EXIT tile contact
        for tile in self.level.tilemap.tiles:
            if tile.tile_type == "EXIT" and self.player.rect.colliderect(tile.rect):
                print("EXIT REACHED")
                break

        # Check for GAP fall
        if self.player.rect.top > SCREEN_HEIGHT:
            self.player.rect.topleft = self.level.player_spawn
            self.player.velocity_x = 0
            self.player.velocity_y = 0

    def draw(self, screen):
        screen.fill((135, 206, 235))  # Sky blue
        self.level.all_sprites.draw(screen)
        self.player.draw(screen)
