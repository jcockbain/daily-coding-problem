from random import uniform
from math import pow


def generate():
    return (uniform(-1, 1), uniform(-1, 1))


def is_in_circle(coords):
    return coords[0] * coords[0] + coords[1] * coords[1] < 1


def estimate(iterations):
    in_circle = len([x for x in range(iterations) if is_in_circle(generate())])
    return 4 * (in_circle / iterations)
