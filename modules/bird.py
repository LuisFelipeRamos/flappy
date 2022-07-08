import pygame
from pygame.constants import K_SPACE

from utils import *


class Bird():
    def __init__(self):
        self.x_pos = BIRD_INITIAL_X_POS
        self.y_pos = BIRD_INITIAL_Y_POS
        self.size = BIRD_SIZE
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)
        self.is_flying = False

    def fly(self):

        if self.is_flying:
            self.y_pos -= 3
        else:
            self.y_pos += 3
            
        self.body = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.body)