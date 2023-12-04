import math

from pico2d import load_image
import game_world
import play_mode
import game_framework


class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, ratio = 0 ,dir = 1, idx = 0):
        if Bullet.image == None:
            Bullet.image = load_image('Resource\\bullet-1.png')
        self.x, self.y = x, y
        self.ratio = ratio
        self.dir = dir
        self.rad = self.calculate_rad()
        self.inx = idx

    def draw(self):
        self.image.composite_draw(self.rad, '', self.x, self.y, 100, 100)

    def update(self):
        self.x += self.ratio * 1000 * game_framework.frame_time * self.dir
        self.y += (1-self.ratio) * 1000 * game_framework.frame_time
        if self.x < 10 or self.x > 1600 - 10:
            game_world.remove_object(self)

    def calculate_rad(self):
        delta_y = play_mode.mouse.y - self.y
        delta_x = play_mode.mouse.x - self.x

        # 아크탄젠트를 사용하여 기울기(라디안) 계산
        slope_rad = math.atan2(delta_y, delta_x)

        return slope_rad
