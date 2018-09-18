from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here


def move_from_point1_to_point2():
    x, y = 203, 535
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(5)


def move_from_point2_to_point3():
    pass


def move_from_point3_to_point4():
    pass


def move_from_point4_to_point5():
    pass


def move_from_point5_to_point6():
    pass


def move_from_point6_to_point7():
    pass


def move_from_point7_to_point8():
    pass


def move_from_point8_to_point9():
    pass


def move_from_point9_to_point10():
    pass


def move_from_point10_to_point1():
    pass


def move_loop():
    move_from_point1_to_point2()
    move_from_point2_to_point3()
    move_from_point3_to_point4()
    move_from_point4_to_point5()
    move_from_point5_to_point6()
    move_from_point6_to_point7()
    move_from_point7_to_point8()
    move_from_point8_to_point9()
    move_from_point9_to_point10()
    move_from_point10_to_point1()

    pass


move_from_point1_to_point2()

close_canvas()
