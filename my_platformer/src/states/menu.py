import pygame
from src.states.base_state import BaseState
from src.states.playing import PlayingState
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class MenuState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font_big   = pygame.font.Font(None, 80)
        self.font_small = pygame.font.Font(None, 36)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.switch_state(PlayingState(self.game))

    def update(self, dt):
        pass

    def draw(self, screen):
        title = self.font_big.render("DIVA", True, WHITE)
        prompt = self.font_small.render("Press ENTER to play", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 250))
        screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 370))
