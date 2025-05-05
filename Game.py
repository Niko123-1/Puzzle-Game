import tkinter as tk
from tkinter import messagebox
import Constant as con
import Robot as rb
import Barrel as br
import Target as tg
import Obstacles as ob
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Робот и бочки")

        self.canvas = tk.Canvas(root, width=con.SCREEN_WIDTH, height=con.SCREEN_HEIGHT, bg=con.WHITE)
        self.canvas.pack()

        self.setup_game()
        self.bind_keys()
        self.draw_grid()

        self.victory_shown = False

    def draw_grid(self):
        for x in range(0, con.SCREEN_WIDTH, con.CELL_WIDTH):
            self.canvas.create_line(x, 0, x, con.SCREEN_HEIGHT, fill=con.GRID_COLOR)
        for y in range(0, con.SCREEN_HEIGHT, con.CELL_HEIGHT):
            self.canvas.create_line(0, y, con.SCREEN_WIDTH, y, fill=con.GRID_COLOR)

    def setup_game(self):
        # Создаем игровые объекты
        self.robot = rb.Robot(self.canvas, 4, 2)

        self.barrels = [
            br.Barrel(self.canvas, 5, 2, con.TARGET_COLOR1),
            br.Barrel(self.canvas, 1, 2, con.TARGET_COLOR2)
        ]

        # Препятствия
        self.obstacles = []
        extra_obstacles = [(3, 1), (4, 1), (2, 3), (3, 3), (3, 4), (2, 4), (4, 4), (5, 4)]

        # Границы
        for x in range(con.GRID_COLS):
            self.obstacles.append(ob.Obstacle(self.canvas, x, 0))
            self.obstacles.append(ob.Obstacle(self.canvas, x, con.GRID_ROWS - 1))

        for y in range(1, con.GRID_ROWS - 1):
            self.obstacles.append(ob.Obstacle(self.canvas, 0, y))
            self.obstacles.append(ob.Obstacle(self.canvas, con.GRID_COLS - 1, y))

        # Дополнительные препятствия
        for (x, y) in extra_obstacles:
            if 0 <= x < con.GRID_COLS and 0 <= y < con.GRID_ROWS:
                self.obstacles.append(ob.Obstacle(self.canvas, x, y))

        # Цели
        self.targets = [
            tg.Target(self.canvas, 5, 1, con.TARGET_COLOR1),
            tg.Target(self.canvas, 1, 4, con.TARGET_COLOR2)
        ]

    def bind_keys(self):
        self.root.bind("<Up>", lambda e: self.move_robot(Direction.UP))
        self.root.bind("<Down>", lambda e: self.move_robot(Direction.DOWN))
        self.root.bind("<Left>", lambda e: self.move_robot(Direction.LEFT))
        self.root.bind("<Right>", lambda e: self.move_robot(Direction.RIGHT))
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def move_robot(self, direction):
        dx, dy = 0, 0
        if direction == Direction.UP:
            dy = -1
        elif direction == Direction.DOWN:
            dy = 1
        elif direction == Direction.LEFT:
            dx = -1
        elif direction == Direction.RIGHT:
            dx = 1

        if dx == 0 and dy == 0:
            return

        new_x = self.robot.x + dx
        new_y = self.robot.y + dy

        # Проверка границ
        if not (0 <= new_x < con.GRID_COLS and 0 <= new_y < con.GRID_ROWS):
            return

        # Проверка препятствий
        for obstacle in self.obstacles:
            if obstacle.x == new_x and obstacle.y == new_y:
                return

        # Проверка бочек
        pushed_barrel = None
        for barrel in self.barrels:
            if barrel.x == new_x and barrel.y == new_y:
                pushed_barrel = barrel
                break

        if pushed_barrel:
            if not self.move_barrel(pushed_barrel, dx, dy):
                return

        # Двигаем робота
        self.robot.move(dx, dy)
        self.robot.update_smile(self.barrels, self.targets)

        # Проверка победы
        self.check_victory()

    def move_barrel(self, barrel, dx, dy):
        new_x = barrel.x + dx
        new_y = barrel.y + dy

        # Проверка границ
        if not (0 <= new_x < con.GRID_COLS and 0 <= new_y < con.GRID_ROWS):
            return False

        # Проверка других бочек
        for other_barrel in self.barrels:
            if other_barrel != barrel and other_barrel.x == new_x and other_barrel.y == new_y:
                return False

        # Проверка препятствий
        for obstacle in self.obstacles:
            if obstacle.x == new_x and obstacle.y == new_y:
                return False

        # Двигаем бочку
        barrel.move(dx, dy)
        return True

    def check_victory(self):
        if self.victory_shown:
            return

        all_on_target = True
        for barrel in self.barrels:
            on_target = False
            for target in self.targets:
                if barrel.x == target.x and barrel.y == target.y and barrel.color == target.color:
                    on_target = True
                    break
            if not on_target:
                all_on_target = False
                break

        if all_on_target:
            self.victory_shown = True
            self.robot.update_smile(self.barrels, self.targets)
            messagebox.showinfo("Победа!", "Все бочки на месте!")
            self.root.after(1000, self.root.destroy)

