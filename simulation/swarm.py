import pygame
from simulation import helperfunctions
from simulation.objects import Objects
from simulation.agent import State
from experiments.covid import parameters as p
import random

"""
General swarm class that defines general swarm properties, which are common across different swarm types
"""

# superclass


class Swarm(pygame.sprite.Sprite):

    def __init__(self, screen_size, plot=None):
        super(Swarm, self).__init__()

        self.partitions = self.create_partitions()
        self.agents = pygame.sprite.Group()
        self.screen = screen_size
        self.objects = Objects()
        self.points_to_plot = {'S': [], 'I': [], 'R': []}
        self.datapoints = []
        self.data = {State.INFECTIOUS: 0, State.RECOVERED: 0,
                     State.SUSCEPTIBLE: p.N_AGENTS}

    def add_agent(self, agent):
        # Assign the agent to the right partition based on its position
        agent.partition_key = self.find_partition_key(agent)
        self.partitions[agent.partition_key].add(agent)

        self.agents.add(agent)

    def update(self):
        # update the movement
        for agent in self.agents:
            agent.update_actions()

        self.remain_in_screen()

        # execute the update
        for agent in self.agents:
            agent.update()

        # print(self.partitions)

    def infect_neighbors(self, agent, radius, infection_rate):

        keys = self.get_adjacent_partition_keys(agent)
        agents = self.agents

        for key in keys:
            # agents.add(self.partitions[key])
            pass

        for neighbour in agents:
            if neighbour == agent:
                continue
            else:
                if helperfunctions.dist(agent.pos, neighbour.pos) < radius:
                    if neighbour.state == State.SUSCEPTIBLE and random.random() <= p.INFECTION_RATE:
                        neighbour.change_state(State.INFECTIOUS, self.swarm)

    def remain_in_screen(self):
        for agent in self.agents:
            if agent.pos[0] > self.screen[0]:
                agent.pos[0] = 0.
            if agent.pos[0] < 0:
                agent.pos[0] = float(self.screen[0])
            if agent.pos[1] < 0:
                agent.pos[1] = float(self.screen[1])
            if agent.pos[1] > self.screen[1]:
                agent.pos[1] = 0.

        self.update_partition(agent)

    def display(self, screen):
        for obstacle in self.objects.obstacles:
            obstacle.display(screen)

        for site in self.objects.sites:
            site.display(screen)

        for agent in self.agents:
            agent.display(screen)

        for agent in self.agents:
            agent.reset_frame()

    def create_partitions(self):
        width = p.S_WIDTH / p.NO_PARTITIONS
        height = p.S_HEIGHT / p.NO_PARTITIONS

        keys = {}

        for i in range(p.NO_PARTITIONS):
            for j in range(p.NO_PARTITIONS):
                keys[tuple([j, i])] = pygame.sprite.Group()

        return keys

    def get_partition_boundaries(self):
        # width = p.S_WIDTH / p.NO_PARTITIONS
        # height = p.S_HEIGHT / p.NO_PARTITIONS

        # partitions = []

        # for i in range(p.NO_PARTITIONS):
        #     for j in range(p.NO_PARTITIONS):
        #         partitions.append(
        #             ({'min_x': width*j, 'max_x': width*j + width, 'min_y': height*i, 'max_y': height*i + height}))
        pass

    def find_partition_key(self, agent):
        width_unit = p.S_WIDTH / p.NO_PARTITIONS
        height_unit = p.S_HEIGHT / p.NO_PARTITIONS

        coordinate1 = int((agent.pos[0]-0000.1)/width_unit)
        coordinate2 = int((agent.pos[1]-0000.1)/height_unit)

        key = [coordinate1, coordinate2]

        return tuple(key)

    def update_partition(self, agent):
        new_key = self.find_partition_key(agent)

        if agent.partition_key != new_key:
            self.partitions[agent.partition_key].remove(agent)
            self.partitions[new_key].add(agent)
            agent.partition_key = new_key

    def get_adjacent_partition_keys(self, agent):

        current_key = [agent.partition_key[0], agent.partition_key[1]]
        keys = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= current_key[0]+j < p.NO_PARTITIONS and 0 <= current_key[1]+i < p.NO_PARTITIONS:
                    keys.append(tuple([current_key[0]+j, current_key[1]+i]))

        return keys
