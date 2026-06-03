#READ ME!!!!!!!!!!

#we are building a cloud-based N-body simulation experiment platform.

# it is not just a galaxy animation. The goal is to let users run reproducible 
# gravity simulations, compare algorithms, measure accuracy/performance, 
# and export meaningful scientific results. 

#the core scientific problem is:

# given many bodies with mass, position, and velocity, 
# simulate how gravity changes their motion over time.

#The cs/engineering side is:

# build the simulation engine, benchmarking system, 
# backend job queue, database, and eventually a web dashboard.

#main algorithms

#we gonna use two simulation method. (FOR NOW):

# 1. direct n-body - every body interacts with every other body. complexity - O(N**2)
# This is slow but accurate, and it becomes our baseline truth.

# 2. barnes-hut - distant groups of bodies are approximated using a quadtree/octree and center of mass.
# complexity - O(n log n) faster but approximate.

#basically 
# direct n-body vs barnes-hut
# speed vs accuracy
# theta value vs error
# energy drift over time
# angular momentum drift over time

#ermuun help implement/check:
# total energy
# kinetic energy
# potential energy
# angular momentum
# center of mass drift

#and benchmark design
# direct vs Barnes-Hut force error
# theta vs runtime
# theta vs accuracy
# timestep vs energy drift
# particle count vs performance

#and initial conditions
# two-body orbit
# three-body problem
# star cluster
# galaxy disk
# keplerian disk around central mass

#also help with shi like - 
# How do we know the simulation is not nonsense?
# Does total energy stay reasonably stable? etc

#you do not need to write code immediately. 
# help me define the equations and tests we will use to prove the simulation is correct.
# i created a doc where you can write those (physics_model.md)










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
