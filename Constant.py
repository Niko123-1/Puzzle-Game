# Константы
CELL_WIDTH = 100
CELL_HEIGHT = 100

# Размеры сетки для каждого уровня (индекс 0 - уровень 1, индекс 1 - уровень 2 и т.д.)
GRID_COLS = [7, 6, 7, 8, 11]
GRID_ROWS = [6, 6, 7, 7, 6]

# Цвета
WHITE = "#FFFFFF"
GRID_COLOR = "#CCCCCC"
ROBOT_COLOR = "#B3BC3E"
DETAIL_COLOR = "#000000"
EYE_COLOR = "#FFFFFF"
OBSTACLE_COLOR = "#6E73F7"
TARGET_COLOR1 = "#FF0000" # красный
TARGET_COLOR2 = "#80FF00" # зеленый
TARGET_COLOR3 = "#1CF9F2" # голубой
TARGET_COLOR4 = "#F91CCD" # фуксия
TARGET_COLOR5 = "#E1F009" # желтый
DEFAULT_BARREL_COLOR = "#928282" # серый

# Функция для получения размеров экрана для конкретного уровня
def get_screen_size(level):
    level_index = level - 1  # преобразуем номер уровня в индекс
    return (GRID_COLS[level_index] * CELL_WIDTH,
            GRID_ROWS[level_index] * CELL_HEIGHT)