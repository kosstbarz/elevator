# coding=utf8

class Elevator (object):
    def __init__(self, num_lev, height_lev):
        self.height = 0
        self.weight = 0
        self.speed = 0
        self.level = 1
        self.inner_door_open = 0
        self.buttons_pushed = {'inner': [], 'outer': []}

    def wait(self, time):
        pass

    def push_outer(self, lev):
        self.wait(self)
        self.level = lev
        self.height = 1 + lev
