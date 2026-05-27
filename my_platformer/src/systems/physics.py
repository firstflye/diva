import pygame
from settings import GRAVITY, MAX_FALL_SPEED

class PhysicsSystem:
    def __init__(self):
        pass

    def apply_gravity(self, entity, dt):
        entity.velocity_y += GRAVITY * dt * 60
        if entity.velocity_y > MAX_FALL_SPEED:
            entity.velocity_y = MAX_FALL_SPEED

    def resolve_collision(self, entity, obstacle):
        # Basic AABB collision resolution
        if entity.rect.colliderect(obstacle.rect):
            # This is a very simple resolution, needs improvement
            # Find overlap on each axis
            overlap_x = min(entity.rect.right, obstacle.rect.right) - max(entity.rect.left, obstacle.rect.left)
            overlap_y = min(entity.rect.bottom, obstacle.rect.bottom) - max(entity.rect.top, obstacle.rect.top)

            if overlap_x < overlap_y:
                if entity.rect.centerx < obstacle.rect.centerx:
                    entity.rect.right = obstacle.rect.left
                else:
                    entity.rect.left = obstacle.rect.right
                entity.velocity_x = 0
            else:
                if entity.rect.centery < obstacle.rect.centery:
                    entity.rect.bottom = obstacle.rect.top
                    entity.velocity_y = 0
                    entity.on_ground = True
                else:
                    entity.rect.top = obstacle.rect.bottom
                    entity.velocity_y = 0

    def resolve_collisions(self, entity, collidables):
        collided_sprites = pygame.sprite.spritecollide(entity, collidables, False)
        for obstacle in collided_sprites:
            self.resolve_collision(entity, obstacle)
