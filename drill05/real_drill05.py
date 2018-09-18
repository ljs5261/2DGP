from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here


def move_from_point1_to_point2():
    x1, y1 = 203, 535
    x2, y2 = 132, 243
    d_x = abs(x1 - x2) / 50  # x축 방향의 프레임사이의 거리
    d_y = abs(y1 - y2) / 50  # y축 방향의 프레임사이의 거리
    while x1 > x2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x1, y1)

        x1 -= d_x
        y1 -= d_y
        delay(0.05)


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
