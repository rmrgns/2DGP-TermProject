import random

from pico2d import load_image
import game_world
import play_mode
import game_framework


class Clay:
    image = None
    imageCoin = None
    imageSpaceShip = None
    imageBomb = None
    def __init__(self, x=400, y=300, dir = -1):
        if Clay.image == None:
            Clay.image = load_image('Resource\\clay_coin.png')

        self.x, self.y = x, y
        self.delete_line = y - 50
        self.dir = dir
        self.image_num = random.randint(0,5)
        self.velocity_x = random.randint(100, 150)
        self.velocity_y = random.randint(1000, 1500)

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)

    def update(self):
        if self.y < self.delete_line:
            game_world.remove_object(self)

        self.x += self.velocity_x * game_framework.frame_time * self.dir
        self.y += self.velocity_y * game_framework.frame_time
        self.calculate_velocity()


    def calculate_velocity(self):
        self.velocity_y -= 10

    def delete_clay(self):
        game_world.remove_object(self)