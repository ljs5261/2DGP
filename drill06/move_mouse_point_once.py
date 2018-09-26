from pico2d import *
import math
open_canvas()


character = load_image('animation_sheet.png')


def handle_events():
    global running
    global click_x, click_y
    events = get_events()                        # 이벤트들을 다 가져옴
    for event in events:                        # 하나하나 가져와서 검사
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click_x, click_y = event.x, 600 - 1 - event.y
        elif event.key == SDLK_ESCAPE:
            running = False


click_x, click_y = 800 // 2, 600 // 2


def move_from_point_to_next_point():
    frame = 0

    x1, y1 = 800 // 2, 600 // 2


    d_x = abs(x1 - click_x) / 50  # x축 방향의 프레임사이의 거리
    d_y = abs(y1 - click_y) / 50  # y축 방향의 프레임사이의 거리

    if x1 - click_x > 0:         # x1이 더 큰 경우
        while x1 > click_y:
            clear_canvas()

            character.clip_draw(frame * 100, 200, 100, 100, x1, click_y)  # 왼쪽을 바라봄
            update_canvas()
            frame = (frame + 1) % 8
            x1 -= d_x
            if y1 - click_y > 0:   # y1이 y2보다 더 크면 y1 감소
                y1 -= d_y
            else:             # y1이 y2보다 더 작으면 y1 증가
                y1 += d_y
            delay(0.05)
            handle_events()
    else:                   # x2가 더 큰 경우
        while x1 < click_x:
            clear_canvas()

            character.clip_draw(frame * 100, 300, 100, 100, x1, y1)   # 오른쪽을 바라봄
            update_canvas()
            frame = (frame + 1) % 8
            x1 += d_x
            if y1 - click_y > 0:
                y1 -= d_y
            else:
                y1 += d_y
            delay(0.05)
            handle_events()

def move_loop():
    while True:
        move_from_point_to_next_point()


move_loop()
close_canvas()
