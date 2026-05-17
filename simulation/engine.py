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
    
class SimulationConfig:
    particle_count: int
    steps: int
    dt: float
    seed: int
    softening: float
