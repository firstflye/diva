import pygame

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self, dt):
        self.rect.x += self.velocity_x * dt * 60
        self.rect.y += self.velocity_y * dt * 60

    def draw(self, screen):
        pass
