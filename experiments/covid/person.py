import pygame
import numpy as np
from simulation import config
from simulation.agent import Agent
from simulation.agent import State
from simulation import helperfunctions
from experiments.covid import parameters as p
from simulation.swarm import Swarm
from scipy.stats import skewnorm


import random


class Person(Agent):

    def __init__(self, pos, v, population, image=None):
        super(Person, self).__init__(pos, v, image,
                                     max_speed=p.MAX_SPEED, min_speed=p.MIN_SPEED,
                                     color=config.SUSCEPTIBLE, mass=p.MASS, width=p.WIDTH, height=p.HEIGHT,
                                     dT=p.dT)

        self.swarm = population
        self.reproduction_rate = 0
        self.ticks = 0
        self.ALIVE = True
        self.infection_time = self.get_infection_time()

        # Set up SEIR model
        if p.SEIR:
            self.exposed_time = self.get_exposed_time()

        # Set up vital dynamics
        if p.VITAL_DYNAMICS:
            self.lifespan = self.get_lifespan()
            self.age = 0

    def update_actions(self):

        if self.ALIVE:

            # Avoid walls
            for wall in self.swarm.objects.walls:
                collide = pygame.sprite.collide_mask(self, wall)
                if bool(collide):
                    self.avoid_obstacle()

            # Keep distance from others
            if p.SOCIAL_DISTANCING:
                self.swarm.avoid_neighbours(self)

            # If infected, spread the infection
            self.infect()

            # If infected, recover after a given period
            self.recover()

            # Randomly change direction
            self.change_direction()

            # If exposed, become infectious
            if p.SEIR:
                self.become_infectious()

            # # See if it's time to die
            if p.VITAL_DYNAMICS:
                self.check_lifespan()
                self.age += 1

    def infect(self):
        if self.state == State.INFECTIOUS:
            self.swarm.spread_infection(self, self.radius)

    def recover(self):
        if self.state == State.INFECTIOUS:
            if self.ticks >= self.infection_time:
                self.change_state(State.RECOVERED, self.swarm)
                self.ticks = 0
            else:
                self.ticks += 1

    def become_infectious(self):
        if self.state == State.EXPOSED:
            if self.ticks >= self.exposed_time:

                # Change either into infectious or recovered
                if random.random() >= p.NEVER_INFECTIOUS:

                    self.change_state(State.INFECTIOUS, self.swarm)

                    # If changed into infectious, shorten the lifespan
                    if p.VITAL_DYNAMICS:
                        self.reduce_lifespan()

                else:
                    self.change_state(State.RECOVERED, self.swarm)

                self.ticks = 0
            else:
                self.ticks += 1

    def check_lifespan(self):
        if self.age >= self.lifespan:
            self.swarm.remove_person(self)
            self.ALIVE = False

    def change_direction(self):
        if random.random() <= 0.001:
            self.v = self.set_velocity()

    def get_lifespan(self):
        return random.randint(p.LIFESPAN-p.MARGIN_LIFESPAN, p.LIFESPAN + p.MARGIN_LIFESPAN)

    def get_infection_time(self):
        return random.randint(p.INFECTION_TIME-p.MARGIN_INFECTION, p.INFECTION_TIME + p.MARGIN_INFECTION)

    def get_exposed_time(self):

        numValues = 100
        maxValue = p.EXPOSED_TIME+p.MARGIN_EXPOSED
        skewness = 5

        # Create a skewed distribution
        r = skewnorm.rvs(a=skewness, loc=maxValue,
                         size=numValues)

        # Shift the set so the minimum value is equal the bottom margin
        r = r - (p.EXPOSED_TIME-p.MARGIN_EXPOSED)
        # Standadize all the vlues
        r = r / max(r)
        # Multiply the standardized values by the maximum value.
        r = r * maxValue

        # Plot histogram to check skewness
        # import matplotlib.pyplot as plt
        # plt.hist(r, 30, density=True, color=config.COLORS['N_INFECTIOUS'])
        # plt.show()

        return random.choice(r)

        #(p.EXPOSED_TIME-p.MARGIN_EXPOSED, p.EXPOSED_TIME+p.MARGIN_EXPOSED)

    def reduce_lifespan(self):
        self.lifespan = random.randint(int(self.lifespan * 0.7), self.lifespan)
