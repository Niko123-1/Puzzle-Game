import Constant as con
from GameObject import GameObject


class Target(GameObject):
    def __init__(self, canvas, x, y, color):
        super().__init__(canvas, x, y)
        self.color = color
        self.draw()

    def draw(self):
        x = self.x * con.CELL_WIDTH + con.CELL_WIDTH // 2
        y = self.y * con.CELL_HEIGHT + con.CELL_HEIGHT // 2
        max_radius = min(con.CELL_WIDTH, con.CELL_HEIGHT) // 2 - 5

        # Рисуем мишень (3 круга)
        for i in range(3, 0, -1):
            radius = max_radius * i / 3
            if i % 2 == 1:
                fill = self.color
            else:
                fill = "#7A8591"
            self.canvas.create_oval(
                x - radius, y - radius,
                x + radius, y + radius,
                fill=fill, outline=""
            )
