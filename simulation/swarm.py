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
        self.data = {State.INFECTIOUS: 0, State.RECOVERED: 0,
                     State.SUSCEPTIBLE: p.N_AGENTS}

    def add_agent(self, agent):
        # Assign the agent to the right partition based on its position
        if p.USE_PARTITIONS:
            agent.partition_key = self.find_partition_key(agent)
            self.partitions[agent.partition_key].add(agent)

        # Store a full list of all agents
        self.agents.add(agent)

    def update(self):
        # update the movement
        for agent in self.agents:
            agent.update_actions()

        # Recalculate the position if necessary
        self.remain_in_screen()

        # execute the update
        for agent in self.agents:
            agent.update()

    def infect_neighbors(self, agent, radius, infection_rate):

        agents = []

        if bool(p.USE_PARTITIONS):

            if agent.state == State.INFECTIOUS:
                # print("AGENT: ", agent.partition_key)

                keys = self.get_adjacent_partition_keys(agent.partition_key)
                agents = pygame.sprite.Group()

                for key in keys:
                    agents.add(self.partitions[key])

                # print("KEYS: ", keys)

                # print("ALL: ")
                # for a in self.agents:
                #     print(a, helperfunctions.dist(
                #         agent.pos, a.pos), a.partition_key)

                # print("NEIGHBOURS: ")
                # for a in agents:
                #     print(a, helperfunctions.dist(
                #         agent.pos, a.pos), a.partition_key)

        else:
            agents = self.agents

        for neighbour in agents:
            if neighbour == agent:
                continue
            else:
                if helperfunctions.dist(agent.pos, neighbour.pos) < radius:
                    if neighbour.state == State.SUSCEPTIBLE and random.random() <= p.INFECTION_RATE:
                        neighbour.change_state(State.INFECTIOUS, self.swarm)

        # Stop sprites to be assigned to a new group every time
        if bool(p.USE_PARTITIONS):
            agents.empty()

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

    def display(self, screen):
        for obstacle in self.objects.obstacles:
            obstacle.display(screen)

        for site in self.objects.sites:
            site.display(screen)

        for agent in self.agents:
            agent.display(screen)

        for agent in self.agents:
            agent.reset_frame()

    '''
    PARTITIONS

    In order to improve the code complexity, the environment can be split into a
    number of partitions (space partitioning). This allows the agents to only 
    investigate the adjacent partitions instead of the whole environment when 
    looking for neighbours. 

    Moreover, the partitions can be used to assign allowed-area(s) to each agent
    and thus restict their mobility.

    '''

    # Creates keys for the partitions
    def create_partitions(self):
        keys = {}

        for i in range(p.NO_PARTITIONS):
            for j in range(p.NO_PARTITIONS):
                keys[tuple([j, i])] = pygame.sprite.Group()

        return keys

    # TODO
    def get_partition_boundaries(self):
        # width = p.S_WIDTH / p.NO_PARTITIONS
        # height = p.S_HEIGHT / p.NO_PARTITIONS

        # partitions = []

        # for i in range(p.NO_PARTITIONS):
        #     for j in range(p.NO_PARTITIONS):
        #         partitions.append(
        #             ({'min_x': width*j, 'max_x': width*j + width, 'min_y': height*i, 'max_y': height*i + height}))
        pass

    # Determines in which partition the agent is currently located
    def find_partition_key(self, agent):
        width_unit = p.S_WIDTH / p.NO_PARTITIONS
        height_unit = p.S_HEIGHT / p.NO_PARTITIONS

        coordinate1 = (int(agent.pos[0]))/width_unit
        coordinate2 = (int(agent.pos[1]))/height_unit

        if coordinate1 >= p.NO_PARTITIONS:
            coordinate1 = p.NO_PARTITIONS - 1

        if coordinate2 >= p.NO_PARTITIONS:
            coordinate2 = p.NO_PARTITIONS - 1

        key = [int(coordinate1), int(coordinate2)]

        return tuple(key)

    # Keeps track of which partition every agent is in
    def update_partition(self, agent):

        new_key = self.find_partition_key(agent)

        if agent.partition_key != new_key:

            # Remove from old partition
            self.partitions[agent.partition_key].remove(agent)

            # Add to the new partition
            self.partitions[new_key].add(agent)

        return new_key

    # Returns the adjacent partitions
    def get_adjacent_partition_keys(self, key):

        current_key = [key[0], key[1]]
        keys = []
        unit = p.NO_PARTITIONS

        for i in range(-1, 2):
            for j in range(-1, 2):

                # Create circular buffer
                # If there are no walls around the environment if p.INSIDE?
                x = current_key[0]+j
                y = current_key[1]+i

                if x < 0:
                    x = unit-1
                elif x >= unit:
                    x = 0
                if y < 0:
                    y = unit-1
                elif y >= unit:
                    y = 0

                keys.append(tuple([x, y]))

        return keys
