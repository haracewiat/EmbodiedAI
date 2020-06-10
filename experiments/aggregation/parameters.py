"""
Parameter settings to be loaded in the model
"""


class obstacle:
    def __init__(self, area_loc, scale, big):
        self.img = 'experiments/aggregation/images/greyc1.png' if not big else 'experiments/aggregation/images/greyc2.png'
        self.area_loc = area_loc
        self.scale = scale if not big else tuple(
            int(dimension*1.2) for dimension in scale)


def experiment0(screensize):  # Single aggregation site
    obstacles = []
    obstacles.append(
        obstacle([screensize[0] / 2., screensize[1] / 2.],
                 [int(S_WIDTH*0.11), int(S_HEIGHT*0.11)], False)
    )

    return obstacles


def experiment1(screensize):  # Two aggregation site (different sizes)
    obstacles = []
    obstacles.append(
        obstacle([screensize[0] / 3.5, screensize[1] / 2.],
                 [int(S_WIDTH*0.11), int(S_HEIGHT*0.11)], False),
    )
    obstacles.append(
        obstacle([(screensize[0] / 3.5) * 2.5, screensize[1] / 2.],
                 [int(S_WIDTH*0.11), int(S_HEIGHT*0.11)], False),
    )

    return obstacles


def experiment2(screensize):  # Two aggregation site (different sizes)
    obstacles = []
    obstacles.append(
        obstacle([screensize[0] / 3.5, screensize[1] / 2.],
                 [int(S_WIDTH*0.11), int(S_HEIGHT*0.11)], False),
    )
    obstacles.append(
        obstacle([(screensize[0] / 3.5) * 2.5, screensize[1] / 2.],
                 [int(S_WIDTH*0.11), int(S_HEIGHT*0.11)], True),
    )

    return obstacles


"""
General settings (DO NOT CHANGE)
"""
# screen settings
S_WIDTH, S_HEIGHT = 1000, 1000
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
# choose experiment
EXPERIMENT = experiment1(SCREEN)

# Agent Settings:
# agent size
WIDTH = 10
HEIGHT = 8
# update
dT = 0.2
# agents mass
MASS = 20
# agent maximum/minimum speed
MAX_SPEED = 7.
MIN_SPEED = 4.


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


"""
Boid class parameters
"""
# view of neighbor agents
RADIUS_VIEW = 70
# weights for velocity forces
COHESION_WEIGHT = 5.
ALIGNMENT_WEIGHT = 15.
SEPARATION_WEIGHT = 5.
