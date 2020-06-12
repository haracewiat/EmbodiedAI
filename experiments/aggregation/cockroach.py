import pygame
import math
from enum import Enum
import numpy as np
from simulation import helperfunctions
from simulation.agent import Agent
from experiments.aggregation import parameters as p
import random


class Cockroach(Agent):

    def __init__(self, pos, v, flock, image='experiments/aggregation/images/cockroach.png'):
        super(Cockroach, self).__init__(pos, v, image,
                                        max_speed=p.MAX_SPEED, min_speed=p.MIN_SPEED,
                                        mass=p.MASS, width=p.WIDTH, height=p.HEIGHT,
                                        dT=p.dT)

        self.flock = flock
        self.site = None
        self.state = State.WANDERING
        self.ticks = 0
        self.last_v = v
        self.T_DIRECTION = random.randint(50, 150)

    # Describes how the agents interact with the aggregation sites and the constricted area
    def update_actions(self):

        # avoid any obstacles in the environment
        for obstacle in self.flock.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle(obstacle.pos, self.flock.object_loc)

        # Sense the entered sites
        for site in self.flock.objects.sites:
            entered = pygame.sprite.collide_mask(self, site)
            if bool(entered):
                self.site = site

        # Decide whether to join or leave a site if joined any
        self.site_behavior()

        # Ack depending on the current state
        self.change_state()

    # Enables the modification of the cockroach state

    def change_state(self):

        if self.state == State.WANDERING:

            # Comment this out if you want the cockroaches to maintain direction
            if bool(self.wait(self.T_DIRECTION)):
                self.v = self.set_velocity()

        elif self.state == State.JOINING:
            collide = pygame.sprite.collide_mask(self, self.site)
            if bool(self.wait(p.T_JOIN)) or not bool(collide):
                self.add_statistic(1)
                self.state = State.STILL

        elif self.state == State.STILL:
            self.v = [0, 0]

            if bool(self.wait(p.D)):
                if random.random() <= self.get_leave_probability():
                    self.state = State.LEAVING

        elif self.state == State.LEAVING:
            self.v = self.last_v

            if bool(self.wait(p.T_LEAVE)):
                self.add_statistic(-1)
                self.site = None
                self.T_DIRECTION = random.randint(50, 150)
                self.state = State.WANDERING

        else:
            print('Invalid state: ', state)

    # Defines when the agent joins and leaves an aggregate
    def site_behavior(self):

        if self.site is None:
            return

        # if just ENTERED, then can stay in WANDERING or change into JOINING
        if self.state == State.WANDERING:
            self.last_v = self.v
            if random.random() <= self.get_join_probability():
                self.ticks = 0
                self.state = State.JOINING

    def wait(self, ticks):
        if self.ticks == ticks:
            self.ticks = 0
            return True

        self.ticks = self.ticks + 1
        return False

    def get_join_probability(self):
        neighbours_count = len(self.flock.find_neighbors(self, p.RADIUS_VIEW))
        return 1 / (1 + math.exp(-neighbours_count * p.P_JOIN))

    def get_leave_probability(self):
        neighbours_count = len(self.flock.find_neighbors(self, p.RADIUS_VIEW))
        return 1 / (1 + math.exp(neighbours_count * p.P_LEAVE))

    def add_statistic(self, number):
        if self.site is None:
            return

        if self.site.pos[0] == self.flock.mask1.area_loc[0]:
            self.flock.site1 = self.flock.site1 + number
        else:
            self.flock.site2 = self.flock.site2 + number

        self.flock.free - number


class State(Enum):
    WANDERING = 0
    JOINING = 1
    STILL = 2
    LEAVING = 3
