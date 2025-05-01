import tkinter as tk
import Ball as bl



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Шар с инерционным движением")

    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    canvas.pack()

    # Границы игрового поля
    rect_coords = (100, 100, 700, 500)
    canvas.create_rectangle(*rect_coords, outline="black", width=2)

    # Создаем шар
    ball = bl.Ball(canvas, rect_coords)

    # Инструкция
    canvas.create_text(350, 50, text="Используйте стрелки для движения", font=("Arial", 14))

    root.mainloop()