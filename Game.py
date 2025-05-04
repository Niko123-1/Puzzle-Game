import pygame
import sys
import Robot as rb
import Barrel as br
import Obstacles as ob
import Target as tg
import Constant as con
from tkinter import messagebox
import tkinter as tk

WHITE = (255, 255, 255)
GRID_COLOR = (50, 50, 50)  # Темно-серый

def main():
    # Инициализация pygame
    pygame.init()
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    pygame.display.set_caption("Робот и бочки")
    clock = pygame.time.Clock()

    # Создание игровых объектов
    robot = rb.Robot(4,2)

    barrels = [
        br.Barrel(5, 2, (215,31,31)),
        br.Barrel(1, 2, (43,213,134))
    ]

    obstacles = []

    for x in range(con.GRID_COLS):
        obstacles.append(ob.Obstacle(x, 0))
        obstacles.append(ob.Obstacle(x, con.GRID_ROWS - 1))

    for y in range(1, con.GRID_ROWS - 1):
        obstacles.append(ob.Obstacle(0, y))
        obstacles.append(ob.Obstacle(con.GRID_COLS - 1, y))

    obstacles.append(ob.Obstacle(3,1))
    obstacles.append(ob.Obstacle(4, 1))
    obstacles.append(ob.Obstacle(2, 3))
    obstacles.append(ob.Obstacle(3, 3))
    obstacles.append(ob.Obstacle(3, 4))
    obstacles.append(ob.Obstacle(2, 4))
    obstacles.append(ob.Obstacle(4, 4))
    obstacles.append(ob.Obstacle(5, 4))

    targets = []

    targets.append(tg.Target(5,1, (215,31,31)))
    targets.append(tg.Target(1,4, (43,213,134)))

    # Основной игровой цикл
    running = True
    victory_shown = False
    victory_delay = 0  # Задержка перед показом сообщения (в кадрах)

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Управление роботом (остается без изменений)
            if event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                elif event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_ESCAPE:
                    running = False

                if dx != 0 or dy != 0:
                    robot.move(dx, dy, barrels, obstacles)

        # Отрисовка (остается без изменений)
        screen.fill(WHITE)
        for x in range(0, con.SCREEN_WIDTH, con.CELL_WIDTH):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, con.SCREEN_HEIGHT))
        for y in range(0, con.SCREEN_HEIGHT, con.CELL_HEIGHT):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (con.SCREEN_WIDTH, y))

        for obstacle in obstacles:
            obstacle.draw(screen)
        for barrel in barrels:
            barrel.draw(screen)
        robot.update_smile(barrels, targets)
        robot.draw(screen)
        for target in targets:
            target.draw(screen)

        # Проверка победы
        all_on_target = True
        for barrel in barrels:
            on_target = False
            for target in targets:
                if barrel.is_on_target(target):
                    on_target = True
                    break
            if not on_target:
                all_on_target = False
                break

        if all_on_target and not victory_shown:
            victory_delay += 1  # Увеличиваем счетчик задержки
            if victory_delay >= 5:  # Ждем 5 кадров (~0.08 сек при 60 FPS)
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Победа!", "В главное меню",)
                victory_shown = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()