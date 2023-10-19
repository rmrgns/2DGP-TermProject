from pico2d import *

import game_world
from background import Background
from character import Character
from ingameUI import InGameUI
from mousecontrol import MouseControl

window_width = 1600
window_height = 900
def handle_events():
    global running
    global mouse
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, window_height - 1 - event.y
        else:
            character.handle_event(event)

def create_world():
    global running
    global background
    global character
    global mouse
    running = True

    background = Background(window_width//2, window_height//2)
    game_world.add_object(background)

    character = Character()
    game_world.add_object(character, 2)

    ingameUI = InGameUI(window_width//2, 100)
    game_world.add_object(ingameUI, 1)

    mouse = MouseControl()
    game_world.add_object(mouse, 2)

def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas(window_width,window_height)
hide_cursor()
create_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    # delay(0.01)

# finalization code
close_canvas()