from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1000, 700

ch_dir = 0    # 캐릭터가 바라보는 방향을 결정하는 값, 0이면 왼쪽, 1이면 오른쪽
moving_count = 0
total_moving_count = 100 + 1
t = 0
size = 4
points = [(random.randint(50,900), random.randint(50,600)) for i in range(size)]   # 랜덤한 좌표 10개 생성
n = 1
draw_n_time = 1

class Kpu_Ground:

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
        global ch_dir, n
        tuple1 = points[n-1]
        tuple2 = points[n]
        if tuple2[0] > tuple1[0]:  # 다음포인트의 x 좌표가 이전포인트의 x 좌표보다 오른쪽이면 캐릭터는 오른쪽을 바라본다.
            ch_dir = 1
        elif tuple2[0] < tuple1[0]:  # 다음포인트의 x 좌표가 이전포인트의 x 좌표보다 왼쪽이면 캐릭터는 왼쪽을 바라본다.
            ch_dir = 0

    def move_curve(self, p1, p2, p3, p4):
        global moving_count, t, cut_point_to_point

        # draw p1-p2            # p4, p1, p2, p3 네 개 점의 100프로
        if draw_n_time == 1:
            t = moving_count / 100
            self.x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                        -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
            self.y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2

        # draw p2-p3             # p1, p2, p3, p4 네 개의 점의 100프로
        elif draw_n_time == 2:
            t = moving_count / 100
            self.x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
            self.y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

        # draw p3-p4            # p2, p3, p4, p1 네 개의 점의 100프로
        elif draw_n_time == 3:
            t = moving_count/ 100
            self.x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
            self.y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2

        # draw p4-p1                 # p3, p4, p1, p2의 100프로
        elif draw_n_time == 4:
            t = moving_count / 100
            self.x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
            self.y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                            -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2


open_canvas(KPU_WIDTH, KPU_HEIGHT)

g = Kpu_Ground()

b = Boy()


running = True

while running:               # 캐릭터 위치 값 바꿔주기-> 방향 정하기-> 그리기
        b.choose_ch_dir()
        while moving_count < total_moving_count:
            b.move_curve(points[0], points[1], points[2], points[3])

            clear_canvas()

            g.draw()

            b.draw()

            update_canvas()
            moving_count += 2

            delay(0.05)

        n = (n + 1) % 4
        draw_n_time += 1
        moving_count = 0
        if draw_n_time == 5:
            draw_n_time = 1
