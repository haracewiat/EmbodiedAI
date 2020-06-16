from experiments.covid import parameters as p
from enum import Enum

buildings = []
walls = []


def scenario0():
    return buildings, walls


def scenario1():

    # Dummy, change to actual wall Object
    walls.append(1)

    return buildings, walls


def scenario2():

    buildings.append(Building(Building_type.HOME))
    buildings.append(Building(Building_type.SHOP))

    return buildings, walls


class Building:
    def __init__(self, type):
        # concat file name instead of dictionary (TODO)
        self.img = self.get_img(type)
        # Change to fit a random partition
        self.loc = [p.SCREEN[0] / 2., p.SCREEN[1] / 2.]

    def get_img(self, type):

        img = {
            Building_type.HOME: 'experiments/covid/images/buildings/home.png',
            Building_type.SHOP: 'experiments/covid/images/buildings/shop.png',
        }

        return img.get(type)


class Building_type(Enum):
    HOME = 0
    SHOP = 1
