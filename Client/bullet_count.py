from pico2d import load_image
import game_world
import play_mode
import game_framework


class BulletCount:
    image = None
    def __init__(self, idx=0, x=0, y=0):
        if BulletCount.image == None:
            BulletCount.image = load_image('Resource\\png1\\gun-01.png')
        self.x, self.y = x, y
        self.idx = idx

    def draw(self):
        if play_mode.character.bullet_count > self.idx:
            self.image.draw(self.x, self.y, 150, 150)


    def update(self):
        pass

