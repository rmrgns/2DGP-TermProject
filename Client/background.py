import random

from pico2d import load_image, get_time

import game_world
from spawn import Spawn


class Background:
    image = None

    def __init__(self, x=1920, y=1080):
        if Background.image == None:
            Background.image = load_image('Resource\\background.png')
        self.x = x
        self.y = y
        self.spawn_time = get_time()
        global spawn

    def draw(self):
        self.image.draw(self.x, self.y,1600,700)

    def update(self):
        if get_time() - self.spawn_time > 5:
            x = random.randint(1200, 1500)
            spawn = Spawn(x)
            game_world.add_object(spawn, 2)
            self.spawn_time = get_time()
        pass
