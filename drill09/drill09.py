from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 8

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5


class SmallBall:
    def __init__(self):             # 객체 생성시 이미지 받아오고 좌표값, 속도값 정해줌

        self.image = load_image('ball21x21.png')
        self.x = random.randint(20, 780)
        self.y = 600
        self.speed = random.uniform(2.0, 5.0)   # 2.0 , 5.0 사이의 임의의 실수 생성

    def draw_ball(self):
        self.image.draw(self.x, self.y)

    def drop_ball(self):
        if self.y >= 65:            # 축구공이 멈출 y 좌표값 지정
            self.y -= self.speed


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

g = Grass()

boys = []

for i in range(20):
    boys += [Boy()]

running = True

# game main loop code
while running:
    handle_events()
    for boy in boys:
        boy.update()

    clear_canvas()
    g.draw()
    for boy in boys:
        boy.draw()
    update_canvas()

    delay(0.05)

