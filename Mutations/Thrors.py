import random
from copy import deepcopy


def Thrors(n):
    def inner_Thrors(ind):
        new_ind = deepcopy(ind)  # Creating a copy of our indivudual
        index_l = random.sample(range(1, len(ind) - 1), k=n)
        # Selecting the indexes we will shift
        index_l.sort()
        # Sorting the indexes to guarantee they are in order
        for i in range(n):
            new_ind[index_l[i]] = ind[index_l[n - 1]]\
                  if i == 0 else ind[index_l[i - 1]]
        # Iterating through the list of indexes to shift and shifting
        # the elements in those positions to the next index in the list
        # The element in the last index goes to the position of the first index
        return new_ind
    return inner_Thrors
