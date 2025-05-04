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

    def draw(self, screen):
        # Создаем временную поверхность с прозрачностью
        transparent_surface = pygame.Surface((con.CELL_WIDTH, con.CELL_HEIGHT), pygame.SRCALPHA)

        # Рисуем круг на временной поверхности
        circle_center = (con.CELL_WIDTH // 2, con.CELL_HEIGHT // 2)
        circle_radius = min(con.CELL_WIDTH, con.CELL_HEIGHT) // 2 - 4  # -4 для отступа от краев

        pygame.draw.circle(
            transparent_surface,
            self.t_color,
            circle_center,
            circle_radius
        )

        # Отображаем временную поверхность на экране
        screen.blit(transparent_surface, (self.rect.x, self.rect.y))