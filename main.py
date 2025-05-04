import pygame
import sys
import Robot as rb
import Barrel as br
import Obstacles as ob
import Target as tg
import Constant as con

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

    target = tg.Target(5,1, (215,31,31))

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
        for x in range(0, con.SCREEN_WIDTH, con.CELL_WIDTH):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, con.SCREEN_HEIGHT))
        for y in range(0, con.SCREEN_HEIGHT, con.CELL_HEIGHT):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (con.SCREEN_WIDTH, y))

        # Отрисовка объектов
        for obstacle in obstacles:
            obstacle.draw(screen)
        for barrel in barrels:
            barrel.draw(screen)
        robot.draw(screen)
        target.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()