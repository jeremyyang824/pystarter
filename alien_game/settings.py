class Settings():
    """"存储《外星人入侵》的所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 720
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置

        self.fleet_drop_speed = 10
        # 向右: 1 向左: -1
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏感
        self.speedup_scale = 1.1
        # 外星人点数提高
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 5

        # 外星人分值
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
