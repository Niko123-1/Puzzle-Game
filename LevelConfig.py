"""Настройки для уровня"""
"""get_level_config - метод возвращает настройки для заданного уровня level_num"""
"""robot_pos - позиция робота на игровом поле"""
"""barrels - позиции бочек"""
"""targets - позиции целей, куда ставить бочки"""
"""extra_obstacles - дополнительные препятствия"""

import Constant as con


class LevelConfig:
    @staticmethod
    def get_level_config(level_num):
        if level_num == 1:
            return {
                'grid_size': (7, 6),
                'robot_pos': (4, 2),
                'barrels': [
                    {'pos': (5, 2), 'color': con.TARGET_COLOR1},
                    {'pos': (1, 2), 'color': con.TARGET_COLOR2}
                ],
                'targets': [
                    {'pos': (5, 1), 'color': con.TARGET_COLOR1},
                    {'pos': (1, 4), 'color': con.TARGET_COLOR2}
                ],
                'extra_obstacles': [(3, 1), (4, 1), (2, 3), (3, 3), (3, 4), (2, 4), (4, 4), (5, 4)]
            }
        elif level_num == 2:
            return {
                'grid_size': (6, 6),
                'robot_pos': (1, 4),
                'barrels': [
                    {'pos': (2, 2), 'color': con.TARGET_COLOR1},
                    {'pos': (2, 3), 'color': con.TARGET_COLOR2}
                ],
                'targets': [
                    {'pos': (3, 3), 'color': con.TARGET_COLOR1},
                    {'pos': (3, 2), 'color': con.TARGET_COLOR2}
                ],
                'extra_obstacles': [(1, 1), (2, 1), (4, 4)]
            }
        elif level_num == 3:
            return {
                'grid_size': (7, 7),
                'robot_pos': (3, 3),
                'barrels': [
                    {'pos': (2, 2), 'color': con.TARGET_COLOR1},
                    {'pos': (4, 4), 'color': con.TARGET_COLOR2},
                    {'pos': (3, 2), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (4, 2), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (4, 3), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (2, 3), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (2, 4), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (3, 4), 'color': con.DEFAULT_BARREL_COLOR}
                ],
                'targets': [
                    {'pos': (4, 2), 'color': con.TARGET_COLOR1},
                    {'pos': (2, 4), 'color': con.TARGET_COLOR2}
                ],
                'extra_obstacles': [(2, 1), (1, 5), (4, 5)]
            }
        elif level_num == 4:
            return {
                'grid_size': (8, 7),
                'robot_pos': (4, 1),
                'barrels': [
                    {'pos': (3, 4), 'color': con.TARGET_COLOR1},
                    {'pos': (3, 2), 'color': con.TARGET_COLOR2},
                    {'pos': (2, 2), 'color': con.TARGET_COLOR3},
                    {'pos': (4, 2), 'color': con.TARGET_COLOR4},
                    {'pos': (4, 4), 'color': con.TARGET_COLOR5},
                ],
                'targets': [
                    {'pos': (2, 3), 'color': con.TARGET_COLOR1},
                    {'pos': (3, 3), 'color': con.TARGET_COLOR2},
                    {'pos': (4, 3), 'color': con.TARGET_COLOR3},
                    {'pos': (5, 3), 'color': con.TARGET_COLOR4},
                    {'pos': (6, 3), 'color': con.TARGET_COLOR5}
                ],
                'extra_obstacles': [(5, 1), (6, 1), (5, 2), (6, 2),(5, 4), (6, 4), (5, 5), (6, 5), (1, 4), (1, 5)]
            }
        elif level_num == 5:
            return {
                'grid_size': (11, 6),
                'robot_pos': (6, 1),
                'barrels': [
                    {'pos': (7, 4), 'color': con.TARGET_COLOR1},
                    {'pos': (6, 3), 'color': con.TARGET_COLOR2},
                    {'pos': (7, 2), 'color': con.TARGET_COLOR3},
                    {'pos': (8, 3), 'color': con.TARGET_COLOR4},
                    {'pos': (7, 3), 'color': con.TARGET_COLOR5},
                    {'pos': (3, 4), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (2, 3), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (3, 2), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (4, 3), 'color': con.DEFAULT_BARREL_COLOR},
                    {'pos': (3, 3), 'color': con.DEFAULT_BARREL_COLOR}
                ],
                'targets': [
                    {'pos': (3, 4), 'color': con.TARGET_COLOR1},
                    {'pos': (2, 3), 'color': con.TARGET_COLOR2},
                    {'pos': (3, 2), 'color': con.TARGET_COLOR3},
                    {'pos': (4, 3), 'color': con.TARGET_COLOR4},
                    {'pos': (3, 3), 'color': con.TARGET_COLOR5}
                ],
                'extra_obstacles': [(1,1),(2,1),(3,1),(4,1),(5,1),(9,1)]
            }
        elif level_num == 6:
            return {
                'grid_size': (9, 6),
                'robot_pos': (7, 4),
                'barrels': [
                    {'pos': (5, 4), 'color': con.TARGET_COLOR1},
                    {'pos': (4, 3), 'color': con.TARGET_COLOR2},
                    {'pos': (5, 2), 'color': con.TARGET_COLOR3},
                    {'pos': (6, 3), 'color': con.TARGET_COLOR4}
                ],
                'targets': [
                    {'pos': (2, 4), 'color': con.TARGET_COLOR1},
                    {'pos': (1, 3), 'color': con.TARGET_COLOR2},
                    {'pos': (2, 2), 'color': con.TARGET_COLOR3},
                    {'pos': (3, 3), 'color': con.TARGET_COLOR4}
                ],
                'extra_obstacles': [(1,4),(2,3),(5,3),(7,1)]
            }
        return None

    @staticmethod
    def get_screen_size(level_num):
        """Возвращает кол-во квадратов, нужного для задания размера экрана для указанного уровня."""
        config = LevelConfig.get_level_config(level_num)
        if config and 'grid_size' in config:
            return config['grid_size']
        return None