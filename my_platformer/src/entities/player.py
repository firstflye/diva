import pygame
import os
from src.entities.base_entity import BaseEntity
from settings import PLAYER_SPEED, PLAYER_JUMP_FORCE, PLAYER_IMG_DIR

class Player(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32)
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False

        # Animation state
        self.state = "IDLE"
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.15 # seconds per frame

        self.animations = {
            "IDLE": [],
            "RUN_LEFT": [],
            "RUN_RIGHT": [],
            "JUMP": []
        }
        self._load_assets()

    def _load_assets(self):
        # Load IDLE
        idle_sheet = pygame.image.load(os.path.join(PLAYER_IMG_DIR, "IDLE.png")).convert_alpha()
        # Row 0, slice into 32x32
        for i in range(0, idle_sheet.get_width(), 32):
            frame = idle_sheet.subsurface(pygame.Rect(i, 0, 32, 32))
            self.animations["IDLE"].append(frame)

        # Jump uses IDLE frames
        self.animations["JUMP"] = self.animations["IDLE"]

        # Load RUN
        run_sheet = pygame.image.load(os.path.join(PLAYER_IMG_DIR, "RUN.png")).convert_alpha()
        # Row 0, slice into 32x32
        for i in range(0, run_sheet.get_width(), 32):
            frame = run_sheet.subsurface(pygame.Rect(i, 0, 32, 32))
            self.animations["RUN_RIGHT"].append(frame)

        # Mirror RUN_RIGHT for RUN_LEFT
        for frame in self.animations["RUN_RIGHT"]:
            self.animations["RUN_LEFT"].append(pygame.transform.flip(frame, True, False))

    def handle_input(self, input_handler):
        self.velocity_x = 0
        if input_handler.is_pressed(pygame.K_LEFT):
            self.velocity_x = -PLAYER_SPEED
            self.state = "RUN_LEFT"
        elif input_handler.is_pressed(pygame.K_RIGHT):
            self.velocity_x = PLAYER_SPEED
            self.state = "RUN_RIGHT"
        else:
            self.state = "IDLE"

        if input_handler.is_pressed(pygame.K_SPACE) and self.on_ground:
            self.velocity_y = PLAYER_JUMP_FORCE
            self.on_ground = False
            self.state = "JUMP"

    def update(self, dt, physics_system):
        # Update animation state based on physics if not already set by input
        if not self.on_ground:
            self.state = "JUMP"
        elif self.velocity_x == 0 and self.state == "RUN_LEFT" or self.state == "RUN_RIGHT":
            # This is handled by handle_input but for safety
            pass

        # Update animation frame
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.state])

        # Apply gravity
        physics_system.apply_gravity(self, dt)

        # Update position based on velocity
        super().update(dt)

    def draw(self, screen):
        frame = self.animations[self.state][self.frame_index]
        screen.blit(frame, self.rect)
