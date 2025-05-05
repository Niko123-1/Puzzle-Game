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

    @staticmethod
    def place_obstacles(additional_obstacles=None):
        """Создает препятствия по периметру и дополнительные (если заданы)"""
        obstacles = []

        # 1. Препятствия по периметру
        # Верхняя и нижняя границы
        for x in range(con.GRID_COLS):
            obstacles.append(Obstacle(x, 0))  # Верх
            obstacles.append(Obstacle(x, con.GRID_ROWS - 1))  # Низ

        # Левая и правая границы (без углов, чтобы не дублировать)
        for y in range(1, con.GRID_ROWS - 1):
            obstacles.append(Obstacle(0, y))  # Лево
            obstacles.append(Obstacle(con.GRID_COLS - 1, y))  # Право

        # 2. Дополнительные препятствия (если переданы)
        if additional_obstacles:
            for (x, y) in additional_obstacles:
                if 0 <= x < con.GRID_COLS and 0 <= y < con.GRID_ROWS:
                    obstacles.append(Obstacle(x, y))

        return obstacles
