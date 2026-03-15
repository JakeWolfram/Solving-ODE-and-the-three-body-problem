from typing import Any
import numpy as np
class spaceObject:

    def __init__(self, r, mass: float):
        if len(r) != 3:
            TypeError("r should have a length of 3")
        self.r = np.array(r)
        self.mass = mass
        self.x = r[0]
        self.y = r[1]
        self.z = r[2]
    