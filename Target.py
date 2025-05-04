import pygame
import Constant as con


class Target:
    """Неподвижное препятствие в виде мишени"""

    def __init__(self, x, y, t_color):
        self.x = x
        self.y = y
        self.t_color = t_color
        self.rect = pygame.Rect(
            self.x * con.CELL_WIDTH,
            self.y * con.CELL_HEIGHT,
            con.CELL_WIDTH,
            con.CELL_HEIGHT
        )

    def draw(self, screen):
        # Создаем временную поверхность с прозрачностью
        transparent_surface = pygame.Surface((con.CELL_WIDTH, con.CELL_HEIGHT), pygame.SRCALPHA)

        circle_center = (con.CELL_WIDTH // 2, con.CELL_HEIGHT // 2)
        max_radius = min(con.CELL_WIDTH, con.CELL_HEIGHT) // 2 - 4  # -4 для отступа от краев

        # Количество кругов в мишени (можно настроить)
        circle_count = 3
        for i in range(circle_count, 0, -1):
            # Вычисляем радиус текущего круга
            radius = max_radius * i / circle_count

            # Чередуем цвет (можно настроить цвета)
            if i % 2 == 1:
                color = self.t_color
            else:
                # Альтернативный цвет - можно задать или вычислять
                color = (122, 133, 145)

            pygame.draw.circle(
                transparent_surface,
                color,
                circle_center,
                int(radius)
            )

        # Отображаем временную поверхность на экране
        screen.blit(transparent_surface, (self.rect.x, self.rect.y))