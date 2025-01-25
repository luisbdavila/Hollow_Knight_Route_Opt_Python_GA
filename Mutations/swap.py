import random
from copy import deepcopy


def swap(ind):
    i_1, i_2 = random.sample(range(1, len(ind) - 1), k=2)
    # Randomly selecting the indexes of the elements to swap
    # (without replacement to avoid getting the same index twice)
    new_ind = deepcopy(ind)
    # Creating a copy of our original individual
    new_ind[i_1] = ind[i_2]
    new_ind[i_2] = ind[i_1]
    # Swapping the elements in the new individual
    return new_ind
