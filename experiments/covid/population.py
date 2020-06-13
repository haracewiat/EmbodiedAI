import numpy as np
from simulation.swarm import Swarm
from simulation import helperfunctions
from experiments.covid.person import Person
from experiments.covid import parameters as p

class Population(Swarm):

    def __init__(self):
        pass
        #To do

    def initialize(self):

        #To Do

        #code snipet (not complete) to avoid initializing agents on obstacles
        #given some coordinates and obstacles in the environment, this repositions the agent
        coordinates = helperfunctions.generate_coordinates(self.screen)

        if p.OBSTACLES: #you need to define this variable
            for object in self.objects.obstacles:
                rel_coordinate = helperfunctions.relative(coordinates, (object.rect[0], object.rect[1]))
                try:
                    while object.mask.get_at(rel_coordinate):
                        coordinates = helperfunctions.generate_coordinates(self.screen)
                        rel_coordinate = helperfunctions.relative(coordinates, (object.rect[0], object.rect[1]))
                except IndexError:
                    pass
