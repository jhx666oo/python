import sys
import pygame
import random

from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from star import Star
 
 
class AlienInvasion:
    """管理游戏资源和行为的类"""
 
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化背景设置
        self.settings = Settings()  # 将Setting类中的资源赋给alien_invasion模块中self.settings这个参数
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
 
        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self)
 
        # 创建存储游戏统计信息的实例，并创建记分牌。
        self.sb = Scoreboard(self)
 
        # 此处 self 对应 Ship 类中定义的 ai_game ，此处将使得 ship 可以通过 ai_game 访问 AlienInvasion 中的初始化后的资源
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # 创建 Play 按钮
        self.play_button = Button(self, 'Play')
 
        self._create_fleet()
        
        #创建 星星类
        self.stars = pygame.sprite.Group()
        self._create_starfield()
        
 
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
                #self._create_fleet()
                
            # 每次循环时都重绘屏幕
            self._update_screen()


    def _check_events(self):
        """响应键盘和鼠标事件。"""
        for event in pygame.event.get():  # 事件循环
            if event.type == pygame.QUIT:  # 关闭事件判定
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydowm_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 监测鼠标
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
 
    def _check_play_button(self, mouse_pos):
        """在玩家单机 Play 按钮时开始游戏。"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息。
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
 
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
 
            # 创建一群新的外星人并让飞船居中。
            self._create_fleet()
            self.ship.center_ship()
 
            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)
 
 
    def _create_starfield(self):
        """创建一群星星。"""
        star = Star(self)
        star_width, star_height = star.rect.size
        for _ in range(50):  # 假设创建50颗星星
            star = Star(self)
            self.stars.add(star)
 
    def _update_screen(self):
        """ 更新屏幕上的图像， 并切换到新屏幕 """
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 显示得分
        self.sb.show_score()
 
        # 如果游戏处于非活动状态，就显示 Play 按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()  # 循环显示新屏幕
 
    def _check_keydowm_events(self, event):
        """响应按键。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:  # 处理向上移动
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:  # 处理向下移动
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
            
    def _check_keyup_events(self, event):
        """响应键盘松开。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:  # 停止向上移动
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:  # 停止向下移动
            self.ship.moving_down = False
 
    def _fire_bullet(self):
        """创建一颗子弹， 并将其加入编组 bullets 中。"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
 
    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹。"""
        # 更新消失的子弹
        self.bullets.update()
 
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
 
    def _check_bullet_alien_collisions(self):
        """相应子弹和外星人碰撞。"""
        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
 
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
 
        if not self.aliens:
            # 删除现有的子弹并新建一群外星人。
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_spped()
 
            # 提高等级。
            self.stats.level += 1
            self.sb.prep_level()
            
    
    
    def _create_fleet(self):
        """创建外星人群。"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = (self.settings.screen_height - (3 * alien_height) - self.ship.rect.height)

        # 基于游戏等级调整外星人数量
        number_aliens_x = min(available_space_x // (2 * alien_width), max(3, self.stats.level))
        number_rows = min(available_space_y // (2 * alien_height), max(1, self.stats.level))

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
 
    def _create_alien(self, alien_number, row_number):
        # 创建一个外星人并将其加入当前行。
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    
    
    def _update_aliens(self):
        """
            检查是否有外星人位于屏幕边缘
            更新外星人群中所有外星人的位置。
        """
        self._check_fleet_edges()
        self.aliens.update()
 
        # 检查外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
 
        # 检查是否有外星人到达了屏幕底端。
        self._check_alien_bottom()
 
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施。"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
 
    def _change_fleet_direction(self):
        """将整群机器人下移，并改变它们的方向。"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
 
    def _ship_hit(self):
        """响应飞船被外星人撞到。"""
        if self.stats.ships_left > 0:
            # 将 ships_left 减 1 并更新记分牌。
            self.stats.ships_left -= 1
            self.sb.prep_ships()
 
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
 
            # 创建一群新的外星人，并将飞船放到屏幕底端的中央。
            self._create_fleet()
            self.ship.center_ship()
 
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
 
    def _check_alien_bottom(self):
        """检查是否有外星人到达了屏幕底端。"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理。
                #self._ship_hit()  
                alien.rect.y = 0
                break
 

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()