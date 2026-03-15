from abc import ABC, abstractmethod
import numpy as np


class Method(ABC):
    @abstractmethod
    def next_step(self, f, t: float, y: np.ndarray, h: float) -> np.ndarray:
        pass