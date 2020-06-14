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

        self.population = population
        self.type = 'S'

    def update_actions(self):

        # self.population.datapoints = ['I'] if random.random() > 0.5 else ['R']

        self.update_state()

    def neighbor_forces(self):

        align_force, cohesion_force, separate_force = np.zeros(
            2), np.zeros(2), np.zeros(2)

        # find all the neighbors of a boid based on its radius view
        neighbors = self.population.find_neighbors(self, p.RADIUS_VIEW)

        # if there are neighbors, estimate the influence of their forces
        if neighbors:
            align_force = self.align(
                self.population.find_neighbor_velocity(neighbors))
            cohesion_force = self.cohesion(
                self.population.find_neighbor_center(neighbors))
            separate_force = self.population.find_neighbor_separation(
                self, neighbors)

        return align_force, cohesion_force, separate_force

    def align(self, neighbor_force):
        """
        Function to align the agent in accordance to neighbor velocity
        :param neighbor_force: np.array(x,y)
        """
        return helperfunctions.normalize(neighbor_force - self.v)

    def cohesion(self, neighbor_center):
        """
        Function to move the agent towards the center of mass of its neighbors
        :param neighbor_rotation: np.array(x,y)
        """
        force = neighbor_center - self.pos
        return helperfunctions.normalize(force - self.v)

    def update_state(self):
        if self.state == State.SUSCEPTIBLE:
            if random.random() < 0.005:
                self.change_state(State.INFECTIOUS, self.population)
        elif self.state == State.INFECTIOUS:
            if random.random() < 0.005:
                self.change_state(State.RECOVERED, self.population)
