import pygame
import sys
import matplotlib.pyplot as plt
from experiments.flocking.flock import Flock
from experiments.aggregation.aggregation import Aggregations
from experiments.covid.population import Population

"""
General simulation pipeline, suitable for all experiments 
"""

class Simulation():
    def __init__(self, num_agents, screen_size, swarm_type, iterations):


        #general settings
        self.screensize = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.sim_background = pygame.Color('gray21')
        self.iter = iterations

        #swarm settings
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

        #update
        self.to_update = pygame.sprite.Group()
        self.to_display = pygame.sprite.Group()
        self.running = True

    def CovidPlot(self, data):
        output_name = "experiments/covid/plots/Covid-19-SIR%s.png" % time.strftime("-%m.%d.%y-%H:%M", time.localtime())
        fig = plt.figure()
        plt.plot(data['S'], label="Susceptible", color=(1,0.5,0)) #Orange
        plt.plot(data['I'], label="Infected", color=(1,0,0)) #Red
        plt.plot(data['R'], label="Recovered", color=(0, 1, 0)) #Green
        plt.title("Covid-19 Simulation S-I-R")
        plt.xlabel("Time")
        plt.ylabel("Population")
        plt.legend()
        fig.savefig(output_name)
        plt.show()

    def FlockPlot(self):
        pass

    def AggregationPlot(self):
        pass

    def plot_simulation(self):
        if self.swarm_type == 'Covid':
            self.CovidPlot(self.swarm.points_to_plot)

        elif self.swarm_type == 'Flock':
            self.FlockPlot()

        elif self.swarm_type == 'Aggregation':
            self.AggregationPlot()



    def display(self):
        for sprite in self.to_display:
            sprite.display(self.screen)

    def update(self):
        self.to_update.update()


    def initialize(self):

        #initialize a swarm type specific environment
        self.swarm.initialize(self.num_agents, self.swarm)

        #add all agents/objects to the update
        self.to_update = pygame.sprite.Group(self.swarm)

        #add all agents/objects to display
        self.to_display = pygame.sprite.Group(
            self.to_update
        )

    def simulate(self):
        self.screen.fill(self.sim_background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.update()
        self.display()
        pygame.display.flip()



    def run(self):
        #initialize the environment and agent/obstacle positions
        self.initialize()
        #the simulation loop, infinite until the user exists the simulation
        #finite time parameter or infinite
        if self.iter == -1:
            while self.running:
                self.simulate()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # The event is pushing the x button, not ctrl-c.
                        self.running = False
                        self.plot_simulation()
        else:
            for i in range(self.iter):
                self.simulate()
            self.plot_simulation()



