from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1000, 700

ch_dir = 0    # 캐릭터가 바라보는 방향을 결정하는 값, 0이면 왼쪽, 1이면 오른쪽
moving_count = 0
total_moving_count = 100 + 1
t = 0
size = 20
points = [(random.randint(50,900), random.randint(50,600)) for i in range(size)]
n = 1


class KPU_GROUND:

    def __init__(self):
        self.image = load_image('KPU_GROUND.png')

        print(self.image)

    def draw(self):
        self.image.draw(KPU_WIDTH//2, KPU_HEIGHT//2)


class Boy:

    def __init__(self):
        self.x = KPU_WIDTH//2
        self.y = KPU_HEIGHT//2
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100 * ch_dir, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 8

    def choose_ch_dir(self):
        global ch_dir
        tuple1 = points[n-1]
        tuple2 = points[n]
        if tuple2[0] > tuple1[0]:  # 다음포인트의 x 좌표가 이전포인트의 x 좌표보다 오른쪽이면 캐릭터는 오른쪽을 바라본다.
            ch_dir = 1
        elif tuple2[0] < tuple1[0]:  # 다음포인트의 x 좌표가 이전포인트의 x 좌표보다 왼쪽이면 캐릭터는 왼쪽을 바라본다.
            ch_dir = 0
        pass

    def move_line(self, p1, p2):
        global moving_count, t

        t = moving_count / 100
        self.x = (1 - t) * p1[0] + t * p2[0]
        self.y = (1 - t) * p1[1] + t * p2[1]


open_canvas(KPU_WIDTH, KPU_HEIGHT)

g = KPU_GROUND()

b = Boy()


running = True

while running:               # 캐릭터 위치 값 바꿔주기-> 방향 정하기-> 그리기

    while moving_count < total_moving_count:
        b.move_line(points[n-1], points[n])
        b.choose_ch_dir()
        clear_canvas()

        g.draw()

        b.draw()

        update_canvas()
        moving_count += 2

        delay(0.05)

    n = (n + 1) % size
    moving_count = 0

