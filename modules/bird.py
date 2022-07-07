import pygame
from pygame.constants import K_SPACE

from utils import *


class Bird():
    def __init__(self):
        self.x_pos = BIRD_INITIAL_X_POS
        self.y_pos = BIRD_INITIAL_Y_POS
        self.size = BIRD_SIZE
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            self.y_pos += 1
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.body)