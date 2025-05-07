"""Настройки для уровня"""
"""get_level_config - метод возвращает настройки для заданного уровня level_num"""
"""robot_pos - позиция робота на игровом поле"""
"""barrels - позиции бочек"""
"""targets - позиции целей, куда ставить бочки"""
"""extra_obstacles - дополнительные препятствия"""

import Constant as con
import Levels as lv


class LevelConfig:

    @staticmethod
    def get_level_config(level_num):
        return lv.levels[level_num]

    @staticmethod
    def get_screen_size(level_num):
        """Возвращает кол-во квадратов, нужного для задания размера экрана для указанного уровня."""
        config = LevelConfig.get_level_config(level_num)
        if config and 'grid_size' in config:
            return config['grid_size']
        return None