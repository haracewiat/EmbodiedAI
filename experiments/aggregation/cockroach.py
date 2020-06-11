import pygame
from enum import Enum
import numpy as np
from simulation import helperfunctions
from simulation.agent import Agent
from experiments.aggregation import parameters as p


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
        self.last_v = self.v

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

        print("My speed: ", self.v)

    # Enables the modification of the cockroach state

    def change_state(self):

        print(self.state)

        if self.state == State.WANDERING:
            pass

        elif self.state == State.JOINING:

            if bool(self.wait(20)):
                self.state = State.STILL

        elif self.state == State.STILL:
            self.v = [0, 0]

        elif self.state == State.LEAVING:
            self.v = self.last_v
            if self.site and not pygame.sprite.collide_mask(self, self.site):
                self.site = None
                self.state = State.WANDERING
            # if self.site and not pygame.sprite.collide_mask(self, self.site):
            #     print("I don't collide anymore!")
            #     self.site = None
            #     self.state = State.WANDERING

        else:
            print('Invalid state: ', state)

    # Defines when the agent joins and leaves an aggregate
    def site_behavior(self):

        if self.site is None:
            return

        probability = helperfunctions.randrange(0, 100)

        # if just ENTERED, then can stay in WANDERING or change into JOINING
        if self.state == State.WANDERING:
            self.last_v = self.v
            if probability >= p.WANDERING_FORCE:
                self.state = State.JOINING

        # if already STILL, then can stay in STILL or change into LEAVING
        elif self.state == State.STILL:
            print("I'm still ---------------------------")
            if probability < p.WANDERING_FORCE:
                self.state = State.LEAVING

    def wandering(self):
        pass

    def wait(self, ticks):
        if self.ticks == ticks:
            self.ticks = 0
            return True

        self.ticks = self.ticks + 1
        return False


class State(Enum):
    WANDERING = 0
    JOINING = 1
    STILL = 2
    LEAVING = 3
