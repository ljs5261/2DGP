from pico2d import *
import random


ch_dir = 0    # 캐릭터가 바라보는 방향을 결정하는 값, 0이면 왼쪽, 1이면 오른쪽
moving_count = 0
total_moving_count = 100 + 1
t = 0
p1 =(400,300)
p2 = (600,500 )

class Grass:

    def __init__(self):
        self.image = load_image('grass.png')

        print(self.image)

    def draw(self):
        self.image.draw(400, 30)


class Boy:

    def __init__(self):
        self.x = 0
        self.y = 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100 * ch_dir, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 8

    def move(self):
        global total_moving_count
        self.x += 5
        self.y += 5

        pass

    def choose_ch_dir(self):
        global ch_dir, mouse_x

        if mouse_x > self.x:  # 마우스 x 좌표가 캐릭터보다 오른쪽이면 캐릭터는 오른쪽을 바라본다.
            ch_dir = 1
        elif mouse_y < self.y:  # 마우스 y 좌표가 캐릭터보다 왼쪽이면 캐릭터는 왼쪽을 바라본다.
            ch_dir = 0
        pass

    def move_line(self, p1, p2):
        global moving_count, t
         # for i in range(0, 100 + 1, 2):
        t = moving_count / 100
        self.x = (1 - t) * p1[0] + t * p2[0]
        self.y = (1 - t) * p1[1] + t * p2[1]


open_canvas()

g = Grass()

b = Boy()

running = True

while running:               # 캐릭터 위치 값 바꿔주기-> 방향 정하기-> 그리기

    while moving_count < total_moving_count:
        b.move_line(p1, p2)

        clear_canvas()

        g.draw()

        b.draw()

        update_canvas()
        moving_count += 2
        delay(0.03)

    moving_count = 0


