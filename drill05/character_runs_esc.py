from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('ataho1.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
x = 0
frame = 5
y = 90
while x < 800 and running:

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 38, 0, 38, 60, x, y)
    update_canvas()
    handle_events()
    if frame >= 11:
        frame = frame - 6
    frame = (frame + 1) % 11
    x += 5
    delay(0.5)



close_canvas()
