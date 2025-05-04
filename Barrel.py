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
        # Создаем временную поверхность с прозрачностью
        transparent_surface = pygame.Surface((con.CELL_WIDTH, con.CELL_HEIGHT), pygame.SRCALPHA)

        # Рисуем круг на временной поверхности
        circle_center = (con.CELL_WIDTH // 2, con.CELL_HEIGHT // 2)
        circle_radius = min(con.CELL_WIDTH, con.CELL_HEIGHT) // 2 - 4  # -4 для отступа от краев

        pygame.draw.circle(
            transparent_surface,
            self.b_color,
            circle_center,
            circle_radius
        )

        # Отображаем временную поверхность на экране
        screen.blit(transparent_surface, (self.rect.x, self.rect.y))

    def is_on_target(self, target):
        return self.x == target.x and self.y == target.y and self.b_color == target.t_color

