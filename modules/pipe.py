import pygame

from utils import *


class Pipe:
    def __init__(self) -> None:
        self.width: float = PIPE_WIDTH
        self.gap_between_pipes: float = GAP_BETWEEN_PIPES
        self.upper_pipe_height: float = UPPER_PIPE_HEIGHT
        self.color: tuple[int] = GREEN
        self.x_pos: float = 450 or SCREEN_WIDTH + self.width / 2
        self.upper_body: pygame.Rect = pygame.Rect(
            self.x_pos,
            0,
            self.width,
            self.upper_pipe_height,
        )
        self.lower_buddy: pygame.Rect = pygame.Rect(
            self.x_pos,
            self.upper_pipe_height + self.gap_between_pipes,
            self.width,
            SCREEN_HEIGHT - self.upper_pipe_height - self.gap_between_pipes,
        )
        self.velocity: float = PIPE_VELOCITY

    def __str__(self) -> str:
        return "Mr. Pipe"

    def move(self) -> None:
        self.x_pos -= self.velocity
        self.upper_body.update(
            self.x_pos,
            0,
            self.width,
            self.upper_pipe_height,
        )
        self.lower_buddy.update(
            self.x_pos,
            self.upper_pipe_height + self.gap_between_pipes,
            self.width,
            SCREEN_HEIGHT - self.upper_pipe_height - self.gap_between_pipes,
        )

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.upper_body)
        pygame.draw.rect(screen, self.color, self.lower_buddy)
