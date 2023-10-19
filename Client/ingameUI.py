from pico2d import load_image

class InGameUI:
    image = None

    def __init__(self, x=0, y=0):
        if InGameUI.image == None:
            InGameUI.image = load_image('Resource\\tempUI.png')
        self.x = x
        self.y = y
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass