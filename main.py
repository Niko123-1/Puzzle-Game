import pygame
import sys
import Robot as rb
import Barrel as br
import Obstacles as ob

# Настройки
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
GRID_ROWS = 10
GRID_COLS = 10
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS

WHITE = (255, 255, 255)
GRID_COLOR = (50, 50, 50)  # Темно-серый

def main():
    # Инициализация pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Робот и бочки")
    clock = pygame.time.Clock()

    # Создание игровых объектов
    robot = rb.Robot()
    barrels = [
        br.Barrel(3, 3),
        br.Barrel(5, 5),
        br.Barrel(2, 7)
    ]
    obstacles = [
        ob.Obstacle(7, 7),
        ob.Obstacle(8, 8),
        ob.Obstacle(4, 4)
    ]

    # Основной игровой цикл
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Управление роботом
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

        # Отрисовка
        screen.fill(WHITE)

        # Отрисовка сетки
        for x in range(0, SCREEN_WIDTH, CELL_WIDTH):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_HEIGHT):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        # Отрисовка объектов
        for obstacle in obstacles:
            obstacle.draw(screen)
        for barrel in barrels:
            barrel.draw(screen)
        robot.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()