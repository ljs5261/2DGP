import random

from pico2d import *


class FixedBall:

    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(0, 1800)  # 이미지에서의 x좌표값 설정
        self.y = random.randint(0, 1000)  # 이미지에서의 y좌표값 설정

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)

    def update(self):
        pass

    def handle_event(self, event):
            pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


