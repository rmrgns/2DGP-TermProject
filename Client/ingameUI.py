from pico2d import load_image

class InGameUI:
    image = None
    UIbackground = None
    def __init__(self, x=0, y=0):
        if InGameUI.image == None:
            InGameUI.image = load_image('Resource\\IngameUI.png')
        if InGameUI.UIbackground == None:
            InGameUI.UIbackground = load_image('Resource\\tempUI.png')
        self.x = x
        self.y = y
    def draw(self):
        self.UIbackground.draw(self.x, self.y, 1600, 200)
        self.image.draw(self.x, self.y, 1600, 200)


    def update(self):
        pass