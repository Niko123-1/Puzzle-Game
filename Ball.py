class Ball:
    def __init__(self, canvas, rectangle, color="blue", radius=50):
        self.canvas = canvas
        self.rect = rectangle
        self.radius = radius
        self.color = color
        self.speed = 10
        self.direction = None
        self.moving = False  # Флаг движения
        self.key_press_enabled = True  # Разрешение на обработку нажатий

        # Центральная позиция
        x = (rectangle[0] + rectangle[2]) // 2
        y = (rectangle[1] + rectangle[3]) // 2

        self.id = canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill=color
        )

        # Привязка клавиш
        self.canvas.bind_all("<KeyPress>", self.key_press)
        self.canvas.focus_set()

        self.animate()

    def key_press(self, event):
        """Обработка нажатия клавиш"""
        if not self.key_press_enabled:
            return

        if not self.moving:  # Только если шар не движется
            if event.keysym == "Left":
                self.direction = "left"
                self.moving = True
                self.key_press_enabled = False  # Блокируем кнопки
            elif event.keysym == "Right":
                self.direction = "right"
                self.moving = True
                self.key_press_enabled = False
            elif event.keysym == "Up":
                self.direction = "up"
                self.moving = True
                self.key_press_enabled = False
            elif event.keysym == "Down":
                self.direction = "down"
                self.moving = True
                self.key_press_enabled = False

    def animate(self):
        """Анимация движения"""
        if self.moving and self.direction:
            dx, dy = 0, 0

            if self.direction == "left":
                dx = -self.speed
            elif self.direction == "right":
                dx = self.speed
            elif self.direction == "up":
                dy = -self.speed
            elif self.direction == "down":
                dy = self.speed

            # Проверка столкновения
            x1, y1, x2, y2 = self.canvas.coords(self.id)

            if (x1 + dx < self.rect[0] and self.direction == "left") or \
                    (x2 + dx > self.rect[2] and self.direction == "right") or \
                    (y1 + dy < self.rect[1] and self.direction == "up") or \
                    (y2 + dy > self.rect[3] and self.direction == "down"):

                self.moving = False
                self.direction = None
                self.key_press_enabled = True  # Разблокируем кнопки
            else:
                self.canvas.move(self.id, dx, dy)

        self.canvas.after(20, self.animate)