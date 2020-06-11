import numpy as np
from simulation import helperfunctions
from simulation.swarm import Swarm
from experiments.aggregation.cockroach import Cockroach
from experiments.aggregation import parameters as p


class Aggregations(Swarm):

    def __init__(self, screen_size):
        super(Aggregations, self).__init__(screen_size)
        self.object_loc = p.OUTSIDE

    def initialize(self, num_agents, swarm):

        # Add the border
        object_loc = p.OBJECT_LOC
        filename = 'experiments/flocking/images/redd.png'
        scale = [int(p.S_WIDTH * 0.8), int(p.S_HEIGHT * 0.8)]

        self.objects.add_object(
            file=filename, pos=object_loc, scale=scale, type='obstacle')

        min_x, max_x = helperfunctions.area(object_loc[0], scale[0])
        min_y, max_y = helperfunctions.area(object_loc[1], scale[1])

        # Add site/-s
        sites = p.EXPERIMENT
        for site in sites:
            self.objects.add_object(
                file=site.img, pos=site.area_loc, scale=site.scale, type='site')

        # Add agents
        for agent in range(num_agents):
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # Keep the cocroaches inside of the environment
            while coordinates[0] >= max_x or coordinates[0] <= min_x or coordinates[1] >= max_y or coordinates[1] <= min_y:
                coordinates = helperfunctions.generate_coordinates(
                    self.screen)

            self.add_agent(
                Cockroach(pos=np.array(coordinates), v=None, flock=swarm))

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
