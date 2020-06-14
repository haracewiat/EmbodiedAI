import numpy as np
from simulation.swarm import Swarm
from simulation import helperfunctions
from experiments.covid.person import Person
from experiments.covid import parameters as p


class Population(Swarm):

    def __init__(self, screen_size):
        super(Population, self).__init__(screen_size)
        self.num_agents = 0
        self.swarm = None
        # To do

    def initialize(self, num_agents, swarm):
        self.num_agents = num_agents
        self.swarm = swarm
        # To Do

        # code snipet (not complete) to avoid initializing agents on obstacles
        # given some coordinates and obstacles in the environment, this repositions the agent
        # coordinates = helperfunctions.generate_coordinates(self.screen)

        # if p.OBSTACLES:  # you need to define this variable
        #     for object in self.objects.obstacles:
        #         rel_coordinate = helperfunctions.relative(
        #             coordinates, (object.rect[0], object.rect[1]))
        #         try:
        #             while object.mask.get_at(rel_coordinate):
        #                 coordinates = helperfunctions.generate_coordinates(
        #                     self.screen)
        #                 rel_coordinate = helperfunctions.relative(
        #                     coordinates, (object.rect[0], object.rect[1]))
        #         except IndexError:
        #             pass

        self.spawn_people()

    def spawn_people(self):
        for agent in range(self.num_agents):
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # if obstacles present re-estimate the corrdinates
            # if p.OBSTACLES:
            #     if p.OUTSIDE:
            #         while coordinates[0]<=max_x and coordinates[0]>=min_x and coordinates[1]<=max_y and coordinates[1]>=min_y:
            #             coordinates = helperfunctions.generate_coordinates(self.screen)
            #     else:
            #         while coordinates[0]>=max_x or coordinates[0]<=min_x or coordinates[1]>=max_y or coordinates[1]<=min_y:
            #             coordinates = helperfunctions.generate_coordinates(self.screen)

            self.add_agent(Person(pos=np.array(coordinates),
                                  v=None, population=self.swarm))

    def find_neighbor_velocity(self, neighbors):
        neighbor_sum_v = np.zeros(2)
        for idx in neighbors:
            neighbor_sum_v += list(self.agents)[idx].v
        return neighbor_sum_v/len(neighbors)

    def find_neighbor_center(self, neighbors):
        neighbor_sum_pos = np.zeros(2)
        for idx in neighbors:
            neighbor_sum_pos += list(self.agents)[idx].pos
        return neighbor_sum_pos/len(neighbors)

    def find_neighbor_separation(self, boid, neighbors):  # show what works better
        separate = np.zeros(2)
        for idx in neighbors:
            neighbor_pos = list(self.agents)[idx].pos
            # compute the distance vector (v_x, v_y)
            difference = boid.pos - neighbor_pos
            # normalize to unit vector with respect to its maginiture
            difference /= helperfunctions.norm(difference)
            separate += difference  # add the influences of all neighbors up
        return separate/len(neighbors)
