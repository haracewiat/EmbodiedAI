from experiments.covid import scenarios as s

"""
GENERAL SETTINGS
"""
# Screen settings
S_WIDTH, S_HEIGHT = 500, 500
SCREEN = (S_WIDTH, S_HEIGHT)

# Partition settings (CAUTION: Make sure a partition has a width no smaller than the person's radius)
NO_PARTITIONS = 5
USE_PARTITIONS = True

# Simulation settings
FRAMES = -1
SWARM = 'Covid'
N_AGENTS = 100
DAY = 200
BUILDINGS, WALLS = s.scenario1()

# Data tracking (store data in a csv file and show live plot)
TRACK_DATA = True
INTERVAL = 100           # Pace at which the plot is refreshed


"""
SIMULATION SETTINGS
"""
# Scenario settings
OBSTACLES = True
OUTSIDE = False
INITIAL_INFECTED = N_AGENTS * 0.01       # Number of infected people initially


"""
AGENT SETTINGS
"""
WIDTH = S_WIDTH * 0.01
HEIGHT = WIDTH
dT = 0.2
MASS = 20
MAX_SPEED = S_WIDTH * 0.004
MIN_SPEED = S_WIDTH * 0.002
MAX_FORCE = 8.

# Infection settings
RADIUS_VIEW = WIDTH*7
INFECTION_TIME = DAY * 2        # How much the recovery lasts
MARGIN = INFECTION_TIME * 0.3   # How much the recovery time can differ among agents
INFECTION_RATE = 0.01


# [???] Scenario settings
OBJECT_LOC = [S_WIDTH/2., S_HEIGHT/2.]
CONVEX = True
