import Constant as con
from GameObject import GameObject
import tkinter as tk

class Robot(GameObject):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
        self.smile = False
        self.wheel_ids = []  # Для хранения ID колёс
        self.eye_ids = []  # Для хранения ID глаз
        self.mouth_id = None  # Для хранения ID рта
        self.draw()

    def draw(self):
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT

        # Основной прямоугольник робота
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=con.ROBOT_COLOR, outline="black")

        # Колеса (4 маленьких квадрата по углам)
        small_size = con.CELL_WIDTH // 4
        corners = [
            (x1, y1),  # Левый верхний
            (x2 - small_size, y1),  # Правый верхний
            (x1, y2 - small_size),  # Левый нижний
            (x2 - small_size, y2 - small_size)  # Правый нижний
        ]

        for corner in corners:
            wheel_id = self.canvas.create_rectangle(
                corner[0], corner[1],
                corner[0] + small_size, corner[1] + small_size,
                fill=con.DETAIL_COLOR, outline="black"
            )
            self.wheel_ids.append(wheel_id)

        # Глаза (два круга)
        eye_radius = small_size // 4
        left_eye_pos = (x1 + con.CELL_WIDTH // 3, y1 + con.CELL_HEIGHT // 3)
        right_eye_pos = (x2 - con.CELL_WIDTH // 3, y1 + con.CELL_HEIGHT // 3)

        left_eye = self.canvas.create_oval(
            left_eye_pos[0] - eye_radius, left_eye_pos[1] - eye_radius,
            left_eye_pos[0] + eye_radius, left_eye_pos[1] + eye_radius,
            fill=con.EYE_COLOR
        )
        right_eye = self.canvas.create_oval(
            right_eye_pos[0] - eye_radius, right_eye_pos[1] - eye_radius,
            right_eye_pos[0] + eye_radius, right_eye_pos[1] + eye_radius,
            fill=con.EYE_COLOR
        )
        self.eye_ids.extend([left_eye, right_eye])

        # Рот (инициализируем)
        self.update_mouth()

    def update_mouth(self):
        """Обновляет отображение рта в зависимости от состояния smile"""
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT

        # Удаляем старый рот, если он есть
        if self.mouth_id:
            self.canvas.delete(self.mouth_id)

        if self.smile:
            # Рисуем улыбку (дугу)
            self.mouth_id = self.canvas.create_arc(
                x1 + con.CELL_WIDTH // 4, y1 + con.CELL_HEIGHT // 2 - 5,
                x2 - con.CELL_WIDTH // 4, y1 + con.CELL_HEIGHT // 2 + 25,
                start=180, extent=180, style=tk.ARC, width=2, outline=con.EYE_COLOR
            )
        else:
            # Рисуем прямой рот (прямоугольник)
            self.mouth_id = self.canvas.create_rectangle(
                x1 + con.CELL_WIDTH // 4, y1 + con.CELL_HEIGHT // 2 + 10,
                x2 - con.CELL_WIDTH // 4, y1 + con.CELL_HEIGHT // 2 + 15,
                fill=con.EYE_COLOR
            )

    def move(self, dx, dy):
        """Перемещает робота и все его части"""
        self.x += dx
        self.y += dy
        self.update_position()

    def update_position(self):
        """Обновляет позиции всех элементов робота"""
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT

        # Основной прямоугольник
        self.canvas.coords(self.id, x1, y1, x2, y2)

        # Обновляем позиции колёс
        small_size = con.CELL_WIDTH // 4
        corners = [
            (x1, y1),
            (x2 - small_size, y1),
            (x1, y2 - small_size),
            (x2 - small_size, y2 - small_size)
        ]

        for i, corner in enumerate(corners):
            self.canvas.coords(
                self.wheel_ids[i],
                corner[0], corner[1],
                corner[0] + small_size, corner[1] + small_size
            )

        # Обновляем позиции глаз
        eye_radius = small_size // 4
        left_eye_pos = (x1 + con.CELL_WIDTH // 3, y1 + con.CELL_HEIGHT // 3)
        right_eye_pos = (x2 - con.CELL_WIDTH // 3, y1 + con.CELL_HEIGHT // 3)

        self.canvas.coords(
            self.eye_ids[0],
            left_eye_pos[0] - eye_radius, left_eye_pos[1] - eye_radius,
            left_eye_pos[0] + eye_radius, left_eye_pos[1] + eye_radius
        )
        self.canvas.coords(
            self.eye_ids[1],
            right_eye_pos[0] - eye_radius, right_eye_pos[1] - eye_radius,
            right_eye_pos[0] + eye_radius, right_eye_pos[1] + eye_radius
        )

        # Обновляем рот
        self.update_mouth()

    def update_smile(self, barrels, targets):
        """Обновляет состояние улыбки в зависимости от положения бочек"""
        all_on_target = True
        for barrel in barrels:
            on_target = False
            for target in targets:
                if barrel.x == target.x and barrel.y == target.y and barrel.color == target.color:
                    on_target = True
                    break
            if not on_target:
                all_on_target = False
                break

        if self.smile != all_on_target:  # Обновляем только если состояние изменилось
            self.smile = all_on_target
            self.update_mouth()  # Обновляем отображение рта