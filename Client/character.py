from pico2d import load_image
from sdl2 import SDL_KEYUP, SDL_KEYDOWN, SDLK_RIGHT, SDLK_LEFT, SDLK_SPACE


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


class Character:
    def __init__(self):
        self.x, self.y = 800,250
        self.frame = 0
        self.action = 0
        self.dir = 0
        self.face_dir = 1

        self.image = load_image('Resource//tempcharacter.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start()
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

class StateMachine:
    def __init__(self, character):
        self.character = character
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down:Run, left_up: Run, right_up:Run, space_down: Idle},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
        }

    def start(self):
        self.cur_state.enter(self.character, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.character)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.character, e)
                self.cur_state = next_state
                self.cur_state.enter(self.character, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.character)

class Idle:
    @staticmethod
    def enter(character, e):
        if character.face_dir == -1:
            character.action = 2
        elif character.face_dir == 1:
            character.action = 3
        character.dir = 0
        character.frame = 0
        pass

    @staticmethod
    def exit(character, e):
        pass

    @staticmethod
    def do(character):
        # character.frame = (character.frame + 1) % 8
        pass

    @staticmethod
    def draw(character):
        character.image.clip_draw(character.frame * 100, 0, 50, 100, character.x, character.y)


class Run:

    @staticmethod
    def enter(character, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            character.dir, character.face_dir, character.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            character.dir, character.face_dir, character.action = -1, -1, 0

    @staticmethod
    def exit(character, e):
        pass

    @staticmethod
    def do(character):
        # character.frame = (character.frame + 1) % 8
        character.x += character.dir * 5
        pass

    @staticmethod
    def draw(character):
        character.image.clip_draw(character.frame * 100, 0, 50, 100, character.x, character.y)
