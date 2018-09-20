from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here

coordinate = [(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225),
(510, 92), (692, 518), (682, 336), (712, 349)]   # 좌표값 리스트


def move_from_point_to_next_point():
    frame = 0
    for i in range(0, 9):
        x1, y1 = coordinate[i]
        x2, y2 = coordinate[i+1]

        d_x = abs(x1 - x2) / 50  # x축 방향의 프레임사이의 거리
        d_y = abs(y1 - y2) / 50  # y축 방향의 프레임사이의 거리

        if x1 - x2 > 0:         # x1이 더 큰 경우
            while x1 > x2:
                clear_canvas()
                grass.draw(400, 30)
                character.clip_draw(frame * 100, 200, 100, 100, x1, y1)  # 왼쪽을 바라봄
                update_canvas()
                frame = (frame + 1) % 8
                x1 -= d_x
                if y1 - y2 > 0:   # y1이 y2보다 더 크면 y1 감소
                    y1 -= d_y
                else:             # y1이 y2보다 더 작으면 y1 증가
                    y1 += d_y
                delay(0.05)
                get_events()
        else:                   # x2가 더 큰 경우
            while x1 < x2:
                clear_canvas()
                grass.draw(400, 30)
                character.clip_draw(frame * 100, 300, 100, 100, x1, y1)   # 오른쪽을 바라봄
                update_canvas()
                frame = (frame + 1) % 8
                x1 += d_x
                if y1 - y2 > 0:
                    y1 -= d_y
                else:
                    y1 += d_y
                delay(0.05)
                get_events()


def move_from_point10_to_point1():
    frame = 0

    x1, y1 = coordinate[9]
    x2, y2 = coordinate[0]

    d_x = abs(x1 - x2) / 50  # x축 방향의 프레임사이의 거리
    d_y = abs(y1 - y2) / 50  # y축 방향의 프레임사이의 거리

    if x1 - x2 > 0:              # x1이 더 큰 경우
        while x1 > x2:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 200, 100, 100, x1, y1)  # 왼쪽을 바라봄
            update_canvas()
            frame = (frame + 1) % 8
            x1 -= d_x
            if y1 - y2 > 0:    # y1이 y2보다 더 크면 y1 감소
                y1 -= d_y
            else:              # y1이 y2보다 더 작으면 y1 증가
                y1 += d_y
            delay(0.05)
            get_events()
    else:                       # x2가 더 큰 경우
        while x1 < x2:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 300, 100, 100, x1, y1)  # 오른쪽을 바라봄
            update_canvas()
            frame = (frame + 1) % 8
            x1 += d_x
            if y1 - y2 > 0:
                y1 -= d_y
            else:
                y1 += d_y
            delay(0.05)
            get_events()


def move_loop():
    while True:
        move_from_point_to_next_point()
        move_from_point10_to_point1()


move_loop()
close_canvas()
