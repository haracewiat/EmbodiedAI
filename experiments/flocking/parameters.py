"""
Parameter settings to be loaded in the model
"""

"""
General settings (DO NOT CHANGE)
"""
#screen settings
S_WIDTH, S_HEIGHT = 1000, 1000
SCREEN = (S_WIDTH, S_HEIGHT)

#choose how long to run the simulation
#-1 : infinite, N: finite
FRAMES=-1

#choose swarm type
SWARM = 'Flock'
#define the number of agents
N_AGENTS = 40
#object location
OBJECT_LOC = [S_WIDTH/2., S_HEIGHT/2.]


#Agent Settings:
#agent size
WIDTH=10
HEIGHT=8
#update
dT=0.2
#agents mass
MASS=20
#agent maximum/minimum speed
MAX_SPEED = 7.
MIN_SPEED = 4.


#Boid Settings:
#view of neighbor agents
RADIUS_VIEW=70
#velocity force
MAX_FORCE = 8.

"""
Simulation settings to adjust:
"""

"""
Flock class parameters (defines the environment of where the flock to act)
"""
#Define the environment
OBSTACLES = True
OUTSIDE = True
CONVEX = True

"""
Boid class parameters
"""
#weights for velocity forces
COHESION_WEIGHT = 3.5
ALIGNMENT_WEIGHT = 4.5
SEPARATION_WEIGHT = 6.









