import random
from copy import deepcopy


def invert_0point(ind):
    ind_c = deepcopy(ind)
    ind_c.reverse()  # Inverting the individual
    return ind_c


def invert_1point(ind):
    index = random.randint(1, len(ind)-3)
    # Randomly selecting the split point
    part1 = ind[1:index]
    part1.reverse()
    part2 = ind[index:len(ind)-1]
    part2.reverse()
    # Splitting the indivual in 2 parts and inverting those parts
    return ind[:1] + part1 + part2 + ind[-1:]
    # Rebuilding the individual with the reversed parts
