import pygame

from utils import *
from .pipe import Pipe


class Bird:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.x_pos: float = BIRD_INITIAL_X_POS
        self.y_pos: float = BIRD_INITIAL_Y_POS
        self.size: float = BIRD_SIZE
        self.velocity: float = BIRD_VEL0CITY
        self.body: pygame.Rect = pygame.Rect(
            self.x_pos, self.y_pos, self.size, self.size
        )
        self.color: tuple[int,int, int] = YELLOW
        self.counter: int = 0

    def __str__(self) -> str:
        return f"{self.name}"

    def set_velocity(self, velocity: float = BIRD_VEL0CITY) -> None:
        self.velocity = velocity

    def fly(self) -> None:
        self.y_pos -= self.velocity
        self.velocity -= GRAVITY
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def increment_counter(self, pipes: list[Pipe]) -> None:
        for pipe in pipes:
            if self.x_pos >= pipe.upper_body.x and not pipe.counted:
                pipe.counted = True
                self.counter += 1

    def collided(self, pipes: list[Pipe]) -> bool:
        pipes_bodies: list[pygame.Rect] = [pipe.upper_body for pipe in pipes] + [
            pipe.lower_body for pipe in pipes
        ]
        return self.body.collidelist(pipes_bodies) != -1

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.body)
