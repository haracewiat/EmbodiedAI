import pygame
import numpy as np
from simulation import config
from simulation.agent import Agent
from simulation.agent import State
from simulation import helperfunctions
from experiments.covid import parameters as p
import random


class Person(Agent):

    def __init__(self, pos, v, population, image=None):
        super(Person, self).__init__(pos, v, image,
                                     max_speed=p.MAX_SPEED, min_speed=p.MIN_SPEED,
                                     color=config.SUSCEPTIBLE, mass=p.MASS, width=p.WIDTH, height=p.HEIGHT,
                                     dT=p.dT)

        self.swarm = population
        self.time = 0
        self.type = 'S'

        # Initialize the new person to infectious with 10% of chance
        if random.random() <= 0.1:
            self.change_state(State.INFECTIOUS, self.swarm)

    def update_actions(self):

        # If infected, spread the infection
        self.infect()

        # If infected, recover after a given period
        self.recover()

    def infect(self):
        if self.state == State.INFECTIOUS:
            self.swarm.spread_infection(self, p.RADIUS_VIEW)

    def recover(self):
        if self.state == State.INFECTIOUS:
            if self.time >= p.DAY:
                self.change_state(State.RECOVERED, self.swarm)
                self.time = 0
            else:
                self.time += 1
