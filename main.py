import pygame
import sys
import Robot as rb


# Инициализация Pygame
pygame.init()

# Константы

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
GRID_ROWS = 10  # Количество строк в сетке
GRID_COLS = 10  # Количество столбцов в сетке
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS

def draw_grid(screen):
    """Отрисовка сетки"""
    for x in range(0, SCREEN_WIDTH, CELL_WIDTH):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_HEIGHT):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (SCREEN_WIDTH, y))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Робот в сетке")
    clock = pygame.time.Clock()

    robot = rb.Robot()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Управление роботом стрелками
                if event.key == pygame.K_UP:
                    robot.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    robot.move(0, 1)
                elif event.key == pygame.K_LEFT:
                    robot.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    robot.move(1, 0)

        # Отрисовка
        screen.fill((255, 255, 255))
        draw_grid(screen)
        robot.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()