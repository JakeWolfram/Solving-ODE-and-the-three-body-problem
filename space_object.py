import numpy as np
class SpaceObject:
    def __init__(self, r, v, mass: float):
        if len(r) != 3:
            raise TypeError("r must have length 3")
        if len(v) != 3:
            raise TypeError("v must have length 3")

        self.r = np.array(r, dtype=float)
        self.v = np.array(v, dtype=float)
        self.mass = float(mass)