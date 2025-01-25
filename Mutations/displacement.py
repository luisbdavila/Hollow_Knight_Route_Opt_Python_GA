import random


def displacement(size):
    # Size defines the number of elements that will be displaced
    def inner_D(ind):
        i_displaced_start = random.randint(1, len(ind) - 1 - size)
        # Randomly defining the start of the displaced area
        displaced = [ind[i_displaced_start + k] for k in range(size)]
        # Getting the displaced elements
        new_ind = [bit for bit in ind if bit not in displaced]
        # Creating a new individual without the displaced portion
        new_i = random.randint(1, len(new_ind) - 1)
        # Randomly selecting the new location of the displaced part
        # in the new individual (can't be at the start or the end)
        return new_ind[:new_i] + displaced + new_ind[new_i:]
        # Inserting the displaced part into the new individual
    return inner_D
