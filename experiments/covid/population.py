import numpy as np
import random
import pygame
from simulation.swarm import Swarm
from simulation import helperfunctions
from experiments.covid.person import Person
from experiments.covid import parameters as p
from simulation.agent import State


class Population(Swarm):

    def __init__(self, screen_size):
        super(Population, self).__init__(screen_size)
        self.num_agents = 0
        self.swarm = None

    def initialize(self, num_agents, swarm):
        self.num_agents = num_agents
        self.swarm = swarm

        # Spawn all components
        self.spawn_walls()
        self.spawn_buildings()
        self.spawn_people()

        # Basic reproduction number
        self.basic_reproduction_number = []
        self.previous_infected = 0
        self.current_infected = 0

    def spawn_people(self):
        for agent in range(self.num_agents):

            # Generate starting coordinates
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # Create a new person
            person = Person(pos=np.array(coordinates),
                            v=None, population=self.swarm)

            # Re-estimate the coordinates if walls are present
            self.avoid_walls(person)

            # Infect the initial number of people
            if agent < p.INITIAL_INFECTED:
                person.change_state(State.INFECTIOUS, self.swarm)

            # Add to the population
            self.add_agent(person)

    def remove_person(self, agent):
        agent.kill()

        # Remove the agent from the data
        self.data[agent.state] -= 1

        # For every dead person, spawn a new one
        self.add_person()

    def add_person(self):
        # Generate starting coordinates
        coordinates = helperfunctions.generate_coordinates(self.screen)

        # Create a new person
        person = Person(pos=np.array(coordinates),
                        v=None, population=self.swarm)

        # Re-estimate the coordinates if walls are present
        self.avoid_walls(person)

        # Add to the population
        self.add_agent(person)

        # Add the person to the data
        self.data[person.state] += 1

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
                file=building.img, pos=[random.randrange(100, int(p.S_HEIGHT/2), 100), random.randrange(100, int(p.S_HEIGHT/2), 100)], scale=[100, 100], type='building')

    def spawn_walls(self):
        walls = p.WALLS

        for wall in walls:
            self.objects.add_object(
                file=wall.img, pos=wall.position, scale=wall.scale, type='wall')

    def avoid_walls(self, agent):

        for wall in self.swarm.objects.walls:

            while True:

                collide = pygame.sprite.collide_mask(agent, wall)

                if collide is not None:
                    agent.pos = np.array(
                        helperfunctions.generate_coordinates(self.screen))
                else:
                    break

    def spread_infection(self, agent, radius):
        super().infect_neighbors(agent, radius, p.INFECTION_RATE)

    def get_reproduction_rate(self):

        self.previous_infected = self.current_infected
        self.current_infected = self.data[State.INFECTIOUS]

        y = self.current_infected / self.previous_infected if self.previous_infected > 0 else 0

        if self.data[State.SUSCEPTIBLE] < p.N_AGENTS and self.data[State.INFECTIOUS] == 0:
            pass
        else:
            self.basic_reproduction_number = [y]

        return round(y, 1)
