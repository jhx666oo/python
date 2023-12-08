import json
import os

class GameStats:
    """跟踪游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        # 指定最高分文件的完整路径
        self.high_score_file = 'D:\\25448\\python课程\\python_practice\\项目\\daima\\high_score.json'
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """从文件中加载最高得分。"""
        if os.path.exists(self.high_score_file):
            with open(self.high_score_file) as f:
                return json.load(f)
        return 0

    def save_high_score(self):
        """将最高得分保存到文件。"""
        with open(self.high_score_file, 'w') as f:
            json.dump(self.high_score, f)
