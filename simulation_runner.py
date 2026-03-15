import numpy as np
from method import Method
from three_body_system import ThreeBodySystem


class SimulationRunner:
    def __init__(self, system: ThreeBodySystem, method: Method):
        self.system = system
        self.method = method

    def set_method(self, method: Method) -> None:
        self.method = method

    def step(self, t: float, y: np.ndarray, h: float) -> np.ndarray:
        return self.method.next_step(self.system.derivatives, t, y, h)

    def run(self, t0: float, y0: np.ndarray, h: float, steps: int):
        times = [t0]
        states = [y0.copy()]

        t = t0
        y = y0.copy()

        for _ in range(steps):
            y = self.step(t, y, h)
            t += h
            times.append(t)
            states.append(y.copy())

        return np.array(times), np.array(states)