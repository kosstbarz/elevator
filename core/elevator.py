# coding=utf8

class Elevator (object):
    def __init__(self, num_lev, height_lev):
        self.height = 0
        self.weight = 0
        self.speed = 0
        self.level = 1
        self.inner_door_open = 0
        self.buttons_pushed = {'inner': [], 'outer': []}

    def push_outer(self, lev):
        self.buttons_pushed['outer'] = lev

    def timestep(self, time):
        if self.buttons_pushed['outer']:
            if self.buttons_pushed['outer'] != self.level:
                self.level = self.buttons_pushed['outer']
                self.height = self.buttons_pushed['outer'] + 1



