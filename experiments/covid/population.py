import numpy as np
from simulation.swarm import Swarm
from simulation import helperfunctions
from experiments.covid.person import Person
from experiments.covid import parameters as p
import random
from simulation.agent import State


class Population(Swarm):

    def __init__(self, screen_size):
        super(Population, self).__init__(screen_size)
        self.num_agents = 0
        self.swarm = None

    def initialize(self, num_agents, swarm):
        self.num_agents = num_agents
        self.swarm = swarm
        self.spawn_buildings()
        self.spawn_people()

    def spawn_people(self):
        for agent in range(self.num_agents):

            # Generate starting coordinates
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # Re-estimate the coordinates if obstacles are present
            # self.avoid_obstacles(coordinates) [NOT IMPLEMENTED]

            # Create a new person
            person = Person(pos=np.array(coordinates),
                            v=None, population=self.swarm)

            # Infect the initial number of people
            if agent < p.INITIAL_INFECTED:
                person.change_state(State.INFECTIOUS, self.swarm)

            # Add to the population
            self.add_agent(person)

    def spawn_buildings(self):
        buildings = p.BUILDINGS

        '''
            DUMMY FUNCTION
            > Add method to randomly select the position (based on free partition)
            > Add method to determine behaviour based on the building type
            > Add transparency if someone is inside (?)
            > Assign each person to a house (?)

            This function demonstrates the ability to spawn the buildings of different types.
        '''
        for building in buildings:
            self.objects.add_object(
                file=building.img, pos=[random.randrange(100, 1000, 50), random.randrange(100, 1000, 50)], scale=[100, 100], type='site')

    def avoid_obstacles(self, coordinates):
        pass

    def spread_infection(self, agent, radius):
        super().infect_neighbors(agent, radius, p.INFECTION_RATE)
