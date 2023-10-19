from pico2d import load_image

class Character:
    def __init__(self):
        self.x, self.y = 110,110
        self.frame = 0
        self.image = load_image('Resource//tempcharacter.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
    def update(self):

        pass

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class StateMachine:
    def __init__(self, character):
        self.character = character
        self.cur_state = None
        self.transitions = {}

    def start(self):
        pass

    def update(self):
        pass

    def handle_event(self, e):
        pass

    def draw(self):
        self.character.draw()