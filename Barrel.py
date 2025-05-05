import Constant as con
from GameObject import GameObject
import tkinter as tk  # Не забудьте импортировать tkinter


class Barrel(GameObject):
    def __init__(self, canvas, x, y, color):
        super().__init__(canvas, x, y)
        self.color = color
        self.tox_symbol_id = None  # ID знака токсичности на canvas
        self.draw()

    def draw(self):
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT

        # Рисуем круг (бочку)
        self.id = self.canvas.create_oval(
            x1 + 5, y1 + 5,
            x2 - 5, y2 - 5,
            fill=self.color,
            outline="black"
        )

        # Рисуем знак токсичности (☠) поверх бочки
        self.tox_symbol_id = self.canvas.create_text(
            (x1 + x2) // 2, (y1 + y2) // 2,
            text="☠",  # Символ черепа с костями
            font=("Arial", int(con.CELL_WIDTH * 0.4)),  # Размер шрифта адаптивный
            fill="black"  # Используем строку с цветом
        )

    def move(self, dx, dy):
        """Перемещает бочку и её знак токсичности"""
        super().move(dx, dy)  # Вызываем родительский метод

        # Обновляем позицию знака токсичности
        if self.tox_symbol_id:
            x1 = self.x * con.CELL_WIDTH
            y1 = self.y * con.CELL_HEIGHT
            x2 = x1 + con.CELL_WIDTH
            y2 = y1 + con.CELL_HEIGHT

            self.canvas.coords(
                self.tox_symbol_id,
                (x1 + x2) // 2, (y1 + y2) // 2
            )