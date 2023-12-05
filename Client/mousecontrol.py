from pico2d import load_image


class MouseControl:
    image = None
    def __init__(self):
        if MouseControl.image == None:
            self.image = load_image('Resource\\MouseIcon.png')
        self.x, self.y = 100,100

    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)

    def update(self):
        pass


    def shot(self):
        # print('shot')
        pass