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

    def wait(self, time):
        pass

    def timestep(self, time):
        if self.buttons_pushed['outer']:
            self.inner_door_open = 1
            if self.weight > 0:
                self.inner_door_open = 0
            if self.buttons_pushed['outer'] != self.level:
                if self.buttons_pushed['outer'] - self.level > 0:
                    while self.level != self.buttons_pushed['outer']:
                        self.wait(5)
                        self.speed = (self.buttons_pushed['outer'] - self.level)/time
                        self.height += 1
                        self.level += 1
                else:
                    while self.level != self.buttons_pushed['outer']:
                        self.wait(5)
                        self.speed = (self.buttons_pushed['outer'] - self.level)/time
                        self.height -= 1
                        self.level -= 1
                if self.level == self.buttons_pushed['outer']:
                    self.speed = 0
                    self.inner_door_open = 1
                if self.weight == 0:
                    self.inner_door_open = 0
                    self.buttons_pushed['outer'] = []
            if not self.buttons_pushed['outer']:
                if self.buttons_pushed['inner'] != self.level:
                    if self.buttons_pushed['inner'] - self.level > 0:
                        while self.level != self.buttons_pushed['inner']:
                            self.wait(5)
                            self.speed = (self.buttons_pushed['inner'] - self.level) / time
                            self.height += 1
                            self.level += 1
                    else:
                        while self.level != self.buttons_pushed['inner']:
                            self.wait(5)
                            self.speed = (self.buttons_pushed['inner'] - self.level) / time
                            self.height -= 1
                            self.level -= 1
                    self.level = self.buttons_pushed['inner']
                    self.height = self.level + 1
                    if self.level == self.buttons_pushed['inner']:
                        self.speed = 0
                        self.inner_door_open = 1
                    if self.weight == 0:
                        self.inner_door_open = 0
                        self.buttons_pushed['inner'] = None

    def push_inner(self, lev):
        self.buttons_pushed['inner'] = lev

