import pico2d
import play_mode

pico2d.open_canvas(play_mode.window_width, play_mode.window_height)
pico2d.hide_cursor()
play_mode.init()

# game loop
while play_mode.running:
    play_mode.handle_events()
    play_mode.update()
    play_mode.draw()
    # delay(0.01)

play_mode.finish()
pico2d.close_canvas()