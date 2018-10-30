
from boy import *
from grass import Grass
from ghost import Ghost

name = "MainState"

boy = None
grass = None
ghost = None


def enter():
    global boy, grass, ghost
    boy = Boy()
    grass = Grass()
    ghost = Ghost(boy)
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(ghost, 1)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    global boy, ghost
    boy.update()
    ghost.update(boy)


def draw():
    global boy, grass, ghost
    clear_canvas()
    grass.draw()
    boy.draw()
    ghost.draw()

    update_canvas()






