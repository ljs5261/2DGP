from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

running = True
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2  # 캐릭터의 최초 위치
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2  # 마우스 실시간 좌표 초기값
click_x, click_y = KPU_WIDTH // 2, KPU_HEIGHT // 2  # 마우스 클릭 좌표 초기값
frame = 0  # 프레임 0으로 초기화
ch_dir = 0  # 캐릭터가 바라보는 방향
moving_count = 0  # 몇번 이동했는지 세는 변수
total_moving_count = 200  # 총 몇 회에 걸쳐 마우스클릭지점까지 이동


def handle_events():
    global running
    global mouse_x, mouse_y
    global click_x, click_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            click_x, click_y = mouse_x - 20, mouse_y + 20             # 마우스클릭시 좌표값이 마우스 실시간좌표값보다
        # x 축으로 -20, y 축으로 +20
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_character():  # 캐릭터의 좌표값을 바꿔줌
    global character_x, character_y, click_x, click_y, total_moving_count
    character_x = character_x + (click_x - character_x) / total_moving_count
    character_y = character_y + (click_y - character_y) / total_moving_count


def choose_ch_dir():
    global ch_dir, character_x, click_x

    if click_x > character_x:  # 마우스클릭이 캐릭터보다 오른쪽이면 캐릭터는 오른쪽을 바라본다.
        ch_dir = 1
    elif click_x < character_x:  # 마우스클릭이 캐릭터보다 왼쪽이면 캐릭터는 왼쪽을 바라본다.
        ch_dir = 0


def draw_character():
    global frame, character_x, character_y, ch_dir
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(mouse_x, mouse_y)
    character.clip_draw(frame * 100, 100 * ch_dir, 100, 100, character_x, character_y)
    update_canvas()

    frame = (frame + 1) % 8


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')
hide_cursor()

while running:  # 캐릭터가 이동하고 마우스를 클릭하는 것은 계속 반복

    while moving_count < total_moving_count:  # 총 몇 회 이동으로 마우스클릭지점까지의 이동 구현
        move_character()
        choose_ch_dir()
        draw_character()
        moving_count += 1
        handle_events()                     # 실시간으로 마우스 좌표값을 가져옴

    moving_count = 0  # 0으로 초기화 해줘야 안쪽 while 문으로 다시 들어감
    delay(0.05)


close_canvas()
