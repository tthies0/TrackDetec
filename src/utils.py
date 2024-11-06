import numpy

def dist(pos_a: tuple[float, float], pos_b: tuple[float, float]) -> float:
    return numpy.sqrt((pos_a[0] - pos_b[0]) ** 2 + (pos_a[1] - pos_b[1]) ** 2)