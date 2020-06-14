"""
Parameter settings for covid experiment
"""

"""
General settings (DO NOT CHANGE)
"""
# screen settings
S_WIDTH, S_HEIGHT = 500, 500
SCREEN = (S_WIDTH, S_HEIGHT)
TRACK_DATA = True

# choose how long to run the simulation
# -1 : infinite, N: finite
FRAMES = -1

# choose swarm type
SWARM = 'Covid'
# define the number of agents
N_AGENTS = 100
# object location
OBJECT_LOC = [S_WIDTH/2., S_HEIGHT/2.]
CONVEX = True
# TIME SETTINGS
# How much the recovery lasts
INFECTION_TIME = 600
# How much the recovery time can differ between people
MARGIN = INFECTION_TIME * 0.3


# Agent Settings:
# agent size
WIDTH = 10
HEIGHT = WIDTH
# update
dT = 0.2
# agents mass
MASS = 20
# agent maximum/minimum speed
MAX_SPEED = 5.
MIN_SPEED = 2.


# Boid Settings:
# velocity force
MAX_FORCE = 8.


"""
Simulation settings to adjust:
"""

"""
Flock class parameters (defines the environment of where the flock to act)
"""
# Define the environment
OBSTACLES = True
OUTSIDE = False

# Number of infected people initially
INITIAL_INFECTED = N_AGENTS * 0.01


"""
Person class parameters
"""
# view of neighbor agents
RADIUS_VIEW = 70
INFECTION_RATE = 0.001
