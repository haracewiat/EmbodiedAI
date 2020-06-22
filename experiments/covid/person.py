import pygame
import numpy as np
from simulation.agent import Agent
from simulation import helperfunctions
from experiments.covid import parameters as p


class Person(Agent):
<<<<<<< Updated upstream
    pass
=======

    def __init__(self, pos, v, population, image=None):
        super(Person, self).__init__(pos, v, image,
                                     max_speed=p.MAX_SPEED, min_speed=p.MIN_SPEED,
                                     color=config.SUSCEPTIBLE, mass=p.MASS, width=p.WIDTH, height=p.HEIGHT,
                                     dT=p.dT)

        self.swarm = population
        self.time = 0
        self.recovery_time = random.randint(
            p.INFECTION_TIME-p.MARGIN, p.INFECTION_TIME + p.MARGIN)
        self.exposed_time = random.randint(
            p.EXPOSED_TIME-p.MARGIN2, p.EXPOSED_TIME + p.MARGIN2)


    def update_actions(self):

        # Avoid walls
        for wall in self.swarm.objects.walls:
            collide = pygame.sprite.collide_mask(self, wall)
            if bool(collide):
                self.avoid_obstacle()

        # If infected, spread the infection
        self.infect()

        # If infected, recover after a given period
        self.recover()

        # If exposed, get sick after a given period
        self.exposed()

    def infect(self):
        if self.state == State.INFECTIOUS:
            self.swarm.spread_infection(self, p.RADIUS_VIEW)
        if self.state == State.EXPOSED:
            self.swarm.spread_infection(self, p.RADIUS_VIEW)
    def recover(self):
        if self.state == State.INFECTIOUS:
            if self.time >= self.recovery_time:
                self.change_state(State.RECOVERED, self.swarm)
                self.time = 0
            else:
                self.time += 1

    def exposed(self):
         if self.state == State.EXPOSED:
            if self.time >= self.exposed_time:
                self.change_state(State.INFECTIOUS, self.swarm)
                self.time = 0
            else:
                self.time += 1
>>>>>>> Stashed changes
