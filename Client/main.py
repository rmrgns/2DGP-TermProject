import pico2d
import play_mode as start_mode
import game_framework

window_width = 1600
window_height = 900

pico2d.open_canvas(window_width, window_height)
pico2d.hide_cursor()
game_framework.run(start_mode)
#
# play_mode.init()
#
#
# # game loop
# while play_mode.running:
#     play_mode.handle_events()
#     play_mode.update()
#     play_mode.draw()
#     # delay(0.01)
#
# play_mode.finish()
pico2d.close_canvas()