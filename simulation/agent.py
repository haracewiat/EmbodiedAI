import numpy as np
import random
import pygame
from simulation import helperfunctions


"""
General agent properties, which are common across all types of agents 
"""

#defines general agent properties
class Agent(pygame.sprite.Sprite): #super class
    def __init__(self, pos=None, v=None,
                 image=None, color=None,
                 max_speed=None, min_speed=None,
                 mass=None, width=None, height=None,
                 dT=None):
        super(Agent, self).__init__()

        self.image_file = image
        if self.image_file != None: #load image from file
            self.base_image, self.rect = helperfunctions.image_with_rect(self.image_file, [width, height])
            self.image = self.base_image
            self.mask = pygame.mask.from_surface(self.image)
            self.mask = self.mask.scale((12, 10))

        else: #draw an agent
            self.image = pygame.Surface((width,height), pygame.SRCALPHA)
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

        self.mass = mass
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.wandering_angle = helperfunctions.randrange(-np.pi, np.pi)  # set a random wandering angle

        self.steering = np.zeros(2)
        self.pos = np.zeros(2) if pos is None else pos
        self.v = self.set_velocity() if v is None else v
        self.dT= dT

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
        self.rect.center = tuple(pos)  # update the rect position as thats actually displayed

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, v):
        self._v = v
        if self.image_file: self._rotate_image()

    def _rotate_image(self):
        """Rotate base image using the velocity and assign to image."""
        angle = -np.rad2deg(np.angle(self.v[0] + 1j * self.v[1])) #using complex number to estimate the angle for rotation
        self.image = pygame.transform.rotate(self.base_image, angle) #rotates the image
        self.rect = self.image.get_rect(center=self.rect.center)


    def set_velocity(self):
        angle = np.pi * (2 * np.random.rand() - 1)
        velocity = [random.randrange(1, self.max_speed + 1) * helperfunctions.plusminus(),
                    random.randrange(1, self.max_speed + 1) * helperfunctions.plusminus()]
        velocity *= np.array([np.cos(angle), np.sin(angle)])
        return velocity

    def wander(self, wander_dist, wander_radius, wander_angle):
        """
        Function to make the agents to perform random movement
        """
        rands = 2 * np.random.rand() - 1
        cos = np.cos(self.wandering_angle)
        sin = np.sin(self.wandering_angle)
        n_v = helperfunctions.normalize(self.v)
        circle_center = n_v * wander_dist
        displacement = np.dot(np.array([[cos, -sin], [sin, cos]]), n_v * wander_radius)
        wander_force = circle_center + displacement
        self.wandering_angle += wander_angle * rands
        return wander_force

    def avoid_obstacle(self):
        """
        Function to avoid obstacles
        need to take into account whether agents inside/outside the obstacle
        moves the agent away from the boarder by distance equivalent to its size
        """
        #adjust the velocity by rotating it around
        self.v = (helperfunctions.rotate(helperfunctions.normalize(self.v)) * helperfunctions.norm(self.v))
        self.pos += self.v *1.5

    def update(self):
        self.v = helperfunctions.truncate(self.v + self.steering, self.max_speed, self.min_speed)
        self.pos += self.v * self.dT


    def display(self, screen):
        screen.blit(self.image, self.rect)

    def reset_frame(self):
        self.steering = np.zeros(2)
<<<<<<< Updated upstream
=======

    def change_state(self, state, swarm):
        if self.state != state:
            self.state = state

            # Update drawing
            self.set_color()
            self.draw()

            # Update data
            if self.state == State.RECOVERED:
                swarm.data[State.INFECTIOUS] -= 1
            elif self.state == State.INFECTIOUS:
                swarm.data[State.SUSCEPTIBLE] -= 1
            elif self.state == State.INFECTIOUS:
                swarm.data[State.EXPOSED] -= 1
            # swarm.data[State[self.state] - 1] -= 1
            swarm.data[self.state] += 1

    def draw(self):
        self.image = pygame.Surface((p.WIDTH, p.HEIGHT), pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(self.image, int(
            p.WIDTH/2), int(p.WIDTH/2), int(p.WIDTH/2)-1, self.color)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def set_color(self):
        if self.state == State.SUSCEPTIBLE:
            self.color = config.SUSCEPTIBLE
        elif self.state == State.INFECTIOUS:
            self.color = config.INFECTIOUS
        elif self.state == State.RECOVERED:
            self.color = config.RECOVERED
        elif self.state == State.EXPOSED:
            self.color = config.EXPOSED


class State(Enum):
    SUSCEPTIBLE = 0
    INFECTIOUS = 1
    RECOVERED = 2
    VACCINATED = 3
    EXPOSED = 1
>>>>>>> Stashed changes
