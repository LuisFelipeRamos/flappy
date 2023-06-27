import pygame

from utils import *


class Bird:
    def __init__(self) -> None:
        self.x_pos: float = BIRD_INITIAL_X_POS
        self.y_pos: float = BIRD_INITIAL_Y_POS
        self.size: float = BIRD_SIZE
        self.velocity: float = BIRD_VEL0CITY
        self.body: pygame.Rect = pygame.Rect(
            self.x_pos, self.y_pos, self.size, self.size
        )
        self.color: tuple[int] = YELLOW

    def __str__(self) -> str:
        return "Bird"

    def set_velocity(self, velocity: float = BIRD_VEL0CITY) -> None:
        self.velocity = velocity

    def fly(self) -> None:
        self.y_pos -= self.velocity
        self.velocity -= GRAVITY
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.body)
