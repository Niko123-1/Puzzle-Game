import pygame
import Constant as con

class Barrel:
    """Бочка, которую можно двигать"""

    def __init__(self, x, y, b_color):
        self.x = x
        self.y = y
        self.b_color = b_color
        self.rect = pygame.Rect(
            self.x * con.CELL_WIDTH,
            self.y * con.CELL_HEIGHT,
            con.CELL_WIDTH,
            con.CELL_HEIGHT
        )

    def move(self, dx, dy, barrels, obstacles):
        """Пытается переместить бочку, возвращает True если удалось"""
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверка границ
        if not (0 <= new_x < con.GRID_COLS and 0 <= new_y < con.GRID_ROWS):
            return False

        # Проверка других бочек
        for barrel in barrels:
            if barrel != self and barrel.x == new_x and barrel.y == new_y:
                return False

        # Проверка препятствий
        for obstacle in obstacles:
            if obstacle.x == new_x and obstacle.y == new_y:
                return False

        # Перемещаем бочку
        self.x = new_x
        self.y = new_y
        self.rect.x = self.x * con.CELL_WIDTH
        self.rect.y = self.y * con.CELL_HEIGHT
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.b_color, self.rect)

    def is_on_target(self, target):
        return self.x == target.x and self.y == target.y and self.b_color == target.t_color

