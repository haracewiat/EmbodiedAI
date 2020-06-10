from experiments.aggregation import parameters as p


def experiment0(screensize):  # Single aggregation site
    obstacles = []
    obstacles.append(
        obstacle([screensize[0] / 2., screensize[1] / 2.],
                 [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False)
    )

    return obstacles


def experiment1(screensize):  # Two aggregation site (different sizes)
    obstacles = []
    # Sorry for the hardcoded values
    obstacles.append(
        obstacle([screensize[0] / 3.5, screensize[1] / 2.],
                 [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )
    obstacles.append(
        obstacle([(screensize[0] / 3.5) * 2.5, screensize[1] / 2.],
                 [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], True),
    )

    return obstacles


def experiment2(screensize):  # Two aggregation site (same sizes)
    obstacles = []
    # Same here :(
    obstacles.append(
        obstacle([screensize[0] / 3.5, screensize[1] / 2.],
                 [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )
    obstacles.append(
        obstacle([(screensize[0] / 3.5) * 2.5, screensize[1] / 2.],
                 [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )

    return obstacles


class obstacle:
    def __init__(self, area_loc, scale, big):
        self.img = 'experiments/aggregation/images/greyc1.png' if not big else 'experiments/aggregation/images/greyc2.png'
        self.area_loc = area_loc
        self.scale = scale if not big else tuple(
            int(dimension*1.2) for dimension in scale)
