import Constant as con
from GameObject import GameObject


class Obstacle(GameObject):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
        self.draw()

    def draw(self):
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT

        # Основной прямоугольник
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=con.OBSTACLE_COLOR, outline="black")

        # Крест
        self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
        self.canvas.create_line(x1, y2, x2, y1, fill="black", width=2)