from pico2d import load_image


class MouseControl:
    def __init__(self):
        self.image = load_image('Resource\\tempmouse.png')

        self.x, self.y = 0,0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass