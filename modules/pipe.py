import pygame

from utils import *
import random


class Pipe:
    def __init__(self) -> None:
        self.width: float = PIPE_WIDTH
        self.gap_between_pipes: float = GAP_BETWEEN_PIPES
        self.upper_pipe_height: float = random.uniform(a=125, b=475)
        self.color: tuple[int, int, int] = GREEN
        self.x_pos: float = SCREEN_WIDTH + self.width
        self.upper_body: pygame.Rect = pygame.Rect(
            self.x_pos,
            0,
            self.width,
            self.upper_pipe_height,
        )
        self.lower_body: pygame.Rect = pygame.Rect(
            self.x_pos,
            self.upper_pipe_height + self.gap_between_pipes,
            self.width,
            SCREEN_HEIGHT - self.upper_pipe_height - self.gap_between_pipes,
        )
        self.velocity: float = PIPE_VELOCITY
        self.counted: bool = False

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
        self.lower_body.update(
            self.x_pos,
            self.upper_pipe_height + self.gap_between_pipes,
            self.width,
            SCREEN_HEIGHT - self.upper_pipe_height - self.gap_between_pipes,
        )

    """ The -10 here is used only to make the pipe disappearance smoother """

    def is_out_of_bounds(self) -> bool:
        return self.x_pos + PIPE_WIDTH < -10

    def draw(self, screen: pygame.Surface, image) -> None:
        upper_image_flipped = pygame.transform.flip(image, False, True)
        screen.blit(
            source=upper_image_flipped,
            dest=(
                self.upper_body.x,
                self.upper_body.y
                + self.upper_body.height
                - upper_image_flipped.get_height(),
            ),
        )
        screen.blit(source=image, dest=self.lower_body)
