import numpy as np
from method import Method


class AdamsBashforth(Method):
    def __init__(self):
        self.prev_f = None

    def next_step(self, f, t: float, y: np.ndarray, h: float) -> np.ndarray:
        current_f = f(t, y)

        if self.prev_f is None:
            y_next = y + h * current_f
        else:
            y_next = y + h * (1.5 * current_f - 0.5 * self.prev_f)

        self.prev_f = current_f
        return y_next




