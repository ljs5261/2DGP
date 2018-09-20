from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x = 90
y = 90
frame = 0
while x < 800:
    clear_canvas()
    grass.draw_now(400, 30)
    character.clip_draw(frame * 400, 100, 100, 100, x, y)
    frame = (frame + 1) % 8

    update_canvas()
    delay(0.05)
    get_events()
    
close_canvas()
