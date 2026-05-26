import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.states.menu import MenuState

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Diva")
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_state = MenuState(self)  # ← state loaded here

    def switch_state(self, new_state):
        self.current_state = new_state

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_state.handle_event(event)
            self.current_state.update(dt)
            self.screen.fill((0, 0, 0))
            self.current_state.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
