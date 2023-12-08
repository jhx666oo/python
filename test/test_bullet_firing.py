import sys
import unittest

# 将包含 bullet.py 的目录添加到 sys.path
sys.path.insert(0, 'D:\\25448\\python课程\\python_practice\\项目\\daima')

from bullet import Bullet
from settings import Settings
from alien_invasion import AlienInvasion

class TestBulletFiring(unittest.TestCase):

    def setUp(self):
        ai_game = AlienInvasion()
        self.bullet = Bullet(ai_game)

    def test_bullet_movement(self):
        """测试子弹向上移动"""
        initial_y = self.bullet.y
        self.bullet.update()
        self.assertTrue(self.bullet.y < initial_y)

if __name__ == '__main__':
    unittest.main()
