import tkinter as tk
import Box as bl

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    # Границы поля (4 линии)
    border_lines = [
        (100, 100, 720, 100),  # верх
        (720, 100, 720, 520),  # право
        (720, 520, 100, 520),  # низ
        (100, 520, 100, 100)  # лево
    ]

    # Препятствия (линии)
    obstacles = [
        (220, 100, 220, 300),
        (220, 300, 520, 300),
        (520, 300, 520, 200),
        (400, 100, 400, 200)
    ]

    # Отрисовка линий
    for line in border_lines + obstacles:
        canvas.create_line(*line, fill="black", width=2)

    root.mainloop()