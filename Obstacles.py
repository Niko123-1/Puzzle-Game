import pygame
import Constant as con


class Obstacle:
    """Неподвижное препятствие"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            self.x * con.CELL_WIDTH,
            self.y * con.CELL_HEIGHT,
            con.CELL_WIDTH,
            con.CELL_HEIGHT
        )
        self.fill_color = (110, 115, 247)
        self.border_color = (0, 0, 0)
        self.border_width = 1
        self.cross_color = (0, 0, 0)  # Цвет креста
        self.cross_width = 2  # Толщина линий креста

    def draw(self, screen):
        # Рисуем основной прямоугольник
        pygame.draw.rect(screen, self.fill_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

        # Координаты для креста
        left_top = (self.rect.left, self.rect.top)
        right_bottom = (self.rect.right, self.rect.bottom)
        right_top = (self.rect.right, self.rect.top)
        left_bottom = (self.rect.left, self.rect.bottom)

        # Рисуем две диагональные линии (крест)
        pygame.draw.line(screen, self.cross_color, left_top, right_bottom, self.cross_width)
        pygame.draw.line(screen, self.cross_color, right_top, left_bottom, self.cross_width)