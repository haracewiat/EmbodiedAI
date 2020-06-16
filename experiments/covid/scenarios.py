from experiments.covid import parameters as p
from enum import Enum


def scenario0():
    buildings = []
    return buildings


def scenario1():
    buildings = []
    buildings.append(Building(Building_type.HOME))
    buildings.append(Building(Building_type.SHOP))

    return buildings


class Building:
    def __init__(self, type):
        # concat file name instead of dictionary (TODO)
        self.img = self.get_img(type)
        # Change to fit a random partition
        self.loc = [p.SCREEN[0] / 2., p.SCREEN[1] / 2.]

    def get_img(self, type):

        img = {
            Building_type.HOME: 'experiments/covid/images/home.png',
            Building_type.SHOP: 'experiments/covid/images/shop.png',
        }

        return img.get(type)


class Building_type(Enum):
    HOME = 0
    SHOP = 1
