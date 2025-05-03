import pygame

# Настройки
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_ROWS = 6
GRID_COLS = 6
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
OBSTACLE_COLOR = (145, 145, 255)

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
        self.fill_color = (110, 115, 247)  # Красный цвет заливки
        self.border_color = (0, 0, 0)  # Черная граница
        self.border_width = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.fill_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)