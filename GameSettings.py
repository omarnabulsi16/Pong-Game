import random

class Settings:
    # paddle and appearance settings
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 153, 76)
        self.speedup_scale = 1.1
        self.vertical_paddle_width = 10
        self.vertical_paddle_height = self.screen_height / 4
        self.horizontal_paddle_width = self.screen_width / 8
        self.horizontal_paddle_height = 10
        self.ball_width = 10
        self.ball_height = 10
        self.paddle1_color = 0, 20, 150
        self.paddle2_color = 150, 20, 0
        self.ball_color = 255, 255, 0
        self.vertical_paddle_speed = self.screen_height/333
        self.horizontal_paddle_speed = self.screen_width/666
        self.ball_speedup = 1.05
        self.game_start = False
        self.initialize_dynamic_settings()

    # serve ball at random speed and angles
    def initialize_dynamic_settings(self):
        self.ball_rise = (random.randint(4, 7) * ((-1)**random.randint(1, 2)))/8
        self.ball_run = (random.randint(4, 7) * ((-1)**random.randint(1, 2)))/8
        self.ball_speed = random.uniform(.5, .5)