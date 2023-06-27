import pygame

from utils import *


class Bird:
    def __init__(self) -> None:
        self.x_pos: float = BIRD_INITIAL_X_POS
        self.y_pos: float = BIRD_INITIAL_Y_POS
        self.size: float = BIRD_SIZE
        self.body: pygame.Rect = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)
        self.is_flying: bool = False

    def fly(self) -> None:
        if self.is_flying:
            self.y_pos -= 3
        else:
            self.y_pos += 3
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, YELLOW, self.body)
