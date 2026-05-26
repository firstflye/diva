import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.states = {}
        self.current_state = None

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(FPS)

        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        if self.current_state:
            self.current_state.update()

    def _draw(self):
        self.screen.fill((0, 0, 0)) # Fill screen with black
        if self.current_state:
            self.current_state.draw(self.screen)
        pygame.display.flip()
