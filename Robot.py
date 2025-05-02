import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
GRID_ROWS = 10  # Количество строк в сетке
GRID_COLS = 10  # Количество столбцов в сетке
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS
ROBOT_COLOR = (0, 255, 0)  # Зеленый цвет для робота


class Robot:
    def __init__(self):
        # Начальная позиция робота (в клетках)
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(
            self.x * CELL_WIDTH,
            self.y * CELL_HEIGHT,
            CELL_WIDTH,
            CELL_HEIGHT
        )

    def move(self, dx, dy):
        """Перемещение робота на dx, dy клеток"""
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверка, чтобы робот не выходил за границы поля
        if 0 <= new_x < GRID_COLS and 0 <= new_y < GRID_ROWS:
            self.x = new_x
            self.y = new_y
            self.rect.x = self.x * CELL_WIDTH
            self.rect.y = self.y * CELL_HEIGHT

    def draw(self, screen):
        """Отрисовка робота"""
        pygame.draw.rect(screen, ROBOT_COLOR, self.rect)