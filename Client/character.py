from pico2d import load_image
from sdl2 import SDL_KEYUP, SDL_KEYDOWN, SDLK_RIGHT, SDLK_LEFT, SDLK_SPACE, SDLK_a, SDLK_d, SDL_MOUSEBUTTONDOWN

import game_framework
import game_world
from bullet import Bullet
import play_mode

window_width = 1600
PIXEL_PER_METER = (1600.0 / 15.0) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def shot(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN

##
animation_names = ['1']

class Character:
    def __init__(self):
        self.x, self.y = 800,270
        self.frame = 0
        self.action = 0
        self.dir = 0
        self.face_dir = 1
        self.size_x, self.size_y = 80, 134
        self.bullet_spread = 0.02
        self.bullet_count = 10
        self.fire_count = 2
        self.image = {}
        for name in animation_names:
            self.image[name] = [load_image("Resource\\png1\\Run\\" + name + "-%d" % i + ".png") for i in range(1, 8)]
        # self.image = load_image("Resource\\png1\\Run\\1-1.png")
        self.state_machine = StateMachine(self)
        self.state_machine.start()
    def update(self):
        self.state_machine.update()
        if self.x > play_mode.mouse.x:
            self.face_dir = -1
        else:
            self.face_dir = 1

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def dash(self):
        self.x += self.dir * 200
        if self.x < 10:
            self.x = 10
        elif self.x > window_width:
            self.x = window_width

    def fire(self):
        if play_mode.mouse.y > self.y and self.fire_count > 0:
            for i in range(0, self.bullet_count):
                ratio = abs(play_mode.mouse.x-self.x) / (abs(play_mode.mouse.x-self.x) + (play_mode.mouse.y-self.y))
                bullet = Bullet(self.x, self.y, ratio + self.bullet_spread * i - (self.bullet_spread * (self.bullet_count / 2)), self.face_dir, i)
                game_world.add_object(bullet)
                game_world.add_collision_pair('bullet:clay', bullet, None)
            self.fire_count -= 1

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
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        pass

    @staticmethod
    def draw(character):
        if character.face_dir == -1:
            character.image['1'][int(character.frame)].composite_draw(0, 'h', character.x, character.y, character.size_x, character.size_y, )
        else:
            character.image['1'][int(character.frame)].draw(character.x, character.y, character.size_x, character.size_y)

class Run:

    @staticmethod
    def enter(character, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            character.dir, character.action = 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            character.dir, character.action = -1, 0

    @staticmethod
    def exit(character, e):
        if space_down(e):
            character.dash()
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        character.x += character.dir * RUN_SPEED_PPS * game_framework.frame_time
        if character.x < 10:
            character.x = 10
        elif character.x > window_width:
            character.x = window_width
        pass

    @staticmethod
    def draw(character):
        if character.face_dir == -1:
            character.image['1'][int(character.frame)].composite_draw(0, 'h', character.x, character.y,
                                                                      character.size_x, character.size_y, )
        else:
            character.image['1'][int(character.frame)].draw(character.x, character.y, character.size_x,
                                                            character.size_y)
