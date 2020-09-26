import numpy as np


class BattleMap(object):
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.grid = np.full(shape=(width, height, depth),
                            fill_value=Air, dtype=Tile)

    def __getitem__(self, key):
        return self.grid[key]


class Tile(object):
    def __init__(self):
        pass


class Air(Tile):
    def __init__(self):
        self.opaque = False
        self.solid = False


class Solid(Tile):
    def __init__(self):
        self.opaque = True
        self.solid = True


class Dirt(Solid):
    def __init__(self):
        super().__init__()
        self.sprite_path = 'resources/dirt.jpg'


class Grass(Dirt):
    def __init__(self):
        super().__init__()
        self.sprite_path = 'resources/grass.jpg'
