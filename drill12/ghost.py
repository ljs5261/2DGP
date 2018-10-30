from pico2d import *
import math
import game_framework

PIXEL_PER_METER = (10.0/ 0.3)
RUN_SPEED_KMPH = 20.0 # 마라토너속도
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

SLEEP_TIMER, ACTIVE_TIMER, CIRCLE_TIMER = range(3)

theta = math.pi / 2
r = 100


class CircleState:

    @staticmethod
    def enter(ghost, event, b):
        pass

    @staticmethod
    def exit(ghost, event):
        pass

    @staticmethod
    def do(ghost, b):
        global theta, r
        ghost.x = b.x + (r * math.cos(theta))
        ghost.y = b.y + (r * math.sin(theta))
        theta += 4 * math.pi * game_framework.frame_time

    @staticmethod
    def draw(ghost):
        ghost.image.clip_draw(0, 300, 100, 100, ghost.x, ghost.y)


class ActiveState:

    @staticmethod
    def enter(ghost, event, b):
        pass

    @staticmethod
    def exit(ghost, event):
        pass

    @staticmethod
    def do(ghost, b):
        if ghost.y <= 190:  # boy의 y값이 90이므로 100pixel만큼 이동, 100pixel = 3M
            ghost.y += 1
        if ghost.y == 190:
            ghost.add_event(CIRCLE_TIMER)

    @staticmethod
    def draw(ghost):
        ghost.image.clip_draw(0, 300, 100, 100, ghost.x, ghost.y)


class SleepState:

    @staticmethod
    def enter(ghost, event, b):
        ghost.prev_time = b.prev_time

    @staticmethod
    def exit(ghost, event):
        pass

    @staticmethod
    def do(ghost, b):
        ghost.x = b.x
        ghost.curr_time = b.curr_time
        if ghost.curr_time - ghost.prev_time >= 10.0:
            ghost.add_event(ACTIVE_TIMER)

    @staticmethod
    def draw(ghost):
        pass


next_state_table = {
    SleepState: {ACTIVE_TIMER: ActiveState},
    ActiveState: {SLEEP_TIMER: SleepState, CIRCLE_TIMER: CircleState
                  }

}


class Ghost:
    def __init__(self, b):
        self.x, self.y = b.x, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = SleepState
        self.cur_state.enter(self, None, b)
        self.prev_time = 0
        self.curr_time = 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self, b):
        self.cur_state.do(self, b)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event, b)

    def draw(self):
        self.cur_state.draw(self)


