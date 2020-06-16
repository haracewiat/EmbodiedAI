from experiments.covid import parameters as p
from enum import Enum

buildings = []
walls = []


def scenario0():
    return buildings, walls


def scenario1():
    walls.append(Wall(1))
    return buildings, walls


def scenario2():
    walls.append(Wall(2))
    return buildings, walls


def scenario3():
    walls.append(Wall(3))
    return buildings, walls


def scenario4():
    buildings.append(Building(Building_type.HOME))
    buildings.append(Building(Building_type.SHOP))

    return buildings, walls


class Wall:
    def __init__(self, index):
        self.img = 'experiments/covid/images/walls/wall' + str(index) + '.png'
        self.position = [p.SCREEN[0] / 2., p.SCREEN[1] / 2.]
        self.scale = [p.S_WIDTH, p.S_HEIGHT]


class Building:
    def __init__(self, type):
        self.img = 'experiments/covid/images/buildings/' + \
            str(type).lower().replace("building_type.", "") + '.png'
        # TODO Change to fit a random partition
        self.position = [p.SCREEN[0] / 2., p.SCREEN[1] / 2.]


class Building_type(Enum):
    HOME = 0
    SHOP = 1
