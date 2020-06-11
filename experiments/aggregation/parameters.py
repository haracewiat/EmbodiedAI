from experiments.aggregation import experiments as e


"""
GLOBAL SETTING (DO NOT CHANGE)
"""
# screen settings
S_WIDTH, S_HEIGHT = 800, 800
SCREEN = (S_WIDTH, S_HEIGHT)

# choose how long to run the simulation
# -1 : infinite, N: finite
FRAMES = -1

# choose swarm type
SWARM = 'Aggregation'
# define the number of agents
N_AGENTS = 40
# object location
OBJECT_LOC = [S_WIDTH/2., S_HEIGHT/2.]
CONVEX = False

# Agent Settings:
# agent size
# WIDTH = int(S_WIDTH*0.01)
# HEIGHT = int(S_HEIGHT*0.008)
WIDTH = 10
HEIGHT = 8
# update
dT = 0.2
# agents mass
MASS = 20
# agent maximum/minimum speed
MAX_SPEED = 17.
MIN_SPEED = 14.


# Cocroach Settings:
# velocity force
MAX_FORCE = 8.


"""
SETTING TO ADJUST:
"""

"""
AGGREGARTION (environment)
"""
OBSTACLES = True
OUTSIDE = False

# choose experiment
EXPERIMENT = e.experiment1(SCREEN)


"""
COCROACH
"""

# view of neighbor agents
# RADIUS_VIEW = int(S_HEIGHT*S_WIDTH*0.000001*70) Make it with respect to the screen size
RADIUS_VIEW = 70

# probability of leaving/not joining the site (a value between 0 and 1)
WANDERING_FORCE = 0.1

# Number of ticks to elapse before changing the state
T_JOIN = 1
T_LEAVE = 4
