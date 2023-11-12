from pico2d import load_image
import game_world
import play_mode

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        if Bullet.image == None:
            Bullet.image = load_image('Resource\\bullet-1.png')
        self.x, self.y = x, y
        self.shot_x, self.shot_y = x, y
        self.velocity_x = play_mode.mouse.x
        self.velocity_y = play_mode.mouse.y


    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)

    def update(self):
        self.x += (self.velocity_x - self.shot_x) // 100
        self.y += (self.velocity_y -self.shot_y) // 100
        if self.x < 10 or self.x > 1600 - 10:
            game_world.remove_object(self)

