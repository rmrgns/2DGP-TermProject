from pico2d import load_image

class Background:
    image = None

    def __init__(self, x=1920, y=1080):
        if Background.image == None:
            Background.image = load_image('Resource\\background.png')
        self.x = x
        self.y = y
    def draw(self):
        self.image.draw(self.x, self.y,1600,700)

    def update(self):
        pass