import random

from pico2d import load_image, get_time
import game_world
import play_mode
from clay import Clay


class Spawn:
    def __init__(self, x=800):
        self.x, self.y = x, 250
        self.time = get_time()
        self.clay_count = 20
        global clays
        clays = [Clay(random.randint(x-100,x+100), self.y) for _ in range(self.clay_count)]
        game_world.add_objects(clays, 2)
    def draw(self):
        pass

    def update(self):
        if get_time() - self.time >= 3.0:

            game_world.remove_object(self)

    def makeclay(self):
        for n in range(0, self.clay_count):
            clay = Clay()
        pass
