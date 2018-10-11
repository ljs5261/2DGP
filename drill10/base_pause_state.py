import game_framework
from pico2d import *
import main_state

name = "LogoState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    # del image


def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time=0
        # game_framework.quit()
        # game_framework.change_state(title_state)
        delay(0.01)

    logo_time += 0.002


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:         # p키가 눌리면
            game_framework.push_state(main_state)                 # 타이틀화면으로 전환


def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()

