import math
import random
import time
from dataclasses import dataclass

@dataclass
class Body:
    x: float
    y: float
    z: float
    vx: float
    vy: float
    vz: float
    mass: float
    
@dataclass
class SimulationConfig:
    particle_count: int
    steps: int
    dt: float
    seed: int
    softening: float

def run_single_particle_demo():
    x = 0.0
    v = 1.0
    dt = 0.1

    for step in range(10):
        x = x + v * dt
        print(f"step {step}: x = {x}")

if __name__ == "__main__":
    run_single_particle_demo()