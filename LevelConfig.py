import Constant as con

class LevelConfig:
    @staticmethod
    def get_level_config(level_num):
        if level_num == 1:
            return {
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
        return None