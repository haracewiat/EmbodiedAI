import pygame
import numpy as np
from simulation import config
from simulation.agent import Agent
from simulation.agent import State
from simulation import helperfunctions
from experiments.covid import parameters as p
from simulation.swarm import Swarm


import random


class Person(Agent):

    def __init__(self, pos, v, population, image=None):
        super(Person, self).__init__(pos, v, image,
                                     max_speed=p.MAX_SPEED, min_speed=p.MIN_SPEED,
                                     color=config.SUSCEPTIBLE, mass=p.MASS, width=p.WIDTH, height=p.HEIGHT,
                                     dT=p.dT)
        
        self.swarm = population
        self.time = 0
        self.agent_lifespan = 0
        self.reproduction_rate = 0
        self.recovery_time = random.randint(
            p.INFECTION_TIME-p.MARGIN, p.INFECTION_TIME + p.MARGIN)
        self.exposed_time = random.randint( p.EXPOSED_TIME, p.EXPOSED_TIME23)
        self.dying_chance = random.randint(
            p.LIFESPAN-p.MARGIN_DYING, p.LIFESPAN + p.MARGIN_DYING
            )

    def update_actions(self):

        # Avoid walls
        for wall in self.swarm.objects.walls:
            collide = pygame.sprite.collide_mask(self, wall)
            if bool(collide):
                self.avoid_obstacle()

        # Keep distance from others
        if p.SOCIAL_DISTANCING:
            self.swarm.avoid_neighbours(self)

        # If infected, spread the infection
        self.infect()

        # If infected, recover after a given period
        self.recover()

        self.exposed()
        self.dying()
        self.dead()
        
        
        
        
        
    def infect(self):
        if self.state == State.INFECTIOUS:
            self.swarm.spread_infection(self, p.RADIUS_VIEW)

    def recover(self):
        if self.state == State.INFECTIOUS:
            if self.time >= self.recovery_time:
                self.change_state(State.RECOVERED, self.swarm)
                self.time = 0
            else:
                self.time += 1

    def exposed(self):
        if self.state == State.EXPOSED: 
            if self.time >= self.exposed_time:
                self.change_state(State.INFECTIOUS, self.swarm)
                self.time = 0
            else:
                self.time += 1

    def dying(self):
         if self.state == State.INFECTIOUS: 
            if self.agent_lifespan >= self.dying_chance:
                self.change_state(State.DEAD, self.swarm)
                self.agent_lifespan = 0
            
            else:
                self.agent_lifespan += 1.4

                
    def dead(self):
        
        if self.state == State.DEAD: 
            self.v = 0 #if death stand still
            self.kill()
          
            pygame.sprite.Sprite.add(self.swarm)

    def kill(self):
        pygame.sprite.Sprite.kill(self)
        self.birth()
        
            

    def birth(self):
    
        coordinates = helperfunctions.generate_coordinates(p.SCREEN)

                # Create a new person
        person = Person(pos=np.array(coordinates),
                            v=None, population=self.swarm)

                # Re-estimate the coordinates if walls are present
        

            # Add to the population
        self.add_agent(person)
                


   