"""
GENERAL SETTINGS
"""
# Screen settings
S_WIDTH, S_HEIGHT = 800, 800
SCREEN = (S_WIDTH, S_HEIGHT)

# Partition settings (CAUTION: Make sure a partition has a width no smaller than the person's radius)
NO_PARTITIONS = 10
USE_PARTITIONS = False

# Simulation settings
FRAMES = -1
SWARM = 'Covid'
N_AGENTS = 50

# Data tracking (store data in a csv file and show live plot)
TRACK_DATA = True

# object location
OBJECT_LOC = [S_WIDTH/2., S_HEIGHT/2.]
CONVEX = True


"""
SIMULATION SETTINGS
"""
# Define the environment
OBSTACLES = True
OUTSIDE = False

# Number of infected people initially
INITIAL_INFECTED = N_AGENTS * 0.1


"""
AGENT SETTINGS
"""
WIDTH = 10
HEIGHT = WIDTH
dT = 0.2
MASS = 20
MAX_SPEED = 2.
MIN_SPEED = 1.
MAX_FORCE = 8.

# Infection settings
RADIUS_VIEW = 70
INFECTION_TIME = 600            # How much the recovery lasts
MARGIN = INFECTION_TIME * 0.3   # How much the recovery time can differ among agents
INFECTION_RATE = 0.01
