import pygame
import Constant as con


class Target:
    """Неподвижное препятствие"""

    def __init__(self, x, y, t_color):
        self.x = x
        self.y = y
        self.t_color=t_color
        self.rect = pygame.Rect(
            self.x * con.CELL_WIDTH,
            self.y * con.CELL_HEIGHT,
            con.CELL_WIDTH,
            con.CELL_HEIGHT
        )
        self.fill_color = (110, 115, 247)  # Красный цвет заливки
        self.border_color = (0, 0, 0)  # Черная граница
        self.border_width = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.t_color, self.rect)