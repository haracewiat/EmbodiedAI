import numpy as np
from simulation.swarm import Swarm
from simulation import helperfunctions
from experiments.covid.person import Person
from experiments.covid import parameters as p

class Population(Swarm):

<<<<<<< Updated upstream
    def __init__(self):
        pass
        #To do
=======
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

    def spawn_people(self):
        for agent in range(self.num_agents):
            Rvalue = 0
            # Generate starting coordinates
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # Create a new person
            person = Person(pos=np.array(coordinates),
                            v=None, population=self.swarm)

            # Re-estimate the coordinates if walls are present
            self.avoid_walls(person)

            # Infect the initial number of people
            if agent < p.INITIAL_INFECTED:
                person.change_state(State.EXPOSED, self.swarm)
                

            # Add to the populationS
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
                file=building.img, pos=[random.randrange(100, int(p.S_HEIGHT/2), 100), random.randrange(100, int(p.S_HEIGHT/2), 100)], scale=[100, 100], type='building')

    def spawn_walls(self):
        walls = p.WALLS

        for wall in walls:
            self.objects.add_object(
                file=wall.img, pos=wall.position, scale=wall.scale, type='wall')

    def avoid_walls(self, agent):

        for wall in self.swarm.objects.walls:
>>>>>>> Stashed changes

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
