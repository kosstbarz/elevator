# coding=utf8


class Elevator(object):
    def __init__(self, levels, total_height):
        self.height = 0
        self.weight = 0
        self.speed = 0
        self.level = 1
        self.inner_door_open = 0
        self.plan = []
        self.buttons_pushed = {'inner': [], 'outer': []}
        self.level_height = total_height//levels
        self.levels = levels

    def __passtime(self):
        self.height += self.speed

    def __brain(self):
        if len(self.plan) == 0:
            self.plan_maker()
            if len(self.plan) == 0:
                self.speed = 0
                return
        self.inner_door_open = 1
        #here need to somehow wait till the person/ppl is/are in
        self.inner_door_open = 0
        plan_height = (self.plan[0] - 1)*self.level_height
        x = plan_height - self.height
        self.speed = x and (1, -1)[x < 0]
        self.level = (self.height + self.level_height)//self.level_height
        if self.height == plan_height:
            del self.plan[0]
            self.inner_door_open = 1
            # here need to somehow wait till the person/ppl is/are in
            self.inner_door_open = 0

    def push_outer(self, lev):
        self.buttons_pushed['outer'].append(lev)

    def push_inner(self, lev):
        self.buttons_pushed['inner'].append(lev)

    def plan_maker(self):
        if len(self.buttons_pushed['outer']) > 0 or len(self.buttons_pushed['inner']) > 0:
            a = self.buttons_pushed['outer'] + self.buttons_pushed['inner']
            for i in a:
                if i not in self.plan:
                    self.plan.append(i)
            self.buttons_pushed['outer'] = []
            self.buttons_pushed['inner'] = []

    def timestep(self, time):
        for i in range(time):
            self.__brain()
            self.__passtime()
