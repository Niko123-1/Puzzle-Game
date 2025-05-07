import tkinter as tk
from tkinter import messagebox, Label, Button
import Constant as con
import Robot as rb
import Barrel as br
import Target as tg
import Obstacles as ob
from enum import Enum
import LevelConfig as lc

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Обезвредить бочки!!!")
        self.root.state('zoomed')
        # Инициализация переменных
        self.victory_shown = False
        self.current_level = None
        self.canvas = None  # Будет создаваться при старте уровня

        # Показываем меню уровней
        self.level_menu()

    def level_menu(self):
        """Создаёт интерфейс выбора уровня."""
        self.clear_window()

        # Сбрасываем состояние игры
        self.victory_shown = False
        if hasattr(self, 'robot'):
            del self.robot
        if hasattr(self, 'barrels'):
            del self.barrels
        if hasattr(self, 'targets'):
            del self.targets
        if hasattr(self, 'obstacles'):
            del self.obstacles

        label = tk.Label(self.root, text="Выберите уровень:", font=("Arial", 25))
        label.pack(pady=20, padx=20)

        # Создаем фрейм для кнопок
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=20)

        level1_btn = tk.Button(button_frame, text="Уровень 1", command=lambda: self.start_level(1), width=10, height=4, font=("Arial", 14))
        level1_btn.grid(row=0, column=0, padx=15, pady=200)

        level2_btn = tk.Button(button_frame, text="Уровень 2", command=lambda: self.start_level(2), width=10, height=4, font=("Arial", 14))
        level2_btn.grid(row=0, column=1, padx=15, pady=200)

        level3_btn = tk.Button(button_frame, text="Уровень 3", command=lambda: self.start_level(3), width=10, height=4, font=("Arial", 14))
        level3_btn.grid(row=0, column=2, padx=15, pady=200)

        level4_btn = tk.Button(button_frame, text="Уровень 4", command=lambda: self.start_level(4), width=10, height=4, font=("Arial", 14))
        level4_btn.grid(row=0, column=3, padx=15, pady=200)

        level5_btn = tk.Button(button_frame, text="Уровень 5", command=lambda: self.start_level(5), width=10, height=4, font=("Arial", 14))
        level5_btn.grid(row=0, column=4, padx=15, pady=200)

    def clear_window(self):
        """Очищает окно от всех виджетов."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Если canvas существует, уничтожаем его
        if self.canvas:
            self.canvas.destroy()
            self.canvas = None

    def start_level(self, level_num):
        """Запускает выбранный уровень."""
        self.current_level = level_num
        self.clear_window()

        # Получаем размеры экрана для текущего уровня
        screen_width, screen_height = con.get_screen_size(level_num)

        # Создаем новый canvas для игры с размерами для текущего уровня
        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height, bg=con.WHITE)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        # Настраиваем игру
        self.setup_game(level_num)
        self.bind_keys()
        self.draw_grid(level_num)

    def draw_grid(self, level_num):
        """Рисует сетку для текущего уровня."""
        cols = con.GRID_COLS[level_num - 1]
        rows = con.GRID_ROWS[level_num - 1]

        for x in range(0, cols * con.CELL_WIDTH, con.CELL_WIDTH):
            self.canvas.create_line(x, 0, x, rows * con.CELL_HEIGHT, fill=con.GRID_COLOR)
        for y in range(0, rows * con.CELL_HEIGHT, con.CELL_HEIGHT):
            self.canvas.create_line(0, y, cols * con.CELL_WIDTH, y, fill=con.GRID_COLOR)

    def setup_game(self, level_num):
        """Настраивает игровые объекты для выбранного уровня."""
        # Очищаем старые объекты если они есть
        if hasattr(self, 'robot'):
            del self.robot
        if hasattr(self, 'barrels'):
            del self.barrels
        if hasattr(self, 'targets'):
            del self.targets
        if hasattr(self, 'obstacles'):
            del self.obstacles

        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=5, pady=5)  # SE = South-East (низ-право)

        # Новая кнопка (располагается выше)
        new_btn = tk.Button(
                               button_frame,
                               text="Начать заново",
                               command=lambda: self.start_level(level_num),
                               width=20, height=4,
                               font=("Arial", 14),
                               bg="#4CAF50",  # Зеленый фон
                               fg="white",  # Белый текст
                               activebackground="#45a049",  # Темно-зеленый при нажатии
                               activeforeground="white"
                               )
        new_btn.pack(pady=(0, 5))  # Отступ снизу 5px

        return_btn = tk.Button(
                               button_frame,
                               text="В главное меню",
                               command=lambda: self.level_menu(),
                               width=20, height=4,
                               font=("Arial", 14),
                               bg="#4CAF50",  # Зеленый фон
                               fg="white",  # Белый текст
                               activebackground="#45a049",  # Темно-зеленый при нажатии
                               activeforeground="white"
                               )
        return_btn.pack()

        # Получаем размеры сетки и конфигурацию уровня
        cols = con.GRID_COLS[level_num - 1]
        rows = con.GRID_ROWS[level_num - 1]
        config = lc.LevelConfig.get_level_config(level_num)

        if not config:
            return

        # Создаем робота
        self.robot = rb.Robot(self.canvas, *config['robot_pos'])

        # Создаем бочки
        self.barrels = [
            br.Barrel(self.canvas, *barrel['pos'], barrel['color'])
            for barrel in config['barrels']
        ]

        # Создаем цели
        self.targets = [
            tg.Target(self.canvas, *target['pos'], target['color'])
            for target in config['targets']
        ]

        # Бочки должны отрисовываться поверх целей
        for barrel in self.barrels:
            barrel.raise_all()

        # Границы и препятствия
        self.obstacles = []

        # Границы для всех уровней - по периметру
        for x in range(cols):
            self.obstacles.append(ob.Obstacle(self.canvas, x, 0))
            self.obstacles.append(ob.Obstacle(self.canvas, x, rows - 1))

        for y in range(1, rows - 1):
            self.obstacles.append(ob.Obstacle(self.canvas, 0, y))
            self.obstacles.append(ob.Obstacle(self.canvas, cols - 1, y))

        # Дополнительные препятствия
        for (x, y) in config['extra_obstacles']:
            if 0 <= x < cols and 0 <= y < rows:
                self.obstacles.append(ob.Obstacle(self.canvas, x, y))

    # Привязка кнопок управления роботом
    def bind_keys(self):
        self.root.bind("<Up>", lambda e: self.move_robot(Direction.UP))
        self.root.bind("<Down>", lambda e: self.move_robot(Direction.DOWN))
        self.root.bind("<Left>", lambda e: self.move_robot(Direction.LEFT))
        self.root.bind("<Right>", lambda e: self.move_robot(Direction.RIGHT))
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    # Перемещение робота
    def move_robot(self, direction):

        self.robot.raise_all()

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

        # Получаем размеры сетки для текущего уровня
        grid_cols = con.GRID_COLS[self.current_level - 1]
        grid_rows = con.GRID_ROWS[self.current_level - 1]

        # Проверка границ
        if not (0 <= new_x < grid_cols and 0 <= new_y < grid_rows):
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

    # Перемещение бочек
    def move_barrel(self, barrel, dx, dy):
        new_x = barrel.x + dx
        new_y = barrel.y + dy

        # Получаем размеры сетки для текущего уровня
        grid_cols = con.GRID_COLS[self.current_level - 1]
        grid_rows = con.GRID_ROWS[self.current_level - 1]

        # Проверка границ
        if not (0 <= new_x < grid_cols and 0 <= new_y < grid_rows):
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
        barrel.raise_all()
        return True

    # Проверка завершения уровня
    def check_victory(self):
        if self.victory_shown:
            return

        all_on_target = True
        for barrel in self.barrels:
            # Проверяем только цветные бочки (не серые)
            if barrel.color != con.DEFAULT_BARREL_COLOR:
                on_target = False
                for target in self.targets:
                    if (barrel.x == target.x and barrel.y == target.y and barrel.color == target.color):
                        on_target = True
                        barrel.raise_all()
                        break
                if not on_target:
                    all_on_target = False
                    break

        if all_on_target:
            self.victory_shown = True
            messagebox.showinfo("Победа!", "Все бочки обезврежены!")
            self.robot.update_smile(self.barrels, self.targets)
            self.root.after(100, self.level_menu)
            self.victory_shown = False