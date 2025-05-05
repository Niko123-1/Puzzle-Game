import Constant as con

class GameObject:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = None

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.update_position()

    def update_position(self):
        x1 = self.x * con.CELL_WIDTH
        y1 = self.y * con.CELL_HEIGHT
        x2 = x1 + con.CELL_WIDTH
        y2 = y1 + con.CELL_HEIGHT
        self.canvas.coords(self.id, x1, y1, x2, y2)