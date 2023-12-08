import pygame


class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
 
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1080
        self.screen_height = 998
        self.bg_color = (230, 230, 230)
       

 
        # 飞船设置
        self.ship_speed = 1.0
        self.ship_limit = 3
 
        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
 
        # 外星人设置
        self.alien_speed = 0.3  # 水平移动速度
        self.alien_speed_vertical = 0.05  # 新增：垂直移动速度
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移， 为 -1 表示向左移。
        self.fleet_direction = 1
 
        # 加快游戏节奏
        self.speedup_scale = 1.05
        # 外星人分数的提高速度
        self.score_scale = 1.2
 
        self.initialize_dynamic_settings()
 
        # 计分
        self.alien_points = 50
 
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.5
 
        # fleet_direction 为 1 表示向右， 为 -1 表示向左。
        self.fleet_direction = 1
 
    def increase_spped(self):
        """提高速度设置和外星人的分数。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
 
        self.alien_points = int(self.alien_points * self.score_scale)