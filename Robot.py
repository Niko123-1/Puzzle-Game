from math import pi
import pygame
import Constant as con

class Robot:
    """Робот, который может толкать бочки"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            self.x * con.CELL_WIDTH,
            self.y * con.CELL_HEIGHT,
            con.CELL_WIDTH,
            con.CELL_HEIGHT
        )
        self.smile = False  # Флаг для улыбки

    def update_smile(self, barrels, targets):
        """Обновляет состояние улыбки в зависимости от положения бочек"""
        all_on_target = True
        for barrel in barrels:
            on_target = False
            for target in targets:
                if barrel.x == target.x and barrel.y == target.y:
                    on_target = True
                    break
            if not on_target:
                all_on_target = False
                break
        self.smile = all_on_target

    def move(self, dx, dy, barrels, obstacles):
        """Пытается переместить робота, толкая бочки при необходимости"""
        new_x = self.x + dx
        new_y = self.y + dy

        if not (0 <= new_x < con.GRID_COLS and 0 <= new_y < con.GRID_ROWS):
            return False

        for obstacle in obstacles:
            if obstacle.x == new_x and obstacle.y == new_y:
                return False

        pushed_barrel = None
        for barrel in barrels:
            if barrel.x == new_x and barrel.y == new_y:
                pushed_barrel = barrel
                break

        if pushed_barrel:
            if not pushed_barrel.move(dx, dy, barrels, obstacles):
                return False

        self.x = new_x
        self.y = new_y
        self.rect.x = self.x * con.CELL_WIDTH
        self.rect.y = self.y * con.CELL_HEIGHT
        return True

    def draw(self, screen):
        # Основной прямоугольник робота
        pygame.draw.rect(screen, con.ROBOT_COLOR, self.rect)

        # Колеса
        small_rect_size = con.CELL_WIDTH // 4
        corners = [
            (self.rect.left, self.rect.top),
            (self.rect.right - small_rect_size, self.rect.top),
            (self.rect.left, self.rect.bottom - small_rect_size),
            (self.rect.right - small_rect_size, self.rect.bottom - small_rect_size)
        ]
        for corner in corners:
            small_rect = pygame.Rect(corner[0], corner[1], small_rect_size, small_rect_size)
            pygame.draw.rect(screen, con.DETAIL_COLOR, small_rect)

        # Глаза
        eye_radius = small_rect_size // 4
        left_eye_pos = (self.rect.left + con.CELL_WIDTH // 3, self.rect.top + con.CELL_HEIGHT // 3)
        right_eye_pos = (self.rect.right - con.CELL_WIDTH // 3, self.rect.top + con.CELL_HEIGHT // 3)
        pygame.draw.circle(screen, con.EYE_COLOR, left_eye_pos, eye_radius)
        pygame.draw.circle(screen, con.EYE_COLOR, right_eye_pos, eye_radius)

        # Рот (прямоугольник или улыбка)
        if self.smile:
            # Рисуем улыбку (полудугу)
            smile_rect = pygame.Rect(
                self.rect.centerx - con.CELL_WIDTH // 4,
                self.rect.centery + 5,
                con.CELL_WIDTH // 2,
                con.CELL_HEIGHT // 4
            )
            pygame.draw.arc(
                screen,
                con.EYE_COLOR,
                smile_rect,
                pi,  # Начальный угол (π радиан = 180 градусов)
                2 * pi,  # Конечный угол (2π радиан = 360 градусов)
                2  # Толщина линии
            )
        else:
            # Рисуем обычный прямоугольный рот
            mouth_width = con.CELL_WIDTH // 2
            mouth_height = 5
            mouth_rect = pygame.Rect(
                self.rect.centerx - mouth_width // 2,
                self.rect.centery + 10,
                mouth_width,
                mouth_height
            )
            pygame.draw.rect(screen, con.EYE_COLOR, mouth_rect)