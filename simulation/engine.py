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

def gravity_from_body(target: Body, source: Body, g: float, softening: float):
    dx = source.x - target.x
    dy = source.y - target.y
    dz = source.z - target.z
    r2 = dx * dx + dy * dy + dz * dz + softening * softening
    inv_r = 1.0 / math.sqrt(r2)
    inv_r3 = inv_r * inv_r * inv_r
    scale = g * source.mass * inv_r3
    return dx * scale, dy * scale, dz * scale
