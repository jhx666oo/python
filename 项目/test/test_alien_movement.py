import sys
import unittest

# 添加源代码目录到sys.path
sys.path.insert(0, 'D:\\25448\\python课程\\python_practice\\项目\\daima')

from alien import Alien
from settings import Settings
from alien_invasion import AlienInvasion

class TestAlienMovement(unittest.TestCase):

    def setUp(self):
        ai_game = AlienInvasion()
        self.alien = Alien(ai_game)

    def test_alien_movement(self):
        """测试外星人移动"""
        initial_x = self.alien.x
        self.alien.update()
        self.assertNotEqual(self.alien.x, initial_x)

if __name__ == '__main__':
    unittest.main()
