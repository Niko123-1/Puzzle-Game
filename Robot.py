import pygame

# Настройки
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_ROWS = 6
GRID_COLS = 6
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
ROBOT_COLOR = (188, 198, 52)  # Зеленый

class Robot:
    """Робот, который может толкать бочки"""

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            self.x * CELL_WIDTH,
            self.y * CELL_HEIGHT,
            CELL_WIDTH,
            CELL_HEIGHT
        )

    def move(self, dx, dy, barrels, obstacles):
        """Пытается переместить робота, толкая бочки при необходимости"""
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверка границ
        if not (0 <= new_x < GRID_COLS and 0 <= new_y < GRID_ROWS):
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
        self.rect.x = self.x * CELL_WIDTH
        self.rect.y = self.y * CELL_HEIGHT
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, ROBOT_COLOR, self.rect)