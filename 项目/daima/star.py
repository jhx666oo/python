import pygame
from pygame.sprite import Sprite
import random

class Star(Sprite):
    """表示单个星星的类。"""

    def __init__(self, ai_game):
        """初始化星星并设置其随机位置。"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载星星图像并设置其 rect 属性。
        self.image = pygame.image.load('项目\image\star.bmp')
        self.rect = self.image.get_rect()

        # 每个星星在屏幕上的随机位置
        self.rect.x = random.randint(0, ai_game.settings.screen_width - self.rect.width)
        self.rect.y = random.randint(0, ai_game.settings.screen_height - self.rect.height)
