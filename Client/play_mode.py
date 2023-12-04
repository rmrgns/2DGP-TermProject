from pico2d import *

import game_world
import game_framework
from fire_count import FireCount
from background import Background
from character import Character
from ingameUI import InGameUI
from mousecontrol import MouseControl

window_width = 1600
window_height = 900
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, window_height - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            character.fire()
        else:
            character.handle_event(event)

def init():

    global background
    global character
    global mouse

    background = Background(window_width//2, window_height//2 + 100)
    game_world.add_object(background)

    character = Character()
    game_world.add_object(character, 2)

    ingameUI = InGameUI(window_width//2, 100)
    game_world.add_object(ingameUI, 1)

    mouse = MouseControl()
    game_world.add_object(mouse, 2)

    for i in range(2):
        firecountUI = FireCount(i, 850 - 150 * i, 100)
        game_world.add_object(firecountUI, 1)

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
