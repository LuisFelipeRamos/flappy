import pygame

pygame.init()

from utils import *
from modules import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy")

# events
PIPE_SPAWN_DELAY: int = 2_000
PIPE_SPAWN_EVENT: int = pygame.USEREVENT + 1
pygame.time.set_timer(event=PIPE_SPAWN_EVENT, millis=PIPE_SPAWN_DELAY)

# images

YELLOW_BIRD_DOWNFLAP_IMAGE = pygame.image.load("assets/sprites/yellowbird-downflap.png")
YELLOW_BIRD_DOWNFLAP_IMAGE.convert()
YELLOW_BIRD_DOWNFLAP_RECT: pygame.Rect = YELLOW_BIRD_DOWNFLAP_IMAGE.get_rect()

YELLOW_BIRD_MIDFLAP_IMAGE = pygame.image.load("assets/sprites/yellowbird-midflap.png")
YELLOW_BIRD_MIDFLAP_IMAGE.convert()
YELLOW_BIRD_MIDFLAP_RECT: pygame.Rect = YELLOW_BIRD_MIDFLAP_IMAGE.get_rect()

YELLOW_BIRD_UPFLAP_IMAGE = pygame.image.load("assets/sprites/yellowbird-upflap.png")
YELLOW_BIRD_UPFLAP_IMAGE.convert()
YELLOW_BIRD_UPFLAP_RECT: pygame.Rect = YELLOW_BIRD_UPFLAP_IMAGE.get_rect()


def main() -> None:
    clock: pygame.time.Clock = pygame.time.Clock()
    bird: Bird = Bird(name="Dias")
    pipes: list[Pipe] = []
    run: bool = True
    game_started: bool = False
    while run:
        clock.tick(FPS)
        if bird.y_pos > SCREEN_HEIGHT or bird.y_pos < 0:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_started = True
                    bird.set_velocity(velocity=BIRD_VEL0CITY)
            elif event.type == PIPE_SPAWN_EVENT and game_started:
                pipes.append(Pipe())
        SCREEN.fill(BLACK)
        bird.draw(screen=SCREEN)
        if game_started:
            bird.fly()
            for pipe in pipes:
                pipe.move()
                pipe.draw(screen=SCREEN)
            if pipes:
                if pipes[0].is_out_of_bounds():
                    pipes = pipes[1:]
                bird.increment_counter(pipes=pipes)
            if bird.collided(pipes=pipes):
                run = False
                print(f"{bird} died!")
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
