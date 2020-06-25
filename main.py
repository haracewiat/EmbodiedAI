from simulation.simulation import Simulation
import pygame

# from experiments.flocking import parameters as p
# from experiments.aggregation import parameters as p
from experiments.covid import parameters as p

"""
Code for multi-agent simulation in PyGame with/without physical objects in the environment
"""

if __name__ == "__main__":
    pygame.init()
    sim = Simulation(num_agents=p.N_AGENTS, screen_size=p.SCREEN,
                     swarm_type=p.SWARM, iterations=p.FRAMES)
    sim.run()



