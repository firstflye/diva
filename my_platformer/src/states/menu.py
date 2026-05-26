import pygame
from src.states.base_state import BaseState
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class MenuState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font_big   = pygame.font.SysFont(None, 80)
        self.font_small = pygame.font.SysFont(None, 36)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass  # will switch to playing state in Phase 2

    def update(self, dt):
        pass

    def draw(self, screen):
        title = self.font_big.render("DIVA", True, WHITE)
        prompt = self.font_small.render("Press ENTER to play", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 250))
        screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 370))
