import pygame
import sys

# Настройки
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
GRID_ROWS = 10
GRID_COLS = 10
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
OBSTACLE_COLOR = (255, 0, 0)  # Красный

class Obstacle:
    """Неподвижное препятствие"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            self.x * CELL_WIDTH,
            self.y * CELL_HEIGHT,
            CELL_WIDTH,
            CELL_HEIGHT
        )

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)