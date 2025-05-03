import pygame

# Настройки
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
GRID_ROWS = 10
GRID_COLS = 10
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
BARREL_COLOR = (139, 69, 19)  # Коричневый

class Barrel:
    """Бочка, которую можно двигать"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            self.x * CELL_WIDTH,
            self.y * CELL_HEIGHT,
            CELL_WIDTH,
            CELL_HEIGHT
        )

    def move(self, dx, dy, barrels, obstacles):
        """Пытается переместить бочку, возвращает True если удалось"""
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверка границ
        if not (0 <= new_x < GRID_COLS and 0 <= new_y < GRID_ROWS):
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
        self.rect.x = self.x * CELL_WIDTH
        self.rect.y = self.y * CELL_HEIGHT
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, BARREL_COLOR, self.rect)