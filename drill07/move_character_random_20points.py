from pico2d import *
import random


ch_dir = 0    # 캐릭터가 바라보는 방향을 결정하는 값, 0이면 왼쪽, 1이면 오른쪽
moving_count = 0
total_moving_count = 30


class Grass:

    def __init__(self):
        self.image = load_image('grass.png')

        print(self.image)

    def draw(self):
        self.image.draw(400, 30)


class Boy:

    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.frame = random.randint(0, 7)

        self.speed = random.uniform(1.0, 3.0)

        self.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100 * ch_dir, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 8

    def move(self):
        global mouse_x, mouse_y, total_moving_count
        self.x += (mouse_x - self.x) / total_moving_count
        self.y += (mouse_y - self.y) / total_moving_count

    def choose_ch_dir(self):
        global ch_dir, mouse_x

        if mouse_x > self.x:  # 마우스 x 좌표가 캐릭터보다 오른쪽이면 캐릭터는 오른쪽을 바라본다.
            ch_dir = 1
        elif mouse_y < self.y:  # 마우스 y 좌표가 캐릭터보다 왼쪽이면 캐릭터는 왼쪽을 바라본다.
            ch_dir = 0


open_canvas()

g = Grass()

b = Boy()

running = True

while running:               # 캐릭터 위치 값 바꿔주기-> 방향 정하기-> 그리기

    while moving_count < total_moving_count:
        b.move()

        clear_canvas()

        g.draw()

        b.draw()

        update_canvas()
        moving_count += 1
        delay(0.03)

    moving_count = 0


