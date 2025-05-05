import Constant as con
from GameObject import GameObject


class Barrel(GameObject):
    def __init__(self, canvas, x, y, color):
        super().__init__(canvas, x, y)
        self.color = color
        self.draw()

    def draw(self):
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT

        # Круг (бочка)
        self.id = self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=self.color, outline="black")