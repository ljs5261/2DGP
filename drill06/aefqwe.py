from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024              # 캔버스의 크기
open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global mouse_x
    global mouse_y
    global click_x
    global click_y
    events = get_events()                        # 이벤트들을 다 가져옴
    for event in events:                        # 하나하나 가져와서 검사
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click_x, click_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def change_direction():
    global dir
    if character_x < click_x:   # 오른쪽을 바라봄
        dir = 1
        return dir
    else:
        dir = 0
        return dir             # 왼쪽을 바라봄


def draw_character_and_mouse():
    global frame
    global character_x
    global character_y

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * change_direction(), 100, 100, character_x, character_y)
    hand_arrow.draw(mouse_x, mouse_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()


character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

running = True
while running:
    draw_character_and_mouse()


close_canvas()



