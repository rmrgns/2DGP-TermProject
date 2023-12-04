import math

from pico2d import load_image
import game_world
import play_mode
import game_framework

PIXEL_PER_METER = (1600.0 / 15.0) # 10 pixel 30 cm
BULLET_SPEED_KMPH = 100.0 # Km / Hour
BULLET_SPEED_MPM = (BULLET_SPEED_KMPH * 1000.0 / 60.0)
BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60.0)
BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)
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
        self.x += self.ratio * BULLET_SPEED_PPS * game_framework.frame_time * self.dir
        self.y += (1-self.ratio) * BULLET_SPEED_PPS * game_framework.frame_time
        if self.x < 10 or self.x > 1600 - 10:
            game_world.remove_object(self)

    def calculate_rad(self):
        delta_y = play_mode.mouse.y - self.y
        delta_x = play_mode.mouse.x - self.x

        # 아크탄젠트를 사용하여 기울기(라디안) 계산
        slope_rad = math.atan2(delta_y, delta_x)

        return slope_rad

    def handle_collision(self, group, other):
        if group == 'bullet:clay':
            pass

    def get_bb(self):
        return self.x, self.y, self.x, self.y