import pygame
import Constant as con

ROBOT_COLOR = (188, 198, 52)

class Robot:
    """Робот, который может толкать бочки"""

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            self.x * con.CELL_WIDTH,
            self.y * con.CELL_HEIGHT,
            con.CELL_WIDTH,
            con.CELL_HEIGHT
        )

    def move(self, dx, dy, barrels, obstacles):
        """Пытается переместить робота, толкая бочки при необходимости"""
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверка границ
        if not (0 <= new_x < con.GRID_COLS and 0 <= new_y < con.GRID_ROWS):
            return False

        # Проверка препятствий
        for obstacle in obstacles:
            if obstacle.x == new_x and obstacle.y == new_y:
                return False

        # Проверка бочек
        pushed_barrel = None
        for barrel in barrels:
            if barrel.x == new_x and barrel.y == new_y:
                pushed_barrel = barrel
                break

        if pushed_barrel:
            # Пытаемся толкнуть бочку
            if not pushed_barrel.move(dx, dy, barrels, obstacles):
                return False

        # Перемещаем робота
        self.x = new_x
        self.y = new_y
        self.rect.x = self.x * con.CELL_WIDTH
        self.rect.y = self.y * con.CELL_HEIGHT
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, ROBOT_COLOR, self.rect)