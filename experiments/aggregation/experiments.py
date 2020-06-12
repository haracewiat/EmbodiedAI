from experiments.aggregation import parameters as p


def experiment0(screensize):  # Single aggregation site
    sites = []
    sites.append(
        site([screensize[0] / 2., screensize[1] / 2.],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False)
    )

    return sites


def experiment1(screensize):  # Two aggregation site (different sizes)
    sites = []
    # Sorry for the hardcoded values
    sites.append(
        site([screensize[0] / 3.5, screensize[1] / 2.],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )
    sites.append(
        site([(screensize[0] / 3.5) * 2.5, screensize[1] / 2.],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], True),
    )

    return sites


def experiment2(screensize):  # Two aggregation site (same sizes)
    sites = []
    # Same here :(
    sites.append(
        site([screensize[0] / 3.5, screensize[1] / 2.],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )
    sites.append(
        site([(screensize[0] / 3.5) * 2.5, screensize[1] / 2.],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )

    return sites


def experiment3(screensize):  # Two aggregation site (same sizes)
    sites = []
    # Same here :(
    sites.append(
        site([screensize[0] / 3.5, screensize[1] / 2.],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], False),
    )
    sites.append(
        site([(screensize[0] / 2.2), screensize[1] / 3.5],
             [int(p.S_WIDTH*0.11), int(p.S_HEIGHT*0.11)], True),
    )

    return sites


class site:
    def __init__(self, area_loc, scale, big):
        self.img = 'experiments/aggregation/images/greyc1.png' if not big else 'experiments/aggregation/images/greyc2.png'
        self.area_loc = area_loc
        self.scale = scale if not big else tuple(
            int(dimension*1.2) for dimension in scale)
