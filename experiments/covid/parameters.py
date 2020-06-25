from experiments.covid import scenarios as s

"""
GENERAL SETTINGS
"""
# Screen settings
S_WIDTH, S_HEIGHT = 1000, 1000
SCREEN = (S_WIDTH, S_HEIGHT)

# Partition settings (CAUTION: Make sure a partition has a width no smaller than the person's radius)
NO_PARTITIONS = 10
USE_PARTITIONS = True

# Simulation settings
FRAMES = -1
SWARM = 'Covid'
N_AGENTS = 100
DAY = 200
BUILDINGS, WALLS = s.scenario0()
SEIR = False
VITAL_DYNAMICS = True

# Policies
SOCIAL_DISTANCING = False

# Data tracking (store data in a csv file and show live plot)
TRACK_DATA = True
DELAY = 5                  # Seconds to dealy the start of the simulation
INTERVAL = 50              # Pace at which the plot is refreshed


"""
SIMULATION SETTINGS
"""
# Scenario settings
INITIAL_INFECTED = N_AGENTS * 0.01       # Number of infected people initially


"""
AGENT SETTINGS
"""
WIDTH = S_WIDTH * 0.01
HEIGHT = WIDTH
dT = 0.2
MASS = 20
MAX_SPEED = int(S_WIDTH * 0.006)
MIN_SPEED = int(S_WIDTH * 0.005)
MAX_FORCE = 8.
RADIUS_VIEW = WIDTH*7

# Infection settings
INFECTION_TIME = DAY * 2.5               # How much the recovery lasts
MARGIN_INFECTION = INFECTION_TIME * 0.3  # Margin of recovery time
INFECTION_RATE = 0.01                    # Chance of infecting others
NEVER_INFECTIOUS = 0.1                   # Chance of never becoming infectious

# Exposed state settings
EXPOSED_TIME = DAY * 2.5                 # How much the exposed phase lasts
MARGIN_EXPOSED = EXPOSED_TIME * 0.2      # Margin of exposed time

# Lifespan settings
LIFESPAN = DAY * 9                       # How much the lifespan is
MARGIN_LIFESPAN = LIFESPAN * 0.3         # Margin of lifespan
