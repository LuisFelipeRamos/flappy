import pygame

pygame.init()

from utils import *
from modules import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy")

# events
PIPE_SPAWN_DELAY: int = 3_000
PIPE_SPAWN_EVENT: pygame.event.Event = pygame.USEREVENT + 1
pygame.time.set_timer(event=PIPE_SPAWN_EVENT, millis=PIPE_SPAWN_DELAY)


def main() -> None:
    clock: pygame.time.Clock = pygame.time.Clock()
    bird: Bird = Bird(name="Dias")
    pipes: list[Pipe] = []
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
                    bird.set_velocity(velocity=BIRD_VEL0CITY)
            elif event.type == PIPE_SPAWN_EVENT:
                pipes.append(Pipe())
        SCREEN.fill(BLACK)
        bird.fly()
        bird.draw(screen=SCREEN)
        for pipe in pipes:
            pipe.move()
            pipe.draw(screen=SCREEN)
        if bird.collided(
            objects=[
                pipe.upper_body for pipe in pipes
            ]  # there is probabily a better way of doing this
            + [pipe.lower_buddy for pipe in pipes]
        ):
            run = False
            print(f"{bird} died!")
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
