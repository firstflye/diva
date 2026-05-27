import os
os.environ.setdefault("SDL_VIDEODRIVER", "x11")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame
pygame.init()

from src.game import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
