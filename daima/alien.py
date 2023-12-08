import random
import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """表示单个外星人的类。"""
 
    def __init__(self, ai_game):
        """初始化外星人并设置其初始位置。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
 
        # 加载外星人图像并设置其 rect 属性。 （此处最好使用绝对路径）
        self.image = pygame.image.load('image\\alien.bmp')
        self.rect = self.image.get_rect()
 
        # 每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width   # 上边距设置为外星人的宽
        self.rect.y = self.rect.height  # 上边距设置为外星人的高
 
        # 存储外星人的精确水平和垂直位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 添加初始化垂直速度和方向
        self.y_speed = random.uniform(0.1, self.settings.alien_speed)
        self.x_speed = random.uniform(0.1, self.settings.alien_speed)
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])
 
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True。"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
 
    
    def update(self):
        """向右或向左移动外星人。"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    '''
    def update(self):
        """更新外星人的位置。"""
        # 水平和垂直随机移动
        self.x += self.x_speed * self.x_direction
        self.y += self.y_speed * self.y_direction

        # 随机改变方向
        #if random.randint(0, 200) == 0:  # 示例：每次更新有0.5%的概率改变方向
         #   self.x_direction *= -1
        #if random.randint(0, 200) == 0:
         #   self.y_direction *= -1

        # 检查外星人是否到达屏幕边缘
        if self.check_edges():
            # 改变水平移动方向
            self.x_direction *= -1
            
        self.rect.x = self.x
        self.rect.y = self.y
'''
       