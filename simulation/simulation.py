import threading
import pandas as pd
import numpy as np
from simulation import config
import time
from simulation.plot import LivePlot
from simulation.plot import Data
from simulation.agent import State
from experiments.covid.population import Population
from experiments.aggregation.aggregation import Aggregations
from experiments.covid import parameters as p
from experiments.flocking.flock import Flock
import matplotlib.pyplot as plt
import pygame
import sys

"""
General simulation pipeline, suitable for all experiments
"""


class Simulation():
    def __init__(self, num_agents, screen_size, swarm_type, iterations):
        # general settings
        self.screensize = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.sim_background = pygame.Color('gray21')
        self.iter = iterations
        self.swarm_type = swarm_type

        # swarm settings
        self.num_agents = num_agents
        if swarm_type == 'Flock':
            self.swarm = Flock(screen_size)
        elif swarm_type == 'Aggregation':
            self.swarm = Aggregations(screen_size)
            pass
        elif swarm_type == 'Covid':
            self.swarm = Population(screen_size)
        else:
            print('None of the possible swarms selected')
            sys.exit()

        if bool(p.TRACK_DATA):
            # Create data storage
            self.data = self.swarm.data
            self.data_storage = Data(self.data)
            self.data_storage.initialize()

            # Spawn the live plot
            self.plot = threading.Thread(target=LivePlot)
            self.plot.setDaemon(True)
            self.plot.start()

        # update
        self.to_update = pygame.sprite.Group()
        self.to_display = pygame.sprite.Group()
        self.running = True

    def display(self):
        for sprite in self.to_display:
            sprite.display(self.screen)

    def update(self):
        self.to_update.update()

    def initialize(self):

        # initialize a swarm type specific environment
        self.swarm.initialize(self.num_agents, self.swarm)

        # add all agents/objects to the update queue
        self.to_update = pygame.sprite.Group(self.swarm)

        # add all agents/objects to display queue
        self.to_display = pygame.sprite.Group(
            self.to_update
        )

    def simulate(self):

        # Store data on every iteration
        if bool(p.TRACK_DATA):
            self.data_storage.add_entry(self.swarm.data)

        self.screen.fill(self.sim_background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # config.terminate_threads = True
                # self.plot.join()
                self.running = False

        self.update()
        self.display()
        pygame.display.flip()

    def run(self):
        # initialize the environment and agent/obstacle positions
        self.initialize()

        # Run the simulation for a number of iterations (infinite if -1)
        if self.iter == -1:
            while self.running:
                self.simulate()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # config.terminate_threads = True
                        # self.plot.join()
                        self.running = False
        else:
            for i in range(self.iter):
                self.simulate()
