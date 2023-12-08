import sys
import unittest

# 将包含 ship.py 的目录添加到 sys.path
sys.path.insert(0, 'D:\\25448\\python课程\\python_practice\\项目\\daima')

# 现在可以导入 ship 模块
from ship import Ship

from settings import Settings
from alien_invasion import AlienInvasion

class TestShipMovement(unittest.TestCase):

    def setUp(self):
        ai_game = AlienInvasion()
        self.ship = Ship(ai_game)

    def test_move_right(self):
        """测试飞船向右移动"""
        self.ship.moving_right = True
        self.ship.update()
        self.assertTrue(self.ship.rect.x > 0)

    def test_move_left(self):
        """测试飞船向左移动"""
        self.ship.moving_left = True
        self.ship.update()
        self.assertTrue(self.ship.rect.x < self.ship.screen_rect.right)

if __name__ == '__main__':
    unittest.main()
