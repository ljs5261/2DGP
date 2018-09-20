from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()  # 이벤트들을 다 가져옴
    for event in events:  # 하나하나 빼서 검사
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
ground_x, ground_y = KPU_WIDTH // 2, KPU_HEIGHT // 2            # kpu 배경이미지 좌표
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2            # 캐릭터의 최초 좌표
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(ground_x, ground_y)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()        # 마우스클릭 좌표값으로 x, y를 갱신
    frame = (frame + 1) % 8

    delay(0.05)

close_canvas()
