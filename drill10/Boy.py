from pico2d import *

ch_dir = 1
pause_x = 0


class Boy:

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.state = 2
        self.hp = 100

    def update(self):
        if self.x < 800:
            self.x = self.x + 5

    def start_pause_next(self):
        self.x = pause_x

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100 * ch_dir, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 8

    def pause(self):
        global pause_x
        pause_x = self.x

    def handle_event(self):
        pass