import pygame
import numpy as np
from simulation import helperfunctions

"""
General Object class to load images in the environment 
"""


class Objects(pygame.sprite.Sprite):
    def __init__(self):
        super(Objects, self).__init__()
        self.walls = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()

    def add_object(self, file, pos, scale, type):
        if type == 'wall':
            self.walls.add(
                Object(filename=file, pos=np.array(pos), scale=scale))
        elif type == 'building':
            self.buildings.add(
                Object(filename=file, pos=np.array(pos), scale=scale))
        else:
            print('object type not specified')


class Object(pygame.sprite.Sprite):

    def __init__(self, filename=None, pos=None, scale=None):
        super(Object, self).__init__()
        self.image, self.rect = helperfunctions.image_with_rect(
            filename, scale)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pos if pos is not None else np.zeros(2)
        self.rect = self.image.get_rect(center=self.pos)

    def display(self, screen):
        screen.blit(self.image, self.rect)

