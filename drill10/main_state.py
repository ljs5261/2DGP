import game_framework
from pico2d import *
from Boy import *
from grass import *
import base_pause_state


boy = None
grass = None
first_start = 1


def enter():
    global boy, grass, first_start
    if first_start == 1:
        open_canvas()
        boy = Boy()
        grass = Grass()
        first_start += 1
    else:
        open_canvas()
        boy = Boy()
        grass = Grass()
        boy.start_pause_next()


def exit():
    global boy, grass
    del(boy)
    del(grass)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:          # p키가 눌리면
            game_framework.push_state(base_pause_state)                      # 타이틀화면으로 전환


def update():
    global boy
    boy.update()


def draw():
    global boy, grass
    clear_canvas()
    grass.draw()
    boy.draw()

    update_canvas()
    delay(0.04)


def pause():
    boy.pause()


def resume():
    pass