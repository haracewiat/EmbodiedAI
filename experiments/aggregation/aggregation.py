import numpy as np
from simulation import helperfunctions
from simulation.swarm import Swarm
from experiments.aggregation.cockroach import Cockroach
from experiments.aggregation import parameters as p


class Aggregations(Swarm):

    def __init__(self, screen_size):
        super(Aggregations, self).__init__(screen_size)
        self.object_loc = p.OUTSIDE

        # Cockroaches data
        self.mask1 = None
        self.site1 = 0
        self.site2 = 0
        self.free = p.N_AGENTS

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
        for index, site in enumerate(sites):
            if index == 0:
                self.mask1 = site

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
