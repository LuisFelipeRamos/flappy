import pygame
pygame.init()

from utils import *
from modules import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy")


def main():
    
    clock = pygame.time.Clock()
    bird = Bird()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill(BLACK)
        bird.move()
        bird.draw(SCREEN)
        pygame.display.update()
    pygame.quit()

if (__name__ == "__main__"):
    main()