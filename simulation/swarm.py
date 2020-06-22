import pygame
from simulation import helperfunctions
from simulation.objects import Objects

"""
General swarm class that defines general swarm properties, which are common across different swarm types
"""

#superclass
class Swarm(pygame.sprite.Sprite):

    def __init__(self,screen_size, plot=None):
        super(Swarm,self).__init__()
        self.agents = pygame.sprite.Group()
        self.screen = screen_size
        self.objects = Objects()
        self.points_to_plot=plot
        self.datapoints = []

<<<<<<< Updated upstream
=======
        # Virus spread data
        self.data = {State.INFECTIOUS: 0, State.RECOVERED: 0, State.EXPOSED : 0,
                     State.SUSCEPTIBLE: p.N_AGENTS}
>>>>>>> Stashed changes

    def add_agent(self,agent):
        self.agents.add(agent)

    def find_neighbors(self, agent, radius):
        agents = list(self.agents).copy()
        neighbors = []
        for j, neighbor in enumerate(agents):
            if agent == neighbor:
                continue
            else:
                try:
                    type = neighbor.type
                except:
                    type = None

            if type != None:
                if type =='I' and helperfunctions.dist(agent.pos, neighbor.pos) < radius:
                    neighbors.append(j)
            elif helperfunctions.dist(agent.pos, neighbor.pos) < radius:
                neighbors.append(j)

        return neighbors

    def remain_in_screen(self):
        for agent in self.agents:
            if agent.pos[0] > self.screen[0]:
                agent.pos[0]=0.
            if agent.pos[0] < 0:
                agent.pos[0] = float(self.screen[0])
            if agent.pos[1] < 0:
                agent.pos[1] = float(self.screen[1])
            if agent.pos[1] > self.screen[1]:
                agent.pos[1]=0.

    # plotting the number of infected and recovered
    def add_point(self, lst):
        #Count current numbers
        values = {'S':0, 'I':0, 'R':0}
        for state in lst:
            values[state] += 1

        for x in values:
            self.points_to_plot[x].append(values[x])


    def update(self):
        #update the movement
        self.datapoints = []
        for agent in self.agents:
<<<<<<< Updated upstream
            agent.update_actions()
=======
            agent.reset_frame()

    def try_to_infect(self, agent, neighbour, radius):

        if neighbour.state != State.SUSCEPTIBLE:
            return

        distance = helperfunctions.dist(agent.pos, neighbour.pos)

        if distance < radius:
            if random.random() <= p.INFECTION_RATE:
                neighbour.change_state(State.EXPOSED, self.swarm)
          
    '''
    PARTITIONS

    In order to reduce the code complexity, the environment can be split into a
    number of partitions (see: space partitioning). This allows the agents to only 
    investigate the adjacent partitions instead of the whole environment when 
    looking for neighbours. 

    Moreover, the partitions can be used to assign "allowed-area(s)" (home, nearest
    shop) to each agent and thus restict their mobility.

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
>>>>>>> Stashed changes

        if len(self.datapoints):
            self.add_point(self.datapoints)
        self.remain_in_screen()

        #execute the update
        for agent in self.agents:
            agent.update()


    def display(self, screen):
        for obstacle in self.objects.obstacles:
            obstacle.display(screen)

        for site in self.objects.sites:
            site.display(screen)

        for agent in self.agents:
            agent.display(screen)

        for agent in self.agents:
            agent.reset_frame()
