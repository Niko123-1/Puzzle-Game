import tkinter as tk
import Game as gm


def main():
    root = tk.Tk()
    game = gm.Game(root)
    root.mainloop()


if __name__ == "__main__":
    main()