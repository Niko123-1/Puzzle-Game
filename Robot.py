from unittest.mock import right

import pygame
import Constant as con

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
        # Основной прямоугольник робота
        pygame.draw.rect(screen, con.ROBOT_COLOR, self.rect)

        # Размеры маленьких прямоугольников (1/4 от размера клетки)
        small_rect_size = con.CELL_WIDTH // 4

        # Координаты 4 углов основного прямоугольника
        corners = [
            (self.rect.left, self.rect.top),  # Левый верхний
            (self.rect.right - small_rect_size, self.rect.top),  # Правый верхний
            (self.rect.left, self.rect.bottom - small_rect_size),  # Левый нижний
            (self.rect.right - small_rect_size, self.rect.bottom - small_rect_size)  # Правый нижний
        ]

        # Колеса по углам робота
        for corner in corners:
            small_rect = pygame.Rect(corner[0], corner[1], small_rect_size, small_rect_size)
            pygame.draw.rect(screen, con.DETAIL_COLOR, small_rect)

        # Глаза
        eye_radius = small_rect_size // 4
        left_eye_pos = (self.rect.left + con.CELL_WIDTH // 3, self.rect.top + con.CELL_HEIGHT // 3)
        right_eye_pos = (self.rect.right - con.CELL_WIDTH // 3, self.rect.top + con.CELL_HEIGHT // 3)

        pygame.draw.circle(screen, con.EYE_COLOR, left_eye_pos, eye_radius)
        pygame.draw.circle(screen, con.EYE_COLOR, right_eye_pos, eye_radius)

        mouth_width = con.CELL_WIDTH // 2
        mouth_height = 5
        mouth_rect = pygame.Rect(
            self.rect.centerx - mouth_width // 2,
            self.rect.centery + 10,
            mouth_width,
            mouth_height
        )
        pygame.draw.rect(screen, con.EYE_COLOR, mouth_rect)  # Чёрный прямоугольник