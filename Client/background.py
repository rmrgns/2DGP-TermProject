from pico2d import load_image

class Background:
    image = None

    def __init__(self, x=0, y=0):
        if Background.image == None:
            Background.image = load_image('Resource\\tempbackground.png')
        self.x = x
        self.y = y
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass