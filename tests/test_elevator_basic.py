# coding=utf8

import unittest
from core.elevator import Elevator

class Test_elevator_state(unittest.TestCase):

    def setUp(self):
        self.elevator = Elevator(5, 15)

    def test_wait(self):
        self.elevator.timestep(10)

    def test_check_height(self):
        self.assertEqual(self.elevator.height, 0)

    def test_check_door_close(self):
        self.assertEqual(self.elevator.inner_door_open, 0)

    def test_check_level(self):
        self.assertEqual(self.elevator.level, 1)

    def test_check_speed(self):
        self.assertEqual(self.elevator.speed, 0)

    def test_check_weight(self):
        self.assertEqual(self.elevator.weight, 0)

    def test_check_buttons(self):
        self.assertEqual(self.elevator.buttons_pushed, {'inner': [], 'outer': []})

class Test_elevator_transitions(unittest.TestCase):
    def setUp(self):
        self.elevator = Elevator(5, 15)

    def test_door_after_push(self):
        self.elevator.push_outer(2)
        self.elevator.timestep(1)
        self.assertEqual(self.elevator.inner_door_open, 0)

class Test_elevator_movement(unittest.TestCase):
    def setUp(self):
        self.elevator = Elevator(5, 15)

    def test_go_to_level(self):
        self.elevator.timestep(10)
        self.elevator.push_outer(2)
        self.elevator.timestep(100)
        self.assertEqual(self.elevator.height, 3)
        self.assertEqual(self.elevator.level, 2)

    def test_go_down(self):
        self.elevator.push_outer(2)
        self.elevator.timestep(100)
        self.elevator.push_inner(1)
        self.elevator.timestep(100)
        self.assertEqual(self.elevator.height, 0)
        self.assertEqual(self.elevator.level, 1)

class Test_elevator_doors(unittest.TestCase):
    def setUp(self):
        self.elevator = Elevator(5, 15, 1, 3, 1)

    def test_let_people_come(self):
        self.elevator.push_outer(2)
        self.elevator.timestep(3)
        self.assertEqual(self.elevator.height, 3)
        self.assertEqual(self.elevator.level, 1)
        self.assertEqual(self.elevator.inner_door_open, 0)
        self.elevator.timestep(3)
        self.assertEqual(self.elevator.inner_door_open, 1)
        self.elevator.timestep(1)
        self.assertEqual(self.elevator.inner_door_open, 1)
        self.elevator.timestep(3)
        self.assertEqual(self.elevator.inner_door_open, 0)
