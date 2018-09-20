from pico2d import *


def handle_events():
    global running
    global dir_
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_ += 1
            elif event.key == SDLK_LEFT:
                dir_ -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_ -= 1
            elif event.key == SDLK_LEFT:
                dir_ += 1


open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 800 // 2
y = 90
frame = 0
dir_ = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_ * 5
    delay(0.05)
    get_events()
    
close_canvas()
