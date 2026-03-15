import numpy as np
from space_object import SpaceObject
from three_body_system import ThreeBodySystem
from simulation_runner import SimulationRunner
from Adams_Bashforth import AdamsBashforth

r1 = SpaceObject([1.0e11, 0.0, 0.0], [0.0, 3.0e4, 0.0], 2.0e30)
r2 = SpaceObject([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 6.0e24)
r3 = SpaceObject([1.0e11 + 3.84e8, 0.0, 0.0], [0.0, 3.1e4, 0.0], 7.35e22)

system = ThreeBodySystem(r1.mass, r2.mass, r3.mass)

y0 = np.concatenate([r1.r, r2.r, r3.r, r1.v, r2.v, r3.v])

runner = SimulationRunner(system, AdamsBashforth())

times, states = runner.run(
    t0=0.0,
    y0=y0,
    h=60.0,
    steps=1000
)

print("Final state:")
print(states[-1])

print("Initial energy:", system.total_energy(states[0]))
print("Final energy:", system.total_energy(states[-1]))