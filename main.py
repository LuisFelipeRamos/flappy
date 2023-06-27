import pygame

pygame.init()

from utils import *
from modules import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy")


def main():
    clock: pygame.time.Clock = pygame.time.Clock()
    bird: Bird = Bird()
    run: bool = True
    while run:
        clock.tick(FPS)
        if bird.y_pos > SCREEN_HEIGHT or bird.y_pos < 0:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.is_flying = True
        SCREEN.fill(BLACK)
        bird.fly()
        bird.draw(SCREEN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
